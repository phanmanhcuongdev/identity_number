import argparse
import json
import os
import sys
import time
from pathlib import Path


def preconfigure_blas_threads(argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--threads", type=int, default=30)
    args, _ = parser.parse_known_args(argv)
    threads = str(max(1, args.threads))
    for name in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS",
    ):
        os.environ.setdefault(name, threads)


preconfigure_blas_threads(sys.argv[1:])

import numpy as np


INPUT_SIZE = 784
NUM_CLASSES = 10
HIDDEN1 = 1024
HIDDEN2 = 512
HIDDEN3 = 256


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a 784-1024-512-256-10 ANN on train_infinity.npy."
    )
    parser.add_argument("--x-path", default="train_infinity.npy")
    parser.add_argument("--y-path", default="labels_infinity.npy")
    parser.add_argument("--checkpoint-dir", default="checkpoints_infinity")
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=4096)
    parser.add_argument("--val-size", type=int, default=100_000)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    parser.add_argument("--lr-decay", type=float, default=0.92)
    parser.add_argument("--weight-decay", type=float, default=1e-5)
    parser.add_argument("--beta1", type=float, default=0.9)
    parser.add_argument("--beta2", type=float, default=0.999)
    parser.add_argument("--epsilon", type=float, default=1e-8)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--log-every", type=int, default=100)
    parser.add_argument("--threads", type=int, default=30)
    parser.add_argument("--resume", default=None, help="Path to a .npz checkpoint.")
    return parser.parse_args()


def load_dataset(x_path, y_path):
    print(f"Loading X from {x_path} with mmap_mode=None...")
    X = np.load(x_path, mmap_mode=None)
    print(f"Loading y from {y_path} with mmap_mode=None...")
    y = np.load(y_path, mmap_mode=None)

    if X.ndim != 2:
        raise ValueError(f"X must be 2D, got shape {X.shape}.")
    if X.shape[1] == INPUT_SIZE:
        pass
    elif X.shape[0] == INPUT_SIZE:
        print("Detected X shape as 784 x N; transposing to N x 784 view.")
        X = X.T
    else:
        raise ValueError(f"X must have 784 features, got shape {X.shape}.")

    y = np.asarray(y).reshape(-1).astype(np.int64, copy=False)
    if X.shape[0] != y.shape[0]:
        raise ValueError(f"X and y size mismatch: {X.shape[0]} vs {y.shape[0]}.")
    if np.any((y < 0) | (y >= NUM_CLASSES)):
        raise ValueError("Labels must be integers in [0, 9].")

    if X.dtype != np.float32:
        print(f"Converting X from {X.dtype} to float32 in RAM...")
        X = X.astype(np.float32, copy=False)
    if X.max() > 1.5:
        print("Normalizing pixels to [0, 1] in-place...")
        X /= np.float32(255.0)

    if not X.flags.c_contiguous:
        print("Making X C-contiguous for faster BLAS matrix multiplication...")
        X = np.ascontiguousarray(X, dtype=np.float32)

    return X, y


def init_params(rng):
    return {
        "W1": (rng.standard_normal((INPUT_SIZE, HIDDEN1), dtype=np.float32) * np.sqrt(2.0 / INPUT_SIZE)).astype(np.float32),
        "b1": np.zeros((HIDDEN1,), dtype=np.float32),
        "W2": (rng.standard_normal((HIDDEN1, HIDDEN2), dtype=np.float32) * np.sqrt(2.0 / HIDDEN1)).astype(np.float32),
        "b2": np.zeros((HIDDEN2,), dtype=np.float32),
        "W3": (rng.standard_normal((HIDDEN2, HIDDEN3), dtype=np.float32) * np.sqrt(2.0 / HIDDEN2)).astype(np.float32),
        "b3": np.zeros((HIDDEN3,), dtype=np.float32),
        "W4": (rng.standard_normal((HIDDEN3, NUM_CLASSES), dtype=np.float32) * np.sqrt(2.0 / HIDDEN3)).astype(np.float32),
        "b4": np.zeros((NUM_CLASSES,), dtype=np.float32),
    }


