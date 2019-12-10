## Build docker image
* ``sudo docker build -t assignment3``

## Spins docker container
* ``sudo docker run -it -p 5000:5000 assignment3``

## To run project using command line

* Server supports GET requests

* ``curl http://127.0.0.1:5000/predict?url="<URL>"``

## Example commands:
* ``curl http://127.0.0.1:5000/predict?url="https://github.com/pytorch/hub/raw/master/dog.jpg"``

* ``curl http://127.0.0.1:5000/predict?url="https://images.unsplash.com/photo-1499084732479-de2c02d45fcc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80"``
