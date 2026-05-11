import webview
from ann2 import ANN, MODEL_FILE, HIDDEN_LAYERS
from image_processing import preprocess_canvas_image
import numpy as np
import cv2
class Api:
    def __init__(self):
        self.ann = ANN(layer_sizes=HIDDEN_LAYERS, model_file=MODEL_FILE)

    def predict(self, image_data):
        processed = preprocess_canvas_image(image_data)
        cv2.imshow("Processed Image", processed.reshape(28, 28))
        cv2.waitKey(0)
        probs = self.ann.predict(processed)[0]
        print("Predicted probabilities:", probs)
        predicted_label = int(np.argmax(probs))

        return {"label": predicted_label, "confidence" : float(probs[predicted_label])}
def start_gui():
    webview.create_window('TTNT Project', 'index.html', js_api=Api(), width=1100, height=850)
    webview.start()
    
if __name__ == '__main__':
    start_gui()