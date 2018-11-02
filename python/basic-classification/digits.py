#docker run -it --rm -v $PWD:/workspace -w /workspace tensorflow/tensorflow:latest-py3 python ./python/basic-classification/digits.py

import tensorflow as tf
import sys

print(tf.VERSION)

mnist = tf.keras.datasets.mnist

# MNIST handwritten digits dataset.
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

sys.exit()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.summary()

model.evaluate(x_test, y_test)
