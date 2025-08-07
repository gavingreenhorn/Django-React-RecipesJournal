# RecipesJournal

![RecipesJournal build](https://github.com/gavingreenhorn/Django-React-RecipesJournal/actions/workflows/recipes_journal.yaml/badge.svg?event=push)

## Summary

Django website with React frontend.

- view recipes posted by others and save as favorites
- create shopping lists
- subscribe to other users

## First run

~~~
setup the required env variables
cd infra
sudo docker-compose up
~~~

## Load mock data

~~~
python manage.py loadcsv users FoodgramUser
python manage.py loadcsv tags Tag
python manage.py loadcsv ingredients Ingredient
python manage.py make_relations
~~~

## Stack

- Django (exposes Rest API, provides ORM to manage data)
- React (manages web UI)
- Nginx (serves static and media requests, routes the rest to Django)
- PostgreSQL (RDBMS)
- Docker (hosts all of the above as isolated containerized services)

## API autospec

- /api/docs/redoc
- /api/docs/swagger

## Author
Gavin Greenhorn
