from lasergame.lib.conf import game


class State:
    __slots__ = ["debug"]

    def __init__(self):
        self.debug = game.debug