def init_adam_state(params):
    state = {}
    for name, value in params.items():
        state[f"m_{name}"] = np.zeros_like(value)
        state[f"v_{name}"] = np.zeros_like(value)
    return state


def relu(x):
    return np.maximum(x, 0.0)


def forward(params, X):
    Z1 = X @ params["W1"] + params["b1"]
    A1 = relu(Z1)
    Z2 = A1 @ params["W2"] + params["b2"]
    A2 = relu(Z2)
    Z3 = A2 @ params["W3"] + params["b3"]
    A3 = relu(Z3)
    logits = A3 @ params["W4"] + params["b4"]
    logits -= np.max(logits, axis=1, keepdims=True)
    exp_logits = np.exp(logits, dtype=np.float32)
    probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)
    return Z1, A1, Z2, A2, Z3, A3, probs


def loss_and_accuracy(probs, y):
    batch = y.shape[0]
    clipped = np.clip(probs[np.arange(batch), y], 1e-8, 1.0)
    loss = -float(np.mean(np.log(clipped)))
    acc = float(np.mean(np.argmax(probs, axis=1) == y))
    return loss, acc


def backward(params, cache, X, y, weight_decay):
    Z1, A1, Z2, A2, Z3, A3, probs = cache
    batch = X.shape[0]

    dlogits = probs
    dlogits[np.arange(batch), y] -= 1.0
    dlogits /= np.float32(batch)

    grads = {
        "W4": A3.T @ dlogits + weight_decay * params["W4"],
        "b4": np.sum(dlogits, axis=0),
    }
    dA3 = dlogits @ params["W4"].T
    dZ3 = dA3 * (Z3 > 0)
    grads["W3"] = A2.T @ dZ3 + weight_decay * params["W3"]
    grads["b3"] = np.sum(dZ3, axis=0)

    dA2 = dZ3 @ params["W3"].T
    dZ2 = dA2 * (Z2 > 0)
    grads["W2"] = A1.T @ dZ2 + weight_decay * params["W2"]
    grads["b2"] = np.sum(dZ2, axis=0)

    dA1 = dZ2 @ params["W2"].T
    dZ1 = dA1 * (Z1 > 0)
    grads["W1"] = X.T @ dZ1 + weight_decay * params["W1"]
    grads["b1"] = np.sum(dZ1, axis=0)
    return grads


def adam_update(params, grads, state, lr, step, beta1, beta2, epsilon):
    beta1_correction = 1.0 - beta1**step
    beta2_correction = 1.0 - beta2**step
    for name in params:
        m_name = f"m_{name}"
        v_name = f"v_{name}"
        state[m_name] = beta1 * state[m_name] + (1.0 - beta1) * grads[name]
        state[v_name] = beta2 * state[v_name] + (1.0 - beta2) * (grads[name] * grads[name])
        m_hat = state[m_name] / beta1_correction
        v_hat = state[v_name] / beta2_correction
        params[name] -= lr * m_hat / (np.sqrt(v_hat) + epsilon)


def evaluate(params, X, y, indices, batch_size):
    total_loss = 0.0
    total_correct = 0
    total = 0
    for start in range(0, indices.shape[0], batch_size):
        batch_idx = indices[start : start + batch_size]
        xb = X[batch_idx]
        yb = y[batch_idx]
        *_, probs = forward(params, xb)
        loss, _ = loss_and_accuracy(probs, yb)
        preds = np.argmax(probs, axis=1)
        total_loss += loss * yb.shape[0]
        total_correct += int(np.sum(preds == yb))
        total += yb.shape[0]
    return total_loss / total, total_correct / total


def save_checkpoint(path, params, state, metadata):
    path.parent.mkdir(parents=True, exist_ok=True)
    arrays = {}
    arrays.update(params)
    arrays.update(state)
    arrays["metadata"] = np.array(json.dumps(metadata), dtype=object)
    np.savez_compressed(path, **arrays)


