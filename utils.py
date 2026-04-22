import cv2
import numpy as np

def preprocess_image(path, size=(128,128)):
    img = cv2.imread(path)
    img = cv2.resize(img, size)
    img = img / 255.0
    return img

def load_data(folder):
    # customize based on your dataset
    pass
