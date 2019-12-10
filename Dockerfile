FROM python:3.7

WORKDIR /home/kriti/Documents/project-3

RUN pip install torchvision

RUN pip install flask

RUN pip install requests

RUN pip install urllib3

COPY . .

CMD python server.py
