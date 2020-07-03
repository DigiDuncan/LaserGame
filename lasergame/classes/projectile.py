import pygame

from lasergame.classes.collidablegameobject import CollidableGameObject


# TODO: Not done, still needs to be stripped.
class Projectile(CollidableGameObject):
    __slots__ = []

    def __init__(self, center: tuple, *, speed = 180, radius = 2):
        self.radius = radius
        super().__init__(center=center)

    @property
    def color(self):
        pass

    def update(self, clock, screen, gm, **kwargs):
        if not self.is_on_screen(screen):
            gm.discard(self)
        super().update(gm=gm)

    def is_on_screen(self, screen):
        raise NotImplementedError

    @property
    def left(self):
        raise NotImplementedError

    @property
    def top(self):
        raise NotImplementedError

    @property
    def right(self):
        raise NotImplementedError

    @property
    def bottom(self):
        raise NotImplementedError

    @property
    def collision_box(self):
        return pygame.Rect(self.left, self.top, self.radius * 2, self.radius * 2)

    def draw(self, screen, debugscreen, **kwargs):
        self.draw_uuid(debugscreen, self.radius * 3 + 8)
        return self.collision_box
