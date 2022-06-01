FROM --platform=linux/amd64 python:3.10-slim

WORKDIR app/

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY todolist /app

COPY ToDoList/todovenv/lib/python3.8/site-packages/django/contrib/admin/static .
