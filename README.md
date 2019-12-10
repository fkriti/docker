#build docker image
sudo docker build -t assignment3 .  

#spins docker container
sudo docker run -it -p 5000:5000 assignment3

#to run project using command line
curl http://127.0.0.1:5000/predict?url=<url-string-in-double-quotes>

Example commands:
curl http://127.0.0.1:5000/predict?url="https://github.com/pytorch/hub/raw/master/dog.jpg"
curl http://127.0.0.1:5000/predict?url="https://images.unsplash.com/photo-1499084732479-de2c02d45fcc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80"
