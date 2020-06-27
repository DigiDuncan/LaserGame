class MenuItem:
    def __init__(self, name, text, function):
        self.name = name
        self.text = text
        self.function = function


class Menu:
    def __init__(self, position: tuple, items: list, *, cursorsettings: dict, fontsettings: dict):
        pass
