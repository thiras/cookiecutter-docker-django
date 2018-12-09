FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# init
RUN apk --no-cache add --update \
    bash \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \
    && pip install pipenv

# app directory
RUN mkdir /app
WORKDIR /app
# COPY Pipfile /app/
# COPY Pipfile.lock /app/

# setup
RUN pipenv install --system --deploy --dev

# Django env
# COPY .env /app/mos/

# clean FIX ME
RUN apk del -r python3-dev postgresql

# prep
# COPY mos /app/
CMD python manage.py migrate && gunicorn {{ cookiecutter.project_slug }}.wsgi