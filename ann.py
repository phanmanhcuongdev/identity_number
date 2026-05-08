import numpy as np


def ReLU(Z):
    return np.maximum(Z, 0)


def softmax(Z):
    Z_shifted = Z - np.max(Z, axis=0, keepdims=True)
    A = np.exp(Z_shifted) / np.sum(np.exp(Z_shifted), axis=0, keepdims=True)
    return A


def forward_prop(W1, b1, W2, b2, W3, b3, W4, b4, X):
    # Layer 1: 1024 neurons
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)

    # Layer 2: 512 neurons
    Z2 = W2.dot(A1) + b2
    A2 = ReLU(Z2)

    # Layer 3: 256 neurons
    Z3 = W3.dot(A2) + b3
    A3 = ReLU(Z3)

    # Layer 4: 10 neurons (Output)
    Z4 = W4.dot(A3) + b4
    A4 = softmax(Z4)

    return Z1, A1, Z2, A2, Z3, A3, Z4, A4


def _as_column_bias(b):
    return np.asarray(b).reshape(-1, 1)


def _normalize_weight_shape(W, expected_shape, name):
    W = np.asarray(W)
    if W.shape == expected_shape:
        return W

    transposed_shape = (expected_shape[1], expected_shape[0])
    if W.shape == transposed_shape:
        return W.T

    raise ValueError(f"{name} has shape {W.shape}, expected {expected_shape}.")


def load_model(filename="model_infinity.npz"):
    data = np.load(filename)

    W1 = _normalize_weight_shape(data["W1"], (1024, 784), "W1")
    W2 = _normalize_weight_shape(data["W2"], (512, 1024), "W2")
    W3 = _normalize_weight_shape(data["W3"], (256, 512), "W3")
    W4 = _normalize_weight_shape(data["W4"], (10, 256), "W4")

    return (
        W1,
        _as_column_bias(data["b1"]),
        W2,
        _as_column_bias(data["b2"]),
        W3,
        _as_column_bias(data["b3"]),
        W4,
        _as_column_bias(data["b4"]),
    )


def get_predictions(A4):
    return np.argmax(A4, 0)
