import os
import numpy as np
from pathlib import Path
from sklearn.metrics import classification_report, confusion_matrix
from matplotlib import pyplot as plt

MODEL_FILE = "model_weights.npz"

INPUT_SIZE = 784
NUM_CLASSES = 10

HIDDEN_LAYERS = [512, 256]

EPOCHS = 15
BATCH_SIZE = 128

LR = 1e-3
LR_DECAY = 0.92

BETA1 = 0.9
BETA2 = 0.999
EPS = 1e-8
WEIGHT_DECAY = 1e-5

def batch_generator(X, y, indices, batch_size):
    n = len(indices)
    while True:
        pos = np.random.randint(0, n, batch_size)
        idx = indices[pos]

        xb = X[idx]
        yb = y[idx]
        yield xb, yb


class ANN:
    def __init__(self, layer_sizes=None, model_file=None):

        self.layer_sizes = layer_sizes or HIDDEN_LAYERS

        if model_file and Path(model_file).exists():
            data = np.load(model_file, allow_pickle=True)
            self.params = {k: data[k] for k in data.files}
        else:
            self.params = self.init_params()

        self.m, self.v = self.init_adam()
        self.t = 0

    def init_params(self):
        params = {}

        dims = [INPUT_SIZE] + self.layer_sizes + [NUM_CLASSES]

        for i in range(len(dims) - 1):
            fan_in = dims[i]
            fan_out = dims[i + 1]

            params[f"W{i+1}"] = np.random.randn(fan_in, fan_out).astype(np.float32) * np.sqrt(2 / fan_in)
            params[f"b{i+1}"] = np.zeros(fan_out, dtype=np.float32)

        return params

    def init_adam(self):
        m, v = {}, {}
        for k in self.params:
            m[k] = np.zeros_like(self.params[k])
            v[k] = np.zeros_like(self.params[k])
        return m, v

    def relu(self, x):
        return np.maximum(x, 0)

    def forward(self, X):
        cache = {"A0": X}
        A = X

        L = len(self.layer_sizes) + 1

        for i in range(1, L + 1):
            W = self.params[f"W{i}"]
            b = self.params[f"b{i}"]

            Z = A @ W + b

            if i != L:
                A = self.relu(Z)
            else:
                A = Z 

            cache[f"Z{i}"] = Z
            cache[f"A{i}"] = A

        logits = A

        logits = logits - np.max(logits, axis=1, keepdims=True)
        exp = np.exp(logits)
        probs = exp / np.sum(exp, axis=1, keepdims=True)

        return cache, probs

    def loss_acc(self, probs, y):
        n = len(y)
        loss = -np.mean(np.log(probs[np.arange(n), y] + 1e-8))
        acc = np.mean(np.argmax(probs, axis=1) == y)
        return loss, acc

    def backward(self, cache, probs, X, y):
        grads = {}
        n = len(y)

        L = len(self.layer_sizes) + 1

        dZ = probs.copy()
        dZ[np.arange(n), y] -= 1
        dZ /= n

        for i in reversed(range(1, L + 1)):
            A_prev = cache[f"A{i-1}"]
            W = self.params[f"W{i}"]

            grads[f"W{i}"] = A_prev.T @ dZ + WEIGHT_DECAY * W
            grads[f"b{i}"] = np.sum(dZ, axis=0)

            if i > 1:
                dA_prev = dZ @ W.T
                dZ = dA_prev * (cache[f"Z{i-1}"] > 0)

        return grads

    def adam(self, grads, lr):
        self.t += 1

        for k in self.params:
            self.m[k] = BETA1 * self.m[k] + (1 - BETA1) * grads[k]
            self.v[k] = BETA2 * self.v[k] + (1 - BETA2) * (grads[k] ** 2)

            m_hat = self.m[k] / (1 - BETA1 ** self.t)
            v_hat = self.v[k] / (1 - BETA2 ** self.t)

            self.params[k] -= lr * m_hat / (np.sqrt(v_hat) + EPS)

    def train(self, X_train, y_train, X_val=None, y_val=None):

        train_idx = np.arange(len(y_train))
        train_gen = batch_generator(X_train, y_train, train_idx, BATCH_SIZE)

        val_gen = None
        if X_val is not None:
            val_idx = np.arange(len(y_val))
            val_gen = batch_generator(X_val, y_val, val_idx, BATCH_SIZE)

        for epoch in range(EPOCHS):

            lr = LR * (LR_DECAY ** epoch)

            total_loss = 0
            total_acc = 0
            seen = 0

            steps = len(y_train) // BATCH_SIZE
            for _ in range(steps):
                xb, yb = next(train_gen)

                cache, probs = self.forward(xb)

                loss, acc = self.loss_acc(probs, yb)

                grads = self.backward(cache, probs, xb, yb)
                self.adam(grads, lr)

                total_loss += loss * len(yb)
                total_acc += acc * len(yb)
                seen += len(yb)

            train_loss = total_loss / seen
            train_acc = total_acc / seen

            if X_val is not None:

                val_loss = 0
                val_acc = 0
                val_seen = 0

                val_steps = len(y_val) // BATCH_SIZE

                for _ in range(val_steps):
                    xb, yb = next(val_gen)
                    _, probs = self.forward(xb)
                    loss, acc = self.loss_acc(probs, yb)

                    val_loss += loss * len(yb)
                    val_acc += acc * len(yb)
                    val_seen += len(yb)

                val_loss /= val_seen
                val_acc /= val_seen

                print(
                    f"Epoch {epoch+1}/{EPOCHS} | "
                    f"Train Loss: {train_loss:.4f} | "
                    f"Train Acc: {train_acc:.4f} | "
                    f"Val Loss: {val_loss:.4f} | "
                    f"Val Acc: {val_acc:.4f}"
                )

            else:
                print(
                    f"Epoch {epoch+1}/{EPOCHS} | "
                    f"Train Loss: {train_loss:.4f} | "
                    f"Train Acc: {train_acc:.4f}"
                )

            self.save()

    def predict(self, X):
        out = []
        for i in range(0, len(X), BATCH_SIZE):
            xb = X[i:i+BATCH_SIZE]
            _, probs = self.forward(xb)
            out.append(probs)

        return np.concatenate(out, axis=0)

    def save(self):
        np.savez(MODEL_FILE, **self.params)


