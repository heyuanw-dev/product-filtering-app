# Django Products (Categories & Tags)

A minimal Django project that models **Products**, **Categories**, and **Tags**, and provides a simple HTML page to **search by description** and **filter by category and tags** (combinable).

## Tech
- Python 3.11+ (works with 3.10+)
- Django 5.x
- SQLite (default)

## Setup

```bash
pip install pipenv
pipenv install django
pipenv shell

# create DB
python manage.py migrate

# admin user
python manage.py createsuperuser

# run
python manage.py runserver
