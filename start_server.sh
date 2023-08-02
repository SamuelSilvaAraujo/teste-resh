#!/bin/bash

# Django
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python3 manage.py createsuperuser --no-input)
fi

if [ -n "$DEPLOY" ]
then
    # Gunicorn
    (gunicorn advocacy.wsgi:application --bind 0.0.0.0:8000)
else
    # Server
    (python3 manage.py runserver 0.0.0.0:8000)
fi