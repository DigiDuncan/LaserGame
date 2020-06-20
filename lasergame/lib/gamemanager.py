from operator import attrgetter


class GameManager:
    def __init__(self, clock):
        self.clock = clock
        self._objects = set()

    def update(self, events, screen):
        for o in list(self._objects):
            o.update(events=events, clock=self.clock, gm=self, screen=screen)

    def draw(self, screen):
        for o in sorted(self._objects, key=attrgetter("z")):
            o.draw(screen)

    def add(self, obj):
        self._objects.add(obj)

    def discard(self, obj):
        self._objects.discard(obj)

    def __len__(self):
        return len(self._objects)
