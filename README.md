# Handwritten Digit Recognition with Deep ANN

## Giới thiệu

Dự án xây dựng hệ thống nhận diện chữ số viết tay dựa trên mạng nơ-ron nhân tạo kết nối đầy đủ, huấn luyện trên Infinity Dataset gồm 10,000,000 mẫu ở định dạng `.npy`. Phần lõi suy luận được cài đặt bằng `NumPy`, không phụ thuộc framework deep learning cấp cao.

Dataset đã sinh sẵn được lưu trên Google Drive:

```text
https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link
```

Project gồm ba phần chính:

- Mô hình Deep ANN để phân loại chữ số `0` đến `9`.
- Flask Web App cho phép vẽ chữ số trên canvas và dự đoán trực tiếp.
- Script tạo Infinity Dataset từ EMNIST digits bằng augmentation.
- Script sinh tài sản báo cáo: loss curve, accuracy curve, ma trận nhầm lẫn, mẫu dự đoán sai, `evaluation_metrics.txt` và sơ đồ tiền xử lý.

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

Lưu ý: checkpoint lưu trọng số theo quy ước huấn luyện của `scripts/train_infinity.py`, ví dụ `W1=(784, 1024)`. Khi suy luận, `ann.py` tự chuẩn hóa shape về quy ước `W @ X + b`, ví dụ `W1=(1024, 784)`.

## Cấu trúc thư mục

```text
.
├── ann.py                         # Lan truyền tiến và load model
├── app.py                         # Flask backend cho Web Demo
├── templates/
│   └── index.html                 # Giao diện vẽ chữ số
├── static/
│   └── script.js                  # Logic canvas, touch drawing và gọi predict
├── scripts/
│   ├── generate_infinity.py       # Tạo data/train_infinity.npy và data/labels_infinity.npy
│   ├── generate_report_assets.py  # Sinh ảnh và metric báo cáo
│   └── train_infinity.py          # Script huấn luyện Deep ANN
├── weights/
│   └── model_infinity.npz         # Model cuối cùng
├── data/
│   ├── train_infinity.npy         # Dataset lớn, không commit Git
│   └── labels_infinity.npy        # Label dataset, không commit Git
├── images/
│   └── preprocessing_pipeline.png # Ảnh sinh tự động cho báo cáo
├── .github/
│   └── workflows/
│       └── docker-ci.yml          # CI build/push Docker image
├── Dockerfile
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

Khi chạy trong Docker hoặc truy cập từ thiết bị khác trong cùng mạng LAN, Flask lắng nghe trên `0.0.0.0:5000`.

Pipeline tiền xử lý trong Flask giữ ảnh vẽ gần định dạng MNIST: decode canvas, chuyển ảnh xám, đảo màu, threshold, crop bounding box, căn giữa, resize `28 x 28`, chuẩn hóa và trải phẳng thành vector `784 x 1`.

## Docker

Repo có sẵn `Dockerfile` dùng base image `python:3.13-slim`, cài các thư viện hệ thống cần thiết cho OpenCV và expose port `5000`.

Build image local:

```powershell
docker build -t identity_number:local .
```

Chạy container:

```powershell
docker run --rm -p 5000:5000 identity_number:local
```

Sau đó mở:

```text
http://127.0.0.1:5000
```

## GitHub Actions Docker CI

Workflow Docker nằm tại:

```text
.github/workflows/docker-ci.yml
```

Workflow chạy khi có push vào nhánh `main`, build image bằng Docker Buildx và push lên Docker Hub với hai tag:

```text
latest
<short-sha>
```

Cần cấu hình hai GitHub Secrets trong repository:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Image được push theo dạng:

```text
<DOCKERHUB_USERNAME>/identity_number:latest
<DOCKERHUB_USERNAME>/identity_number:<short-sha>
```

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
evaluation_metrics.txt
images/preprocessing_pipeline.png
```

`evaluation_metrics.txt` được tính trên 10,000 mẫu cuối của dataset bằng mô hình cuối cùng, gồm Accuracy, Macro Precision, Macro Recall, Macro F1-Score và classification report cho từng nhãn `0` đến `9`. Đây là bước đánh giá hậu huấn luyện, không can thiệp vào logic train.

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

Thông số mặc định chính:

```text
Epochs: 20
Batch size: 4096
Validation size: 100,000
Initial learning rate: 0.001
Learning rate decay: 0.92 per epoch
Weight decay: 1e-5
Adam beta1/beta2/epsilon: 0.9 / 0.999 / 1e-8
```

Tập validation được chọn bằng hoán vị ngẫu nhiên với seed cố định trong `scripts/train_infinity.py`, không phải bằng cách lấy tuần tự một đoạn cuối dataset.

## Kết quả

Theo log huấn luyện 20 epoch, cấu hình Infinity đạt xấp xỉ:

```text
Training Accuracy:   99.44%
Validation Accuracy: 98.82%
Validation Loss:     0.0393
```

Kết quả đánh giá bổ sung trên 10,000 mẫu cuối của dataset:

```text
Evaluation Accuracy:        99.57%
Macro Precision:            99.57%
Macro Recall:               99.57%
Macro F1-Score:             99.57%
```

Các số liệu chi tiết theo từng lớp nằm trong `evaluation_metrics.txt` và đã được tổng hợp vào `report.md`.

## Git Policy

Không commit các file sau:

- Dataset lớn: `data/*.npy`, `*.csv`
- Checkpoint trung gian: `checkpoints_infinity/`, `*.npz` ngoài model cuối
- Môi trường ảo/cache: `.venv/`, `__pycache__/`

Các thư mục `data/`, `weights/`, `images/` được giữ lại bằng `.gitkeep` để repo có cấu trúc rõ ràng. Riêng `weights/model_infinity.npz`, `train.log` và ảnh báo cáo được track để người đọc repo có đủ ngữ cảnh thực nghiệm.
