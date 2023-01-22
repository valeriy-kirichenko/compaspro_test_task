FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app
COPY run.sh /app
COPY . /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir
