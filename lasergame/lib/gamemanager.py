from functools import lru_cache

from lasergame.classes.abc import Drawable, Updateable, Collidable
from lasergame.lib.inputmanager import InputManager
from lasergame.lib.collisionmanager import CollisionManager
from lasergame.lib.state import State
from lasergame.lib.utils import default_itemgetter
from lasergame.objects.bullet import Bullet


class GameManager:
    __slots__ = ["_drawables", "_updateables", "_collidables", "_projectiles", "state", "input", "collisions"]

    def __init__(self, inputmanager: InputManager):
        self._drawables = set()
        self._updateables = set()
        self._collidables = set()
        self._projectiles = set()
        self.state = State()
        self.input = inputmanager
        self.collisions = CollisionManager()

    def update(self, events, **kwargs):
        """Update every object with a `.update()` method"""
        self.collisions.update(self._collidables, self._projectiles)
        for o in list(self._updateables):
            o.update(gm=self, events=events, **kwargs)

    def draw(self, **kwargs):
        """Draw every object with a `.draw()` method, in order of increasing `.z` value"""
        for o in sorted(self._drawables, key=default_itemgetter("z", default=0)):
            o.draw(**kwargs)

    def add(self, obj):
        """Add new objects to the appropriate Set collections, depending on the features they support"""
        if isinstance(obj, Drawable):
            self._drawables.add(obj)
        if isinstance(obj, Updateable):
            self._updateables.add(obj)
        if isinstance(obj, Collidable) and not isinstance(obj, Bullet):
            self._collidables.add(obj)
        if isinstance(obj, Collidable) and isinstance(obj, Bullet):
            self._projectiles.add(obj)
        self.__len__.cache_clear()

    def discard(self, obj):
        """Remove objects from the all the Set collections they are in"""
        self._drawables.discard(obj)
        self._updateables.discard(obj)
        self._collidables.discard(obj)
        self._projectiles.discard(obj)
        self.__len__.cache_clear()

    @lru_cache(maxsize=1)
    def __len__(self):
        """Count up all unique objects (cached for performance)"""
        return len(self._drawables | self._updateables | self._updateables | self._projectiles)
