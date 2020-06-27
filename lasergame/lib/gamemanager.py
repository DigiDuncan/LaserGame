from operator import attrgetter

from lasergame.classes.collidablegameobject import CollidableGameObject
from lasergame.lib.inputmanager import InputManager
from lasergame.lib.state import State
from lasergame.objects.bullet import Bullet


class GameManager:
    __slots__ = ["_objects", "state", "input"]

    def __init__(self, inputmanager: InputManager):
        self._objects = set()
        self.state = State()
        self.input = inputmanager

    def update(self, events, **kwargs):
        for o in list(self._objects):
            o.update(gm=self, events=events, **kwargs)

    def draw(self, **kwargs):
        for o in sorted(self._objects, key=attrgetter("z")):
            o.draw(**kwargs)

    def collide(self, **kwargs):
        for o1 in self.nonbullet_collidables:
            for o2 in self.collidables:
                o1.collide(o2, gm = self)

    def add(self, obj):
        self._objects.add(obj)

    def discard(self, obj):
        self._objects.discard(obj)

    def __len__(self):
        return len(self._objects)

    @property
    def collidables(self):
        return [o for o in self._objects if isinstance(o, CollidableGameObject)]

    @property
    def nonbullet_collidables(self):
        return [o for o in self._objects if isinstance(o, CollidableGameObject) and not isinstance(o, Bullet)]
