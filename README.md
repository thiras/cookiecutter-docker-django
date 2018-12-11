# Cookiecutter for Dockerized Django

Cookiecutter for Dockerized Django is an (as much as possible) unbiased [cookiecutter](https://github.com/audreyr/cookiecutter) script set for bootstrapping dockerized and CI enabled Django projects.

## Features
* For latest stable Django
* Works with Python 3.6
* PostgreSQL for database
* Dependency management with [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [12-Factor](https://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
* Custom User model
* Integrated [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar), [django-extensinons](https://github.com/django-extensions/django-extensions) and [django-model-utils](https://github.com/jazzband/django-model-utils)

## Optional Integrations
* Complete dockerization
* GitLab CI/CD for testing
* Procfile for deploying to Heroku