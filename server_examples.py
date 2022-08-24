import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def handle_file_upload():
    try:
        photo = request.files['images']
    except FileNotFoundError:
        return 'failed to upload image'
    else:
        photo.save(os.path.join('.', photo.filename))
        print("image saved")

    class KNN:
        def __init__(self):
            self.number = "Its a one"

        def find_number(self):
            pass

    knn_clf = KNN()

    return knn_clf.number


@app.route("/choose_picture", methods=['GET'])
def choose_mnist_picture():
    return 'static/Dog.jpg'


if __name__ == '__main__':
    app.run(debug=True)
