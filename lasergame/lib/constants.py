import importlib.resources as pkg_resources

import toml

import lasergame.data
from lasergame.lib.attrdict import AttrDict

game = None
buttons = None


def loadgame(data):
    global game
    gamedict = data.get("game", {})
    # make all names lowercase
    gamedict = {name.lower(): value for name, value in gamedict.items()}
    # create the enum
    game = AttrDict(gamedict)
    if not isinstance(game.scale, int):
        raise ValueError("Scale is not an integer.")
    game["windowwidth"] = game.width * game.scale
    game["windowheight"] = game.height * game.scale
    game["center"] = (round(game.width / 2), round(game.height / 2))


def loadbuttons(data):
    global buttons
    buttonsdict = data.get("buttons", {})
    # make all names lowercase
    buttonsdict = {name.lower(): value for name, value in buttonsdict.items()}
    # create the enum
    buttons = AttrDict(buttonsdict)


def load():
    # Load constants toml file
    data = toml.loads(pkg_resources.read_text(lasergame.data, "constants.toml"))
    loadgame(data)
    loadbuttons(data)


load()
