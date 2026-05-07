import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

data = pd.read_csv('train.csv')

data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:4000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

data_train = data[4000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape

test_data = pd.read_csv('test.csv')
test_data = np.array(test_data)
np.random.shuffle(test_data)
test_data = test_data[0:10000].T
X_test = test_data / 255.

def init_params():
    # Khởi tạo He Initialization chuẩn cho ReLU
    W1 = np.random.randn(128, 784) * np.sqrt(2.0 / 784)
    b1 = np.zeros((128, 1))
    W2 = np.random.randn(10, 128) * np.sqrt(2.0 / 128)
    b2 = np.zeros((10, 1))
    return W1, b1, W2, b2

def softmax(Z):
    # Softmax ổn định số học (tránh tràn số overflow)
    Z_shifted = Z - np.max(Z, axis=0, keepdims=True)
    A = np.exp(Z_shifted) / np.sum(np.exp(Z_shifted), axis=0, keepdims=True)
    return A

def ReLU(Z):
    return np.maximum(Z, 0)

def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def ReLU_deriv(Z):
    return Z > 0

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def compute_loss(A2, Y):
    m = Y.size
    one_hot_Y = one_hot(Y)
    
    # tránh log(0)
    epsilon = 1e-8
    loss = -np.sum(one_hot_Y * np.log(A2 + epsilon)) / m
    
    return loss

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    m = X.shape[1]
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size


def get_learning_rate(iteration):
    if iteration < 400:
        return 0.5
    if iteration < 800:
        return 0.2
    return 0.05


def gradient_descent(X, Y, iterations=1200):
    W1, b1, W2, b2 = init_params()

    # Tạo dictionary để lưu lịch sử
    history = {'train_loss': [], 'dev_loss': [], 'train_acc': [], 'dev_acc': [], 'iter': [], 'alpha': []}

    for i in range(iterations):
        alpha = get_learning_rate(i)
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)

        if i % 10 == 0:
            predictions = get_predictions(A2)
            train_loss = compute_loss(A2, Y)
            train_acc = get_accuracy(predictions, Y)

            _, _, _, A2_dev = forward_prop(W1, b1, W2, b2, X_dev)
            dev_pred = get_predictions(A2_dev)
            dev_loss = compute_loss(A2_dev, Y_dev)
            dev_acc = get_accuracy(dev_pred, Y_dev)

            print(
                f"Iter: {i} | Alpha: {alpha:.4f} | Train Loss: {train_loss:.4f} | Dev Loss: {dev_loss:.4f} | Train Acc: {train_acc:.4f} | Dev Acc: {dev_acc:.4f}")

            # Lưu vào mảng
            history['iter'].append(i)
            history['alpha'].append(alpha)
            history['train_loss'].append(train_loss)
            history['dev_loss'].append(dev_loss)
            history['train_acc'].append(train_acc)
            history['dev_acc'].append(dev_acc)

    return W1, b1, W2, b2, history

def save_model(W1, b1, W2, b2, filename="model_weights.npz"):
    np.savez(filename, W1=W1, b1=b1, W2=W2, b2=b2)

def load_model(filename="model_weights.npz"):
    data = np.load(filename)
    return data["W1"], data["b1"], data["W2"], data["b2"]


def plot_and_save_metrics(history):
    # 1. Vẽ Loss Curve
    plt.figure(figsize=(8, 5))
    plt.plot(history['iter'], history['train_loss'], label='Train Loss', color='blue')
    plt.plot(history['iter'], history['dev_loss'], label='Dev Loss', color='red')
    plt.title('Train and Dev Loss over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Cross-Entropy Loss')
    plt.legend()
    plt.savefig('loss_curve.png')  # LƯU ẢNH LOSS ĐỂ CHO VÀO BÁO CÁO
    plt.close()

    # 2. Vẽ Accuracy Curve
    plt.figure(figsize=(8, 5))
    plt.plot(history['iter'], history['train_acc'], label='Train Accuracy', color='blue')
    plt.plot(history['iter'], history['dev_acc'], label='Dev Accuracy', color='red')
    plt.title('Train and Dev Accuracy over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('accuracy_curve.png')  # LƯU ẢNH ACC ĐỂ CHO VÀO BÁO CÁO
    plt.close()


def generate_confusion_matrix_and_errors(W1, b1, W2, b2):
    # Dự đoán trên tập Dev
    _, _, _, A2_dev = forward_prop(W1, b1, W2, b2, X_dev)
    dev_pred = get_predictions(A2_dev)

    # 3. Vẽ Confusion Matrix
    cm = confusion_matrix(Y_dev, dev_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix on Dev Set')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.savefig('confusion_matrix.png')  # LƯU ẢNH MATRIX ĐỂ CHO VÀO BÁO CÁO
    plt.close()

    # 4. Tìm và xuất ảnh dự đoán sai (Misclassified)
    incorrect_indices = np.where(dev_pred != Y_dev)[0]
    plt.figure(figsize=(10, 5))
    for i, idx in enumerate(incorrect_indices[:10]):  # Lấy 10 ảnh sai đầu tiên
        plt.subplot(2, 5, i + 1)
        img = X_dev[:, idx].reshape(28, 28) * 255
        plt.imshow(img, cmap='gray')
        plt.title(f"T:{Y_dev[idx]} P:{dev_pred[idx]}")  # T: Thật, P: Dự đoán
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('misclassified_samples.png')  # LƯU ẢNH LỖI ĐỂ CHO VÀO BÁO CÁO
    plt.close()
    print("Đã lưu thành công toàn bộ ảnh báo cáo!")


# --- THỰC THI CHÍNH ---
if __name__ == "__main__":
    if os.path.exists("model_weights.npz"):
        os.remove("model_weights.npz")
        print("Removed old model_weights.npz. Training a fresh model on train.csv...")

    print("Training model...")
    W1, b1, W2, b2, history = gradient_descent(X_train, Y_train, iterations=1200)
    save_model(W1, b1, W2, b2)
    # Gen ảnh biểu đồ
    plot_and_save_metrics(history)
    # Gen ma trận và ảnh sai
    generate_confusion_matrix_and_errors(W1, b1, W2, b2)

