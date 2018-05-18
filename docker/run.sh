#!/bin/bash

./waitforit.sh db 5432
python manage.py migrate todo
python manage.py migrate
export DJANGO_SETTINGS_MODULE=project.local
python ./createusers.py
python manage.py runserver 0.0.0.0:8000

$@

