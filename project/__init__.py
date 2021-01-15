from consolemenu import ConsoleMenu as Menu
from consolemenu.items import FunctionItem as Option, SubmenuItem as Submenu

class GameMenus:
    def __init__(self, config: dict, secrets: dict):
        self.config = config
        self.secrets = secrets

    def create_menu(self, name):
        menu_config = self.config['menus'][name]
        menu = Menu(menu_config['title'], menu_config['subtitle'])
        for item in menu_config['options']:
            if item['type'] == 'menu':
                submenu = self.create_menu(item['function'])
                menu.append_item(Submenu(item['label'], submenu, menu))
            elif item['type'] == 'function':
                pass
        return menu
