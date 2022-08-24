import requests as req

url_to_upload = "http://127.0.0.1:5000/upload"
url_random_picture = "http://127.0.0.1:5000/choose_picture"

picture = req.get(url_random_picture)


with open(picture.text, 'rb') as f:
    files = {'images': f}
    r = req.post(url_to_upload, files=files)
    print(r.text)
