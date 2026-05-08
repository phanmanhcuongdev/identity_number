import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from sklearn.metrics import classification_report, confusion_matrix, f1_score, precision_score, recall_score

from ann import forward_prop, load_model


LOG_PATH = ROOT_DIR / "train.log"
FALLBACK_LOG_PATH = ROOT_DIR / "train_full.log"
MODEL_PATH = ROOT_DIR / "weights" / "model_infinity.npz"
X_PATH = ROOT_DIR / "data" / "train_infinity.npy"
Y_PATH = ROOT_DIR / "data" / "labels_infinity.npy"
OUTPUT_DIR = ROOT_DIR
EVAL_SAMPLES = 10_000
DPI = 300


def display_path(path):
    path = Path(path)
    try:
        return str(path.relative_to(ROOT_DIR))
    except ValueError:
        return path.name


def _extract_metrics_from_text(text):
    batch_pattern = re.compile(
        r"Epoch\s+(\d+)/(\d+)\s+\|\s+Batch\s+(\d+)/(\d+)\s+\|\s+LR\s+"
        r"([0-9.eE+-]+)\s+\|\s+Loss\s+([0-9.]+)\s+\|\s+Acc\s+([0-9.]+)"
    )
    val_pattern = re.compile(
        r"Epoch\s+(\d+)\s+done\s+in\s+[0-9.]+\s+min\s+\|\s+Val Loss\s+"
        r"([0-9.]+)\s+\|\s+Val Acc\s+([0-9.]+)"
    )

    train_by_epoch = {}
    val_by_epoch = {}

    max_epoch = None

    for line in text.splitlines():
        batch_match = batch_pattern.search(line)
        if batch_match:
            epoch = int(batch_match.group(1))
            max_epoch = int(batch_match.group(2))
            batch_no = int(batch_match.group(3))
            total_batches = int(batch_match.group(4))
            loss = float(batch_match.group(6))
            acc = float(batch_match.group(7))

            # Keep the final batch summary as the epoch-level training metric.
            if batch_no == total_batches:
                train_by_epoch[epoch] = (loss, acc)
            continue

        val_match = val_pattern.search(line)
        if val_match:
            epoch = int(val_match.group(1))
            val_loss = float(val_match.group(2))
            val_acc = float(val_match.group(3))
            val_by_epoch[epoch] = (val_loss, val_acc)

    return train_by_epoch, val_by_epoch, max_epoch


def parse_training_log(log_path=LOG_PATH, fallback_log_path=FALLBACK_LOG_PATH):
    if not log_path.exists():
        raise FileNotFoundError(f"Missing log file: {log_path}")

    train_by_epoch, val_by_epoch, max_epoch = _extract_metrics_from_text(
        log_path.read_text(encoding="utf-8", errors="ignore")
    )
    val_source_by_epoch = {epoch: str(log_path) for epoch in val_by_epoch}

    missing_val_epochs = sorted(set(train_by_epoch) - set(val_by_epoch))
    if missing_val_epochs and fallback_log_path.exists():
        fallback_train, fallback_val, fallback_max_epoch = _extract_metrics_from_text(
            fallback_log_path.read_text(encoding="utf-8", errors="ignore")
        )
        train_by_epoch.update({k: v for k, v in fallback_train.items() if k not in train_by_epoch})
        for epoch, value in fallback_val.items():
            if epoch not in val_by_epoch:
                val_by_epoch[epoch] = value
                val_source_by_epoch[epoch] = str(fallback_log_path)
        max_epoch = max_epoch or fallback_max_epoch

    epochs = sorted(set(train_by_epoch) & set(val_by_epoch))
    if not epochs:
        raise ValueError(f"No complete epoch metrics found in {log_path}")

    if max_epoch is not None and len(epochs) < max_epoch:
        missing = sorted(set(range(1, max_epoch + 1)) - set(epochs))
        print(f"Warning: missing complete metrics for epochs: {missing}")

    return {
        "epochs": np.array(epochs),
        "train_loss": np.array([train_by_epoch[e][0] for e in epochs]),
        "train_acc": np.array([train_by_epoch[e][1] for e in epochs]),
        "val_loss": np.array([val_by_epoch[e][0] for e in epochs]),
        "val_acc": np.array([val_by_epoch[e][1] for e in epochs]),
        "val_sources": [val_source_by_epoch[e] for e in epochs],
    }


