import requests as req
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import cv2

# Init the mnist library
mnist = load_digits()
X = mnist.data
y = mnist.target

url_to_upload = "http://127.0.0.1:5000/upload"

# Getting the number from the user
choice = int(input("Enter number between 0-1797: "))
picture = mnist.images[choice]
print("You chose the following number")
plt.imshow(picture, cmap='gray')
plt.show()
# Saving picture to file
plt.imsave('images/model.png', picture)
# Sending picture to server
with open('images/model.png', 'rb') as f:
    files = {'image': f}
    r = req.post(url_to_upload, files=files)
    if r.status_code == 200 and r.status_code != 'Fail':
        print(f"The classify predict {r.text}")
    else:
        print("Something went very wrong!!!")
