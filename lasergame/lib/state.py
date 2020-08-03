from lasergame.lib.conf import settings


class State:
    __slots__ = ["debug", "score"]

    def __init__(self):
        self.debug = settings.debug
        self.score = 0
