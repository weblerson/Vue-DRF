FROM python:3.10-slim
LABEL authors="weblerson"

ENV PYTHONUNBUFFERED=1

RUN apt update

RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/media

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000