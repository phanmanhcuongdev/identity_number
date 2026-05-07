import base64
from io import BytesIO

import cv2
import numpy as np
from flask import Flask, jsonify, render_template, request
from PIL import Image

from ann import forward_prop, load_model


app = Flask(__name__)

# Load trained weights once when the server starts.
W1, b1, W2, b2 = load_model("model_weights.npz")


def preprocess_canvas_image(image_data):
    """Convert a base64 canvas image into a normalized MNIST-like (784, 1) vector."""
    if "," in image_data:
        image_data = image_data.split(",", 1)[1]

    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes)).convert("RGBA")

    # Composite onto a white background so transparent canvas pixels are handled consistently.
    background = Image.new("RGBA", image.size, (255, 255, 255, 255))
    image = Image.alpha_composite(background, image).convert("L")

    gray = np.array(image)
    inverted = cv2.bitwise_not(gray)

    # Remove weak background noise and locate the drawn digit.
    _, binary = cv2.threshold(inverted, 20, 255, cv2.THRESH_BINARY)
    points = cv2.findNonZero(binary)
    if points is None:
        return None

    x, y, w, h = cv2.boundingRect(points)
    digit = inverted[y:y + h, x:x + w]

    # Pad into a square canvas, centered, with black background.
    side = max(w, h)
    margin = max(8, int(side * 0.25))
    square_size = side + 2 * margin
    square = np.zeros((square_size, square_size), dtype=np.uint8)

    x_offset = (square_size - w) // 2
    y_offset = (square_size - h) // 2
    square[y_offset:y_offset + h, x_offset:x_offset + w] = digit

    resized = cv2.resize(square, (28, 28), interpolation=cv2.INTER_AREA)
    normalized = resized.astype(np.float32) / 255.0
    return normalized.reshape(784, 1)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True) or {}
    image_data = payload.get("image")
    if not image_data:
        return jsonify({"error": "Missing image data"}), 400

    X = preprocess_canvas_image(image_data)
    if X is None:
        return jsonify({"error": "No digit detected"}), 400

    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    probabilities = A2[:, 0]
    prediction = int(np.argmax(probabilities))
    confidence = float(probabilities[prediction])

    return jsonify({
        "prediction": prediction,
        "confidence": confidence,
        "probabilities": probabilities.astype(float).tolist(),
    })


if __name__ == "__main__":
    app.run(debug=True)
