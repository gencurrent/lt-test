#!/bin/sh


# Ожидание Базы Данных
while ! nc -z $DB_HOST $DB_PORT; do
    echo "Waiting for postgres to launch on $DB_PORT..."
    sleep 0.5 # wait for 1/10 of the second before check again
done
echo "Postgres is launched"

./manage.py migrate
./manage.py runserver 0.0.0.0:8000