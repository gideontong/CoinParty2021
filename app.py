from json import load, dump
from bitcash import Key as key

secrets = None
config = None

def on_open():
    with open('secrets.json') as secrets_file:
        secrets = load(secrets_file)
    with open('config.json') as config_file:
        config = load(config_file)

def on_exit():
    with open('secrets.json', 'w') as secrets_file:
        dump(secrets, secrets_file)

on_open()

on_exit()