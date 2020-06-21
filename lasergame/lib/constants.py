import importlib.resources as pkg_resources

import toml

import lasergame.data

buttons = None


def loadbuttons(data):
    global buttons
    buttons = data.get("buttons", {})


def load():
    # Load constants toml file
    data = toml.loads(pkg_resources.read_text(lasergame.data, "constants.toml"))
    loadbuttons(data)


load()
