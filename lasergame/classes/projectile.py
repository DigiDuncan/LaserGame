import pygame

from lasergame.classes.collidablegameobject import CollidableGameObject

# TODO: Not done, still needs to be stripped.
class Projectile(CollidableGameObject):
    __slots__ = []

    def __init__(self, center: tuple, *, speed = 180, bullettype = "red", radius = 2):
        self.speed = speed
        self.bullettype = bullettype
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
        return self.x + self.radius > 0 \
            and self.x - self.radius < screen.get_width() \
            and self.y + self.radius > 0 \
            and self.y - self.radius < screen.get_height()

    @property
    def left(self):
        return self.x - self.radius

    @property
    def top(self):
        return self.y - self.radius

    @property
    def right(self):
        return self.left + self.radius * 2

    @property
    def bottom(self):
        return self.top + self.radius * 2

    @property
    def collision_box(self):
        return pygame.Rect(self.left, self.top, self.radius * 2, self.radius * 2)

    def draw(self, screen, debugscreen, **kwargs):
        self.draw_uuid(debugscreen, self.radius * 3 + 8)
        return self.collision_box
