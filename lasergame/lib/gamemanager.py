from operator import attrgetter

from lasergame.classes.abc import Drawable, Updateable, Collidable
from lasergame.lib.inputmanager import InputManager
from lasergame.lib.state import State
from lasergame.objects.bullet import Bullet


class GameManager:
    __slots__ = ["_drawables", "_updateables", "_collidables", "_nonbullet_collidables", "state", "input"]

    def __init__(self, inputmanager: InputManager):
        self._drawables = set()
        self._updateables = set()
        self._collidables = set()
        self._nonbullet_collidables = set()
        self.state = State()
        self.input = inputmanager

    def update(self, events, **kwargs):
        for o in list(self._updateables):
            o.update(gm=self, events=events, **kwargs)

    def draw(self, **kwargs):
        for o in sorted(self._drawables, key=attrgetter("z")):
            o.draw(**kwargs)

    def collide(self, **kwargs):
        for o1 in self.nonbullet_collidables:
            for o2 in self.collidables:
                o1.collide(o2, gm = self)

    def add(self, obj):
        if isinstance(obj, Drawable):
            self._drawables.add(obj)
        if isinstance(obj, Updateable):
            self._updateables.add(obj)
        if isinstance(obj, Collidable):
            self._collidables.add(obj)
        if isinstance(obj, Collidable) and not isinstance(obj, Bullet):
            self._nonbullet_collidables.add(obj)

    def discard(self, obj):
        self._drawables.discard(obj)
        self._updateables.discard(obj)
        self._collidables.discard(obj)

    def __len__(self):
        return len(self._drawables | self._updateables)

    @property
    def collidables(self):
        return list(self._collidables)

    @property
    def nonbullet_collidables(self):
        return list(self._nonbullet_collidables)
