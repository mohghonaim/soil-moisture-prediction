from pathlib import Path

import tensorflow as tf
from tensorflow import keras
import numpy as np


BASE_DIR = Path(__file__).resolve(strict=True).parent

model = tf.keras.models.load_model(f"{BASE_DIR}/dnn_model2")


def predict_val(text):
    if text is not None:
        text = text.split('\t')
        pred = model.predict(np.array(text, dtype=np.float32))
        return pred
    else:
        return('empty')