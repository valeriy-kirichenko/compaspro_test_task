#!/usr/bin/env sh

python ./manage.py wait_for_db

python ./manage.py migrate
python ./manage.py collectstatic --noinput
python ./manage.py createsuperuser --noinput
gunicorn test_task.wsgi:application --bind 0:8000
