FROM python:3.10

MAINTAINER Bipul Dawadi

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY ./*app/ /app/

USER user 