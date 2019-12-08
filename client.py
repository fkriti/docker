import requests
import urllib
url = "https://images.unsplash.com/photo-1499084732479-de2c02d45fcc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80"
filename = "testing.jpg"
try: urllib.URLopener().retrieve(url, filename)
except: urllib.request.urlretrieve(url, filename)
resp = requests.post("http://127.0.0.1:5000/predict",files={"file": open(filename,'rb')})
print(resp.json()['class_name'])