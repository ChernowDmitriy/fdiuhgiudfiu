FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/core

COPY ./requirements.txt/ usr/src/core/requirements.txt

RUN pip install -r usr/src/core/requirements.txt

COPY . /usr/src/core

EXPOSE 8000