def save_loss_curve(metrics, output_path=OUTPUT_DIR / "loss_curve.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(metrics["epochs"], metrics["train_loss"], marker="o", label="Training Loss")
    plt.plot(metrics["epochs"], metrics["val_loss"], marker="s", label="Validation Loss")
    plt.title("Training and Validation Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.xticks(metrics["epochs"])
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI)
    plt.close()


def save_accuracy_curve(metrics, output_path=OUTPUT_DIR / "accuracy_curve.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(metrics["epochs"], metrics["train_acc"], marker="o", label="Training Accuracy")
    plt.plot(metrics["epochs"], metrics["val_acc"], marker="s", label="Validation Accuracy")
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.xticks(metrics["epochs"])
    plt.ylim(0.94, 1.0)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI)
    plt.close()


def load_eval_data(x_path=X_PATH, y_path=Y_PATH, sample_count=EVAL_SAMPLES):
    if not x_path.exists():
        raise FileNotFoundError(
            f"Missing dataset file: {x_path}. "
            "train_infinity.py is the training script, not the NumPy dataset. "
            "Place train_infinity.npy in data/ or change X_PATH in generate_report_assets.py."
        )
    if not y_path.exists():
        raise FileNotFoundError(
            f"Missing label file: {y_path}. "
            "Place labels_infinity.npy in data/ or change Y_PATH in generate_report_assets.py."
        )

    X = np.load(x_path, mmap_mode="r")
    y = np.load(y_path, mmap_mode="r")

    if X.ndim != 2:
        raise ValueError(f"X must be 2D, got shape {X.shape}")

    if X.shape[1] == 784:
        X_eval = np.asarray(X[-sample_count:], dtype=np.float32)
    elif X.shape[0] == 784:
        X_eval = np.asarray(X[:, -sample_count:].T, dtype=np.float32)
    else:
        raise ValueError(f"X must contain 784 features, got shape {X.shape}")

    y_eval = np.asarray(y[-X_eval.shape[0] :], dtype=np.int64).reshape(-1)
    if X_eval.max() > 1.5:
        X_eval /= np.float32(255.0)

    return X_eval, y_eval


def predict_labels(model_params, X_eval, batch_size=512):
    predictions = []
    probabilities = []

    for start in range(0, X_eval.shape[0], batch_size):
        batch = X_eval[start : start + batch_size].T
        *_, A4 = forward_prop(*model_params, batch)
        batch_probs = A4.T
        predictions.append(np.argmax(batch_probs, axis=1))
        probabilities.append(batch_probs)

    return np.concatenate(predictions), np.vstack(probabilities)


def save_confusion_matrix(y_true, y_pred, output_path=OUTPUT_DIR / "confusion_matrix.png"):
    cm = confusion_matrix(y_true, y_pred, labels=np.arange(10))

    plt.figure(figsize=(9, 7))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=np.arange(10),
        yticklabels=np.arange(10),
        cbar=True,
    )
    plt.title("Confusion Matrix on 10,000 Evaluation Samples")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI)
    plt.close()


