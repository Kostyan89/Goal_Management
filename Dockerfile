FROM --platform=linux/amd64 python:3.10-slim

WORKDIR app/
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
CMD pyhton manage.py runserver 0.0.0.0:0000