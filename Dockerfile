FROM python:3.10.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN #mkdir /django
#WORKDIR /django

WORKDIR /usr/src/app
COPY requirements.txt .

RUN apt-get update && apt-get -y install postgresql libpq-dev postgresql-client postgresql-client-common python3-pip git netcat
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY ./restaurant_saas .

RUN python3 manage.py collectstatic --no-input