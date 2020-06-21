from operator import attrgetter

from lasergame.lib.state import State


class GameManager:
    def __init__(self):
        self._objects = set()
        self.state = State()

    def update(self, **kwargs):
        for o in list(self._objects):
            o.update(gm=self, **kwargs)

    def draw(self, **kwargs):
        for o in sorted(self._objects, key=attrgetter("z")):
            o.draw(**kwargs)

    def add(self, obj):
        self._objects.add(obj)

    def discard(self, obj):
        self._objects.discard(obj)

    def __len__(self):
        return len(self._objects)
