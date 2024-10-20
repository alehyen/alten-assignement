#!/bin/bash

if [ ${DATABASE} = "postgres" ]
then
  echo "waiting for postgres ..."

  while ! nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
    sleep 0.1
  done

  echo "postgres started"
fi

python manage.py migrate

exec "$@"
