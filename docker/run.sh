#!/bin/bash

./waitforit.sh ${DB_HOST}:${DB_PORT}
python manage.py migrate
python ./createusers.py
python manage.py runserver 0.0.0.0:8000

$@

