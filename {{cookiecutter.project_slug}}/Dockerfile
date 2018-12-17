FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# init
RUN apk --no-cache add --update \
    bash \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext \
    && pip install pip --upgrade \
    && pip install pipenv

# app directory
RUN mkdir /app
WORKDIR /app

# Copying dependency first to reduce rebuild time
COPY Pipfile /app/
COPY Pipfile.lock /app/

# setup
RUN pipenv install --system --deploy --dev

# FIX ME: Find better solution
RUN apk del -r python3-dev postgresql

COPY . /app

CMD [ "python", "manage.py" ]