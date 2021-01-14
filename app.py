from json import load, dump
from bitcash import Key
from consolemenu import ConsoleMenu as Menu
from consolemenu.items import FunctionItem as Option, MenuItem as SubMenu
from project import GameMenus

folder = 'config'
secrets = None
config = None

def on_open():
    global secrets, config
    with open(f'{folder}/secrets.json') as secrets_file:
        secrets = load(secrets_file)
    with open(f'{folder}/config.json') as config_file:
        config = load(config_file)

def main():
    global secrets, config
    GameMenus(config, secrets)

def on_exit():
    global secrets
    with open(f'{folder}/secrets.json', 'w') as secrets_file:
        dump(secrets, secrets_file)

on_open()

on_exit()