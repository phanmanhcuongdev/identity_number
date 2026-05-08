# Sử dụng Python 3.13-slim làm nền tảng
FROM python:3.13-slim

# Thiết lập biến môi trường để tối ưu Python trong Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các thư viện hệ thống cần thiết cho OpenCV và xử lý ảnh
# Đã thay libgl1-mesa-glx bằng libgl1 chuẩn hơn cho bản slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy và cài đặt thư viện Python trước để tận dụng cache của Docker
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn và trọng số mô hình vào container
COPY . .

# Mở cổng 5000 cho Flask
EXPOSE 5000

# Lệnh khởi chạy ứng dụng
CMD ["python", "app.py"]