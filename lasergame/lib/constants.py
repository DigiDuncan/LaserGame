import importlib.resources as pkg_resources

import toml

import lasergame.data

game = None


class AttrDict:
    def __init__(self, data):
        self.__dict__ = data


def loadgame(data):
    global game
    gamedict = data.get("game", {})
    # make all names lowercase
    gamedict = {name.lower(): value for name, value in gamedict.items()}
    # create the enum
    game = AttrDict(gamedict)


def load():
    # Load constants toml file
    data = toml.loads(pkg_resources.read_text(lasergame.data, "constants.toml"))
    loadgame(data)


load()
