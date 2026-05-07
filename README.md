# Nhận diện chữ số viết tay MNIST bằng ANN NumPy

## Giới thiệu

Dự án cài đặt mô hình mạng nơ-ron Fully Connected để nhận diện chữ số viết tay MNIST. Phần lõi AI được viết từ đầu bằng `NumPy`, không dùng framework học sâu cấp cao cho quá trình forward propagation, backward propagation và cập nhật tham số.

Mô hình sử dụng kiến trúc:

```text
784 -> 128 -> 10
```

Trong đó:

- `784` là số pixel của ảnh đầu vào kích thước `28 x 28`.
- `128` là số neuron của tầng ẩn.
- `10` là số lớp đầu ra, tương ứng các chữ số từ `0` đến `9`.

Ngoài phần huấn luyện bằng terminal, dự án có thêm Flask Web App để người dùng vẽ chữ số trực tiếp trên trình duyệt và nhận kết quả dự đoán.

## Cấu trúc chính

```text
ann.py                         # Mô hình ANN NumPy và pipeline huấn luyện
app.py                         # Flask backend cho Web Demo
templates/index.html           # Giao diện Canvas để vẽ chữ số
expand_mnist_dataset.py        # Script mở rộng dữ liệu MNIST bằng augmentation
train.csv                      # Dữ liệu huấn luyện dạng label + 784 pixel
test.csv                       # Dữ liệu test/demo
report.md                      # Báo cáo kỹ thuật
loss_curve.png                 # Biểu đồ loss
accuracy_curve.png             # Biểu đồ accuracy
confusion_matrix.png           # Confusion matrix
misclassified_samples.png      # Một số mẫu dự đoán sai
```

## Cài đặt môi trường

Tạo và kích hoạt môi trường ảo:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Cài các thư viện cần thiết:

```powershell
pip install numpy pandas matplotlib seaborn scikit-learn flask opencv-python pillow
```

Nếu muốn tải MNIST bằng TensorFlow trong script mở rộng dữ liệu, có thể cài thêm:

```powershell
pip install tensorflow
```

Nếu không có TensorFlow, `expand_mnist_dataset.py` sẽ fallback sang `sklearn.datasets.fetch_openml`.

## Huấn luyện mô hình

Chạy:

```powershell
.\.venv\Scripts\python.exe ann.py
```

Khi chạy trực tiếp, `ann.py` sẽ:

- Đọc dữ liệu từ `train.csv`.
- Shuffle dữ liệu.
- Chia `4000` mẫu đầu làm tập dev.
- Chuẩn hóa pixel về khoảng `[0, 1]`.
- Khởi tạo tham số bằng He Initialization.
- Huấn luyện mô hình bằng Batch Gradient Descent.
- Dùng Step Decay learning rate:
  - Iteration `< 400`: `alpha = 0.5`
  - `400 <= iteration < 800`: `alpha = 0.2`
  - `iteration >= 800`: `alpha = 0.05`
- Chạy `1200` iterations.
- Tự xóa `model_weights.npz` cũ trước khi train lại.
- Lưu model mới vào `model_weights.npz`.
- Xuất các ảnh báo cáo: loss curve, accuracy curve, confusion matrix và mẫu dự đoán sai.

Lưu ý: `model_weights.npz` được sinh tự động sau khi train và đã được đưa vào `.gitignore`.

## Chạy Web Demo

Sau khi đã có `model_weights.npz`, chạy Flask app:

```powershell
.\.venv\Scripts\python.exe app.py
```

Mở trình duyệt tại:

```text
http://127.0.0.1:5000
```

Web Demo cho phép:

- Vẽ chữ số trên canvas `300 x 300`.
- Xóa canvas bằng nút `Clear`.
- Gửi ảnh đến API `/predict` bằng `fetch`.
- Nhận kết quả dự đoán và confidence mà không reload trang.

Pipeline tiền xử lý ảnh Canvas gồm:

1. Giải mã ảnh base64.
2. Chuyển sang grayscale.
3. Invert màu để đưa về dạng nền đen chữ trắng giống MNIST.
4. Tìm bounding box của nét vẽ.
5. Crop sát chữ số.
6. Pad thành ảnh vuông và căn giữa.
7. Resize về `28 x 28`.
8. Normalize về `[0, 1]`.
9. Flatten thành vector `784 x 1`.
10. Dự đoán bằng `forward_prop` trong `ann.py`.

## Mở rộng dữ liệu

Script `expand_mnist_dataset.py` dùng để tạo bộ dữ liệu lớn hơn từ MNIST và augmentation:

```powershell
.\.venv\Scripts\python.exe expand_mnist_dataset.py
```

Script này có thể:

- Tải full MNIST `70,000` mẫu.
- Tạo nhiều biến thể bằng rotation, scaling, shifting, shear và Gaussian noise.
- Gộp với `train.csv` hiện có.
- Dùng `np.unique(axis=0)` để loại bỏ mẫu trùng.
- Shuffle dữ liệu.
- Xuất file dữ liệu mở rộng.

## Lưu ý về dữ liệu lớn

File `train.csv` mở rộng có thể rất lớn, lên tới hàng GB. Không nên commit file dữ liệu quá lớn trực tiếp lên GitHub vì có thể vượt giới hạn dung lượng file của GitHub.

Khuyến nghị:

- Giữ dữ liệu lớn ở local.
- Chỉ commit code, báo cáo và ảnh kết quả cần thiết.
- Nếu cần chia sẻ dữ liệu lớn, dùng Google Drive, Kaggle Dataset, Hugging Face Dataset hoặc Git LFS.

## Báo cáo

Báo cáo kỹ thuật nằm trong:

```text
report.md
```

Báo cáo trình bày:

- Cơ sở lý thuyết ANN.
- Tiền xử lý dữ liệu.
- Forward propagation.
- Stable Softmax.
- Cross-Entropy Loss.
- Backpropagation.
- Kết quả thực nghiệm.
- Confusion matrix.
- Phân tích mẫu sai.
- Web Demo và pipeline xử lý Wild Data.

## Ghi chú Git

Các file sinh tự động hoặc quá lớn không nên đưa vào Git:

- `model_weights.npz`
- Các file dataset mở rộng dung lượng lớn nếu vượt giới hạn GitHub.

`model_weights.npz` có thể được tạo lại bằng cách chạy:

```powershell
.\.venv\Scripts\python.exe ann.py
```
