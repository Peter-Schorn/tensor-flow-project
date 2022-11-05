from flask import Flask
from flask import request
import random


app = Flask(__name__)

@app.route("/")
def index():
    return "success"

@app.route("/categorize", methods=["POST"])
def categorize():
    # categories = ["dog", "cat", "cow"]
    # category = random.choice(categories)
    # return f"<h1>{category}</h1>"
    if request.method != "POST":
        print(f"error: unexpected method: {request.method}")
        return

    f = request.files[request.files.keys(0)]
    print(f)



import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
