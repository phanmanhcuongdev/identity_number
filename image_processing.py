import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

def preprocess_canvas_image(image_data):
    if "," in image_data:
        image_data = image_data.split(",", 1)[1]

    image_bytes = base64.b64decode(image_data)
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    
    kernel = np.ones((2, 2), np.uint8) 
    thresh = cv2.dilate(thresh, kernel, iterations=1)
    
    # Tìm vùng chứa chữ số
    coords = cv2.findNonZero(thresh)
    if coords is None: return np.zeros((784, 1))
    x, y, w, h = cv2.boundingRect(coords)
    
    # Thêm padding 10%
    pad = int(max(w, h) * 0.1)
    digit_roi = cv2.copyMakeBorder(thresh[y:y+h, x:x+w], pad, pad, pad, pad, 
                                   cv2.BORDER_CONSTANT, value=0)
    
    # 4. Resize về 20x20 rồi đặt vào giữa 28x28  theo chuẩn MNIST
    h_roi, w_roi = digit_roi.shape
    ratio = 20.0 / max(h_roi, w_roi)
    new_size = (int(w_roi * ratio), int(h_roi * ratio))
    # Tránh trường hợp size quá nhỏ
    if new_size[0] <= 0 or new_size[1] <= 0: return np.zeros((784, 1))
    
    digit_res = cv2.resize(digit_roi, new_size)
    
    final_img = np.zeros((28, 28), dtype=np.uint8)
    y_off = (28 - new_size[1]) // 2
    x_off = (28 - new_size[0]) // 2
    final_img[y_off:y_off+new_size[1], x_off:x_off+new_size[0]] = digit_res
    
    # Làm mờ nhẹ để khử răng cưa
    final_img = cv2.GaussianBlur(final_img, (3, 3), 0)

    return (final_img / 255.0).reshape(1, 784)
