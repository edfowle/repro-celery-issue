FROM python:3.7-stretch

WORKDIR /opt/test

COPY consumer/* .

RUN pip install -r requirements.txt