def load_checkpoint(path):
    data = np.load(path, allow_pickle=True)
    params = {name: data[name].astype(np.float32, copy=False) for name in ("W1", "b1", "W2", "b2", "W3", "b3", "W4", "b4")}
    state = {name: data[name].astype(np.float32, copy=False) for name in data.files if name.startswith(("m_", "v_"))}
    metadata = json.loads(str(data["metadata"].item())) if "metadata" in data.files else {}
    return params, state, metadata


def main():
    args = parse_args()
    rng = np.random.default_rng(args.seed)
    X, y = load_dataset(args.x_path, args.y_path)
    n_samples = y.shape[0]
    val_size = min(args.val_size, max(1, n_samples // 10))

    all_indices = rng.permutation(n_samples)
    val_idx = all_indices[:val_size]
    train_idx = all_indices[val_size:]
    if train_idx.size == 0:
        raise ValueError("Training set is empty after validation split.")

    if args.resume:
        params, state, metadata = load_checkpoint(args.resume)
        start_epoch = int(metadata.get("epoch", 0)) + 1
        global_step = int(metadata.get("global_step", 0))
        print(f"Resumed from {args.resume}: epoch={start_epoch}, global_step={global_step}")
    else:
        params = init_params(rng)
        state = init_adam_state(params)
        start_epoch = 1
        global_step = 0

    batches_per_epoch = int(np.ceil(train_idx.size / args.batch_size))
    print(
        "Training config: "
        f"samples={n_samples:,}, train={train_idx.size:,}, val={val_idx.size:,}, "
        f"batch_size={args.batch_size}, epochs={args.epochs}, batches/epoch={batches_per_epoch}, "
        f"threads={args.threads}"
    )
    print("Architecture: 784 -> 1024 -> 512 -> 256 -> 10, optimizer=Adam")

    checkpoint_dir = Path(args.checkpoint_dir)
    for epoch in range(start_epoch, args.epochs + 1):
        epoch_start = time.time()
        lr = args.learning_rate * (args.lr_decay ** (epoch - 1))
        rng.shuffle(train_idx)
        running_loss = 0.0
        running_correct = 0
        running_seen = 0

        for batch_no, start in enumerate(range(0, train_idx.size, args.batch_size), start=1):
            batch_idx = train_idx[start : start + args.batch_size]
            xb = X[batch_idx]
            yb = y[batch_idx]

            cache = forward(params, xb)
            probs = cache[-1]
            batch_loss, batch_acc = loss_and_accuracy(probs, yb)
            grads = backward(params, cache, xb, yb, args.weight_decay)
            global_step += 1
            adam_update(params, grads, state, lr, global_step, args.beta1, args.beta2, args.epsilon)

            running_loss += batch_loss * yb.shape[0]
            running_correct += int(batch_acc * yb.shape[0])
            running_seen += yb.shape[0]

            if batch_no % args.log_every == 0 or batch_no == batches_per_epoch:
                avg_loss = running_loss / running_seen
                avg_acc = running_correct / running_seen
                print(
                    f"Epoch {epoch:03d}/{args.epochs:03d} | "
                    f"Batch {batch_no:05d}/{batches_per_epoch:05d} | "
                    f"LR {lr:.6g} | Loss {avg_loss:.4f} | Acc {avg_acc:.4f}"
                )

        val_loss, val_acc = evaluate(params, X, y, val_idx, args.batch_size)
        elapsed = time.time() - epoch_start
        metadata = {
            "epoch": epoch,
            "global_step": global_step,
            "learning_rate": lr,
            "train_samples": int(train_idx.size),
            "val_samples": int(val_idx.size),
            "val_loss": float(val_loss),
            "val_accuracy": float(val_acc),
            "architecture": "784-1024-512-256-10",
        }
        ckpt_path = checkpoint_dir / f"infinity_epoch_{epoch:03d}.npz"
        latest_path = checkpoint_dir / "infinity_latest.npz"
        save_checkpoint(ckpt_path, params, state, metadata)
        save_checkpoint(latest_path, params, state, metadata)
        print(
            f"Epoch {epoch:03d} done in {elapsed / 60:.1f} min | "
            f"Val Loss {val_loss:.4f} | Val Acc {val_acc:.4f} | "
            f"Saved {ckpt_path}"
        )


if __name__ == "__main__":
    main()