def save_evaluation_metrics(y_true, y_pred, output_path=OUTPUT_DIR / "evaluation_metrics.txt"):
    accuracy = float(np.mean(y_true == y_pred))
    macro_precision = precision_score(y_true, y_pred, average="macro", zero_division=0)
    macro_recall = recall_score(y_true, y_pred, average="macro", zero_division=0)
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    report = classification_report(
        y_true,
        y_pred,
        labels=np.arange(10),
        digits=4,
        zero_division=0,
    )

    output_path.write_text(
        "\n".join(
            [
                "Evaluation Metrics on 10,000 Samples",
                "=" * 35,
                f"Accuracy:        {accuracy:.6f}",
                f"Macro Precision: {macro_precision:.6f}",
                f"Macro Recall:    {macro_recall:.6f}",
                f"Macro F1-Score:  {macro_f1:.6f}",
                "",
                "Classification Report by Label",
                "-" * 35,
                report,
                "",
            ]
        ),
        encoding="utf-8",
    )


def save_misclassified_samples(X_eval, y_true, y_pred, output_path=OUTPUT_DIR / "misclassified_samples.png"):
    wrong_indices = np.where(y_true != y_pred)[0][:10]
    if wrong_indices.size == 0:
        raise ValueError("No misclassified samples found in the selected evaluation set.")

    fig, axes = plt.subplots(2, 5, figsize=(10, 4.5))
    for ax, idx in zip(axes.flat, wrong_indices):
        ax.imshow(X_eval[idx].reshape(28, 28), cmap="gray")
        ax.set_title(f"True: {y_true[idx]} | Pred: {y_pred[idx]}", fontsize=10)
        ax.axis("off")

    for ax in axes.flat[wrong_indices.size :]:
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI)
    plt.close(fig)


def save_preprocessing_pipeline(output_path=OUTPUT_DIR / "images" / "preprocessing_pipeline.png"):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    steps = [
        "Input Image",
        "Grayscale\nInvert",
        "Thresholding",
        "Bounding Box",
        "Centering",
        "Resize\n28x28",
        "Normalization",
    ]

    fig, ax = plt.subplots(figsize=(15, 3))
    ax.set_xlim(0, len(steps))
    ax.set_ylim(0, 1)
    ax.axis("off")

    box_width = 0.9
    box_height = 0.42
    y = 0.5 - box_height / 2

    for i, step in enumerate(steps):
        x = i + 0.05
        box = FancyBboxPatch(
            (x, y),
            box_width,
            box_height,
            boxstyle="round,pad=0.03,rounding_size=0.04",
            linewidth=1.4,
            edgecolor="#1f4e79",
            facecolor="#eaf3fb",
        )
        ax.add_patch(box)
        ax.text(
            x + box_width / 2,
            0.5,
            step,
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#17324d",
        )

        if i < len(steps) - 1:
            arrow = FancyArrowPatch(
                (x + box_width + 0.03, 0.5),
                (i + 1.02, 0.5),
                arrowstyle="-|>",
                mutation_scale=14,
                linewidth=1.4,
                color="#333333",
            )
            ax.add_patch(arrow)

    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI)
    plt.close(fig)


def main():
    sns.set_theme(style="whitegrid")

    metrics = parse_training_log(LOG_PATH)
    val_sources = sorted(set(display_path(source) for source in metrics["val_sources"]))
    print(f"Parsed {len(metrics['epochs'])} complete epochs.")
    print(f"Training metrics source: {display_path(LOG_PATH)}")
    print(f"Validation metrics source(s): {', '.join(val_sources)}")
    save_loss_curve(metrics)
    save_accuracy_curve(metrics)
    print("Saved loss_curve.png and accuracy_curve.png")

    save_preprocessing_pipeline()
    print("Saved images/preprocessing_pipeline.png")

    model_params = load_model(MODEL_PATH)
    X_eval, y_eval = load_eval_data()
    y_pred, _ = predict_labels(model_params, X_eval)
    save_evaluation_metrics(y_eval, y_pred)
    save_confusion_matrix(y_eval, y_pred)
    save_misclassified_samples(X_eval, y_eval, y_pred)
    print("Saved evaluation_metrics.txt, confusion_matrix.png and misclassified_samples.png")


if __name__ == "__main__":
    main()
