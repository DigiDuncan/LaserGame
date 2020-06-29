from lasergame.lib.conf import settings


class State:
    __slots__ = ["debug"]

    def __init__(self):
        self.debug = settings.debug
