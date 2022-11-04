from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "success"

@app.route("/categorize")
def hello_world():
    categories = ["dog", "cat", "cow"]
    category = random.choice(categories)
    return f"<h1>{category}</h1>"

