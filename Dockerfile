FROM python:3.10.10-slim-buster
#SHELL ["bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV DEBUG 0

RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/

RUN apt-get update && apt-get -y install postgresql libpq-dev postgresql-client postgresql-client-common python3-pip git netcat
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN adduser -D nonroot
#USER nonroot
EXPOSE 8000

WORKDIR ./restaurant_saas

CMD gunicorn restaurant_saas.wsgi:application --bind 0.0.0.0:8000


