#!/bin/sh

python3 manage.py migrate
python3 create_public_tenant.py
gunicorn restaurant_saas.wsgi:application --bind 0.0.0.0:8000