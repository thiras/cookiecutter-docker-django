import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/{{ cookiecutter.gitlab_username }}/{{ cookiecutter.project_slug }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Flake8",
        CC_LICENSE_CC,
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    install_requires=[
        "django",
        "django-environ",
        "django-extensions",
        "django-model-utils",
        "psycopg2-binary",
        "gunicorn",
        "coverage"
    ],
    extras_require={
        "dev": [
            "django-debug-toolbar",
            "flake8",
            "flake8-django",
            "pre-commit",
        ]
    },
    python_requires='>=3.7',
)