def load_and_split():
    data = np.loadtxt("train.csv", delimiter=",", skiprows=1)
    X = data[:, 1:].astype(np.float32) / 255.0
    y = data[:, 0].astype(np.uint8)

    if X.shape[1] != 784:
        X = X.T

    n = len(y)
    rng = np.random.default_rng()

    test_and_val_size = 0.1

    test_idx = rng.choice(n, int(n * test_and_val_size), replace=False)

    mask = np.zeros(n, dtype=bool)
    mask[test_idx] = True

    remaining = np.where(~mask)[0]
    val_idx = rng.choice(remaining, int(n * test_and_val_size), replace=False)

    mask[val_idx] = True
    train_idx = np.where(~mask)[0]

    return X, y, train_idx, val_idx, test_idx


if __name__ == "__main__":

    X, y, train_idx, val_idx, test_idx = load_and_split()

    model = ANN(layer_sizes=HIDDEN_LAYERS)
    model.train(
        X[train_idx],
        y[train_idx],
        X[val_idx],
        y[val_idx]
    )

    preds = model.predict(X[test_idx])
    preds = np.argmax(preds, axis=1)

    print(classification_report(y[test_idx], preds))

    cm = confusion_matrix(y[test_idx], preds)

    plt.imshow(cm, cmap="Blues")
    plt.colorbar()

    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, str(cm[i, j]),
                     ha="center", va="center",
                     color="white" if i == j else "black",
                     fontsize=8)

    plt.show()