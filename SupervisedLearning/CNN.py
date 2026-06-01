pip install tensorflow

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load the MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

len(x_train)
#print(x_train)

x_train.shape

import matplotlib.pyplot as plt
#print(x_train[2])
plt.matshow(x_train[59999])

len(x_test)

model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the input
    layers.Dense(128, activation='relu'),   # Hidden layer with ReLU activation
    layers.Dense(10, activation='softmax')   # Output layer with softmax for classification
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)

# Example: Print the first predicted class
#print(y_test)
#print(predicted_classes)
for i in range(0,len(y_test)):
  print(predicted_classes[i], y_test[i])

