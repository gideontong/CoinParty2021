from json import load, dump
from bitcash import Key as key

folder = 'config'
secrets = None
config = None

def on_open():
    with open(f'{folder}/secrets.json') as secrets_file:
        secrets = load(secrets_file)
    with open(f'{folder}/config.json') as config_file:
        config = load(config_file)

def on_exit():
    with open(f'{folder}/secrets.json', 'w') as secrets_file:
        dump(secrets, secrets_file)

on_open()

import enquiries

options = ['thing 1', 'thing 2', 'thing 3']
choice = enquiries.choose('Choose one of these options: ', options)

if enquiries.confirm('Do you want to write something?'):
    text = enquiries.freetext('Write something interesting: ')
    print(text)

on_exit()