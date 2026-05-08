# Handwritten Digit Recognition with Deep ANN

## Giới thiệu

Dự án xây dựng hệ thống nhận diện chữ số viết tay dựa trên mạng nơ-ron nhân tạo Fully Connected, huấn luyện trên Infinity Dataset gồm 10,000,000 mẫu ở định dạng `.npy`. Phần lõi inference được cài đặt bằng `NumPy`, không phụ thuộc framework deep learning cấp cao.

Dataset đã sinh sẵn được lưu trên Google Drive:

```text
https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link
```

Project gồm ba phần chính:

- Mô hình Deep ANN để phân loại chữ số `0` đến `9`.
- Flask Web App cho phép vẽ chữ số trên canvas và dự đoán trực tiếp.
- Script tạo Infinity Dataset từ EMNIST digits bằng augmentation.
- Script sinh tài sản báo cáo: loss curve, accuracy curve, confusion matrix, mẫu dự đoán sai và sơ đồ preprocessing.

## Model Architecture

Kiến trúc mô hình:

```text
784 -> 1024 -> 512 -> 256 -> 10
```

Trong đó:

- `784`: vector ảnh đầu vào `28 x 28`.
- `1024`, `512`, `256`: ba tầng ẩn dùng ReLU.
- `10`: tầng đầu ra dùng Softmax cho 10 lớp chữ số.

File trọng số cuối cùng được đặt tại:

```text
weights/model_infinity.npz
```

## Cấu trúc thư mục

```text
.
├── ann.py                         # Forward propagation và load model
├── app.py                         # Flask backend cho Web Demo
├── templates/
│   └── index.html                 # Giao diện vẽ chữ số
├── scripts/
│   ├── generate_infinity.py       # Tạo data/train_infinity.npy và data/labels_infinity.npy
│   ├── generate_report_assets.py  # Sinh ảnh báo cáo
│   └── train_infinity.py          # Script huấn luyện Deep ANN
├── weights/
│   └── model_infinity.npz         # Model cuối cùng
├── data/
│   ├── train_infinity.npy         # Dataset lớn, không commit Git
│   └── labels_infinity.npy        # Label dataset, không commit Git
├── images/
│   └── preprocessing_pipeline.png # Ảnh sinh tự động cho báo cáo
├── report.md
├── requirements.txt
└── README.md
```

Các file dữ liệu lớn và checkpoint trung gian đã được đưa vào `.gitignore`. Model cuối cùng, log huấn luyện và ảnh báo cáo đã được đưa vào repo để phục vụ đọc báo cáo.

## Cài đặt

Tạo môi trường ảo:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Cài dependencies:

```powershell
pip install -r requirements.txt
```

## Chạy Flask Web App

Đảm bảo file model tồn tại:

```text
weights/model_infinity.npz
```

Chạy app:

```powershell
.\.venv\Scripts\python.exe app.py
```

Mở trình duyệt:

```text
http://127.0.0.1:5000
```

Pipeline preprocessing trong Flask giữ ảnh vẽ gần định dạng MNIST: decode canvas, grayscale, invert, threshold, crop bounding box, căn giữa, resize `28 x 28`, normalize và flatten thành vector `784 x 1`.

## Sinh ảnh báo cáo

Đảm bảo có các file local sau:

```text
train.log
weights/model_infinity.npz
data/train_infinity.npy
data/labels_infinity.npy
```

Nếu chưa có hai file `.npy`, tải từ Google Drive dataset ở phần giới thiệu hoặc tự tạo bằng `scripts/generate_infinity.py`.

Chạy:

```powershell
.\.venv\Scripts\python.exe .\scripts\generate_report_assets.py
```

Script sẽ sinh:

```text
loss_curve.png
accuracy_curve.png
confusion_matrix.png
misclassified_samples.png
images/preprocessing_pipeline.png
```

## Tạo Infinity Dataset

Script tạo dataset nằm tại:

```text
scripts/generate_infinity.py
```

Dataset đã tạo sẵn có thể tải tại:

```text
https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link
```

Script sử dụng EMNIST digits làm dữ liệu gốc, sau đó sinh thêm mẫu bằng rotation, scaling, elastic distortion và Gaussian noise. Output mặc định:

```text
data/train_infinity.npy
data/labels_infinity.npy
```

Chạy từ thư mục gốc project:

```powershell
.\.venv\Scripts\python.exe .\scripts\generate_infinity.py
```

Lưu ý: cấu hình mặc định tạo `10,000,000` mẫu và dùng `30` process, nên cần đủ CPU, RAM và dung lượng đĩa.

## Training

Script huấn luyện nằm tại:

```text
scripts/train_infinity.py
```

Ví dụ chạy từ thư mục gốc project:

```powershell
.\.venv\Scripts\python.exe .\scripts\train_infinity.py `
  --epochs 20 `
  --batch-size 4096 `
  --threads 30
```

Script sử dụng kiến trúc `784 -> 1024 -> 512 -> 256 -> 10` và optimizer Adam.

## Kết quả

Theo log huấn luyện 20 epoch, cấu hình Infinity đạt xấp xỉ:

```text
Training Accuracy:   99.44%
Validation Accuracy: 98.82% - 98.84%
```

Con số `99.44%` là accuracy trên training batch cuối của epoch 20. Validation accuracy cuối nằm quanh `98.8%`.

## Git Policy

Không commit các file sau:

- Dataset lớn: `data/*.npy`, `*.csv`
- Checkpoint trung gian: `checkpoints_infinity/`, `*.npz` ngoài model cuối
- Môi trường ảo/cache: `.venv/`, `__pycache__/`

Các thư mục `data/`, `weights/`, `images/` được giữ lại bằng `.gitkeep` để repo có cấu trúc rõ ràng. Riêng `weights/model_infinity.npz`, `train.log` và ảnh báo cáo được track để người đọc repo có đủ ngữ cảnh thực nghiệm.
