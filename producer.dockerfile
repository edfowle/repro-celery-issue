FROM python:3.7-stretch

WORKDIR /opt/test

COPY / .

RUN pip install -r producer/requirements.txt
