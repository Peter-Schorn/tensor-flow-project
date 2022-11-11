from flask import Flask
from flask import request
import random
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def index():
    return "success"

@app.route("/categorize", methods=["POST"])
def categorize():
    # the data for the request body
    data = request.data
    return "calculating"
