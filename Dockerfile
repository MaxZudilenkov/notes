FROM alpine:3.14
FROM python:3.8.3-alpine
RUN mkdir /code
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN apk update \
    && apk add -u gcc musl-dev&& apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
ADD . /code/
