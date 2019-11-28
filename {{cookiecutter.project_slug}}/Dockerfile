FROM python:3.7-alpine
LABEL maintainer="{{ cookiecutter.email }}"

ENV PYTHONUNBUFFERED 1

ARG EXTRA_PACKAGES=""

# init
RUN apk --no-cache add --update \
    ${EXTRA_PACKAGES} \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext

USER ${UID}:${GROUPS}

# app directory
RUN ["mkdir", "/app"]
WORKDIR /app

# Copy dependency first to reduce rebuild time
COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN ["chmod", "+x", "docker-entrypoint.sh"]

# CMD [ "python", "manage.py" ]
ENTRYPOINT [ "./docker-entrypoint.sh" ]
