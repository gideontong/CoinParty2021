from consolemenu import ConsoleMenu as Menu
from consolemenu.items import FunctionItem as Option, MenuItem as SubMenu

class GameMenus:
    def __init__(self, config: dict, secrets: dict):
        self.config = config
        self.secrets = secrets