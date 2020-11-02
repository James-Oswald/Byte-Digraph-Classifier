
import tensorflow as tf
from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255
x_train = np.expand_dims(x_train, -1)
x_train = np.expand_dims(x_train, 1)
print(x_train.shape)

#print(np.matrix(x_train[0, :, :]))
#print(y_train[0])

model = keras.models.load_model("Models/MNIST")
print(model(x_train[0, :, :, :, :]))
#model.summary()