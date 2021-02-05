import tensorflow as tf
from random import randint
from kivy.graphics.texture import Texture
import cv2
from tensorflow.keras.models import load_model
import numpy as np

mnist_dataset = tf.keras.datasets.mnist
(_, _), (x, y) = mnist_dataset.load_data()
x = x.reshape(x.shape[0], 28, 28, 1)
model = load_model('models/model1.h5')


def get_batch(n):
    out_x = []
    out_y = []
    for _ in range(n):
        i = randint(0, len(x) - 1)
        out_x.append(x[i])
        out_y.append(y[i])
    return out_x, out_y


def to_texture(img):
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB), 0)
    texture = Texture.create(size=(28, 28))
    texture.blit_buffer(img.tostring(), bufferfmt="ubyte", colorfmt="rgb")
    return texture


def predict(batch):
    batch = np.array(batch).reshape(len(batch), 28, 28, 1) / 255
    return np.argmax(model.predict([batch]), axis=1)


