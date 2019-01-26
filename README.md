# Cookiecutter for Dockerized Django

Cookiecutter for Dockerized Django is an (as much as possible) unbiased [cookiecutter](https://github.com/audreyr/cookiecutter) script set for bootstrapping dockerized and CI enabled Django projects. Inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

## Features
* For latest stable Django
* Works with Python 3.6
* PostgreSQL for database
* Dependency management with [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [12-Factor](https://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
* Custom User model
* Integrated [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar), [django-extensinons](https://github.com/django-extensions/django-extensions) and [django-model-utils](https://github.com/jazzband/django-model-utils)

## Optional Integrations
* Complete dockerization with simple extendable docker-entrypoint script
* GitLab CI configuration for testing with options
  * Shell runner
  * DinD (Docker-in-Docker) runner
  * Non-dockerized shell runner
* Procfile for deploying to Heroku

## Usage
To use this cookiecutter script, you need to have Python 3 installed on your system.

First, you need to install python 3 version of Cookiecutter:

```
pip3 install cookiecutter
```

Now you can run against this repo:

```
cookiecutter https://gitlab.com/thiras/cookiecutter-docker-django
```

You'll be prompted for some values and options script needs.

## Contributions
Contributions are welcome. Contributors should comply with [Code of Conduct](CODE_OF_CONDUCT.md).
