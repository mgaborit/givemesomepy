# syntax=docker/dockerfile:1
FROM python:3.13-slim

WORKDIR /app

RUN pip install psycopg2-binary
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/main.py main.py
