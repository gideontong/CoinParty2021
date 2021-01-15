from json import load, dump
from project import GameMenus

folder = 'config'

def on_open():
    with open(f'{folder}/secrets.json') as secrets_file:
        secrets = load(secrets_file)
    with open(f'{folder}/config.json') as config_file:
        config = load(config_file)
    return secrets, config

def main(secrets, config):
    menus = GameMenus(config, secrets)
    main_menu = menus.create_menu('main')
    main_menu.show()

def on_exit(secrets):
    with open(f'{folder}/secrets.json', 'w') as secrets_file:
        dump(secrets, secrets_file)

if __name__ == '__main__':
    secrets, config = on_open()
    main(secrets, config)
    on_exit(secrets)
