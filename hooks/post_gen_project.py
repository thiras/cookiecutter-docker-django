import os
import random
import string


def remove(*file_names):
    for i in file_names:
        os.remove(i)


def generate_random_string(
    length: int,
    digits: bool = True,
    ascii_letters: bool = True,
    punctuation: bool = False
):
    symbols = []
    if digits:
        symbols += string.digits
    if ascii_letters:
        symbols += string.ascii_letters
    if punctuation:
        punctuation = '!@#$%^&*(-_=+)'
        symbols += ''.join(punctuation)
    return ''.join([random.choice(symbols) for i in range(length)])


def set_flag(
    file_path: str,
    flag: str,
    value: str = None,
    formatted: str = None,
    *args,
    **kwargs
):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your system. "
                "Please, make sure to manually {} later.".format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def main():
    if "{{ cookiecutter.license }}" ==  "Not open source":
        remove('LICENSE')

    if "{{ cookiecutter.create_gitlab_ci }}".lower() == "n":
        remove('.gitlab-ci.yml')

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove('docker-compose.yml', '.dockerignore', 'Dockerfile', 'docker-entrypoint.sh')

    if "{{ cookiecutter.create_gitlab_ci }}" != "with shell runner":
        remove('docker-compose.ci.yml')

    if "{{ cookiecutter.package_manager }}" == "pipenv":
        remove("pyproject.toml")
    elif "{{ cookiecutter.package_manager }}" == "poetry":
        remove("Pipfile")
    else:
        remove("Pipfile", "pyproject.toml")

    if "{{ cookiecutter.license }}" == "MIT":
        set_flag(
            "setup.py",
            "CC_LICENSE_CC",
            "License :: OSI Approved :: MIT License"
        )
    elif "{{ cookiecutter.license }}" == "BSD 3-clause":
        set_flag(
            "setup.py",
            "CC_LICENSE_CC",
            "License :: OSI Approved :: BSD License"
        )
    elif "{{ cookiecutter.license }}" == "GPLv3":
        set_flag(
            "setup.py",
            "CC_LICENSE_CC",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        )
    elif "{{ cookiecutter.license }}" == "Apache Software License 2.0":
        set_flag(
            "setup.py",
            "CC_LICENSE_CC",
            "License :: OSI Approved :: Apache Software License"
        )
    else:
        with open("setup.py", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if "CC_LICENSE_CC" in line:
                    f.write(line)
            f.truncate()

    ##################
    # .env file
    ##################

    # Set secret Key
    set_flag(
        '.env',
        'CC_SECRET_KEY_CC',
        length=50,
        punctuation=True,
    )

    # Set random database user
    set_flag(
        '.env',
        'CC_DB_USER_CC',
        length=24,
    )

    # Set random password for database user password
    set_flag(
        '.env',
        'CC_DB_PASS_CC',
        length=24,
    )

    # Set random database
    set_flag(
        '.env',
        'CC_DB_CC',
        length=32,
    )

    ##################
    # settings.py file
    ##################

    # Set development secret key at settings.py
    set_flag(
        '{{ cookiecutter.project_slug }}/settings/common.py',
        'CC_SECRET_KEY_CC',
        length=50,
        punctuation=True,
    )

    #
    # .gitlab-ci.yml
    #

    # Set random database user
    # set_flag(
    #     '.gitlab-ci.yml',
    #     'CC_DB_USER_CC',
    #     length=24,
    # )

    # # Set random password for database user password
    # set_flag(
    #     '.gitlab-ci.yml',
    #     'CC_DB_PASS_CC',
    #     length=24,
    # )

    # # Set random database
    # set_flag(
    #     '.gitlab-ci.yml',
    #     'CC_DB_CC',
    #     length=24,
    # )


if __name__ == "__main__":
    main()
