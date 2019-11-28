# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Development

{% if cookiecutter.package_manager == "pipenv %}
To start develop locally, first, you need to create your virtual environment and install dependencies. To do this;

```
pipenv install --dev
```
{% elif cookiecutter.package_manager == "poerty" %}
To start develop locally, first, you need to have poetry's preview version.

```
poetry self:update --preview
```

After having that, you need to create virtual environment and install dependencies.

```
poetry install
```
{% elif cookiecutter.package_manager == "pip-tools/no manager"}
To start develop locally, first, you need to create your virtual environment and activate it with;
```
python3 -m venv .venv/
source .venv/bin/activate
```

After that install `pip-tools` for deterministic environments and create your deterministic environment;

```
pip install wheel pip-tools
pip-compile
```
{% endif %}
{% if cookiecutter.use_docker == "y" %}
To create requirements.txt for Docker, simply run;

{% if cookiecutter.package_manager == "pipenv" %}
```
pipenv lock -r > requirements.txt
```
{% elif cookiecutter.package_manager == "poerty" %}
```
poetry export -f requirements.txt
```
{% elif cookiecutter.package_manager == "pip-tools/no manager" %}
```
pip-compile - --output-file=- < requirements.in > requirements.txt
```
{% endif %}

Then simply start docker-compose stack with;

```
docker-compose up -d
```

Code changes will be immediately reflected on the container since project root mounted as volume.
{% endif %}
