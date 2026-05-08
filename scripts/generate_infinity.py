import numpy as np
import cv2
from scipy.ndimage import map_coordinates, gaussian_filter
from emnist import extract_training_samples
from multiprocessing import Pool
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

TOTAL_SAMPLES = 10_000_000
NUM_PROCESSES = 30
OUTPUT_FILE = DATA_DIR / "train_infinity.npy"
LABEL_FILE = DATA_DIR / "labels_infinity.npy"

def elastic_transform(image, alpha, sigma):
    """Apply elastic distortion to simulate handwriting variation."""
    random_state = np.random.RandomState(None)
    shape = image.shape
    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
    x, y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]), indexing='ij')
    indices = np.reshape(x + dx, (-1, 1)), np.reshape(y + dy, (-1, 1))
    return map_coordinates(image, indices, order=1).reshape(shape)

def augment_image(img):
    """Apply rotation, scaling, elastic distortion, and light noise."""
    angle = np.random.uniform(-25, 25)
    M = cv2.getRotationMatrix2D((14, 14), angle, np.random.uniform(0.8, 1.2))
    img = cv2.warpAffine(img, M, (28, 28))
    
    img = elastic_transform(img, alpha=36, sigma=4)
    
    noise = np.random.normal(0, 5, img.shape)
    img = np.clip(img + noise, 0, 255)
    
    return img.flatten().astype(np.uint8)

def process_chunk(chunk_data):
    return [augment_image(img.reshape(28, 28)) for img in chunk_data]

if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("--- Loading EMNIST digits seed dataset ---")
    images, labels = extract_training_samples('digits')
    
    print(f"--- Generating {TOTAL_SAMPLES:,} augmented samples on {NUM_PROCESSES} processes ---")
    chunk_size = TOTAL_SAMPLES // NUM_PROCESSES
    indices = np.random.choice(len(images), TOTAL_SAMPLES)
    
    with Pool(NUM_PROCESSES) as p:
        data_chunks = [images[indices[i:i + chunk_size]] for i in range(0, TOTAL_SAMPLES, chunk_size)]
        results = p.map(process_chunk, data_chunks)

    full_data = np.vstack(results)
    full_labels = labels[indices]

    print(f"--- Saving {TOTAL_SAMPLES:,} samples in NumPy binary format ---")
    np.save(OUTPUT_FILE, full_data)
    np.save(LABEL_FILE, full_labels)
    print(f"Done. Dataset saved to {OUTPUT_FILE} and {LABEL_FILE}.")
