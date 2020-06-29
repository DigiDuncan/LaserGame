import importlib.resources as pkg_resources

import toml

import lasergame.data
from lasergame.lib.attrdict import AttrDict

buttons = None
game = None


def loadgame(data):
    global game
    gamedict = data.get("game", {})
    # make all names lowercase
    gamedict = {name.lower(): value for name, value in gamedict.items()}
    # create the enum
    game = AttrDict(gamedict)
    game.center = (round(game.width / 2), round(game.height / 2))


def loadbuttons(data):
    global buttons
    buttons = data.get("buttons", {})


def load():
    # Load constants toml file
    data = toml.loads(pkg_resources.read_text(lasergame.data, "constants.toml"))
    loadbuttons(data)
    loadgame(data)


load()
