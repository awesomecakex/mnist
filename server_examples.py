import os
from flask import Flask, request
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from numpy import asarray
from knnserver import Knn
import cv2

app = Flask(__name__)

# Init the mnist library
mnist = load_digits()
X = mnist.data
y = mnist.target


@app.route("/")
def home():
    return 'This is home page'


@app.route("/upload", methods=['POST'])
def handle_file_upload():
    if 'image' in request.files:
        # In case a file was sent
        photo = request.files['image']
        # If the file is valid
        if photo.filename != '':
            # Save the file to folder
            photo.save(os.path.join('.', photo.filename))
            # Read the file to grayscale picture
            picture = cv2.imread('model.png', 0)
            # Convert the picture to numpy array
            np_picture = asarray(picture)
            # Reshape in favor of the knn predictore
            photo_np = np_picture.reshape(64)
            # init the knn class
            knn_cls = Knn(k=3)
            knn_cls.fit()
            # make a prediction
            prediction = knn_cls.predict(photo_np)
            return str(prediction)
    else:
        # No image was sent or bad connection issue
        return "Fail"


if __name__ == '__main__':
    app.run()
