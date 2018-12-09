import os
import random
import string
import fileinput
import re.sub
import urllib.request

def remove_files(*file_names):
    for i in file_names:
        os.remove(file_names)

def generate_random_string(
    length,
    digits = True,
    ascii_letters = True,
    punctuation = False
):
    symbols = []
    if digits:
        symbols += string.digits
    if ascii_letters:
        symbols += string.ascii_letters
    if punctuation:
        all_punctuation = set(string.punctuation)
        exclude = {"'", '"', '\\', '$', '/'}
        suitable = all_punctuation.difference(exclude)
        symbols += ''.join(suitable)
    return ''.join([random.choice(symbols) for i in range(length)])

def insert_random(strings, length):
    for i in strings:
        with open('.env', 'w') as f:
            s = re.sub(i, generate_random_string(length), f)
            f.write(s)

def main():
    if "{{ cookiecutter.open_source_license }}" ==  "Not open source":
        remove_files('LICENSE')

    # Generate and insert randoms
    insert_random('CC_SECRET_KEY_CC', 30)
    insert_random('CC_DB_USER_CC', 24)
    insert_random('CC_DB_PASS_CC', 24)
    insert_random('CC_DB_CC', 16)

    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove_files('docker-compose.yml', '.dockerignore', 'Dockerfile')

    
    # Download .gitignore for Django
    urllib.request.urlretrieve('https://www.gitignore.io/api/django', '.gitignore')