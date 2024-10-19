# Technical assignement
 Le backend est fait avec Python/Django, avec un base de donnés Postgres

 ## How to start the app

L'application est dockerisé donc il suffit de tapez la commande suivante `docker compose up -d --build`

ou bien si vous voulez le faire localement il suffit de tapez les commandes suivantes (il est préférable de créer un environment virtuels avant )

1- `make run_postgres_local` pour lancer le docker container pour la base de donnés

2- `pip install -r requirements.txt` pour installer les dependencies

3- `python manage.py migrate` pour faire les migrations

4- `python manage.py runserver` pour lancer l'application

## Docs

une interface swagger est fournite sur `http://localhost:8000/api/v1/docs/` pour pouvoir visualiser l'API

## Tests

les tests sont réalisés avec pytest et il couvrent l'intégralité des exigences du test technique