import pygame

from digicolor import colors

from lasergame.classes.projectile import Projectile
from lasergame.lib.utils import degreesToXY

bullettypes = {
    "red": {
        "color": colors.RED.rgb,
        "damage": 1,
        "radius": 2
    },
    "orange": {
        "color": colors.DARK_ORANGE.rgb,
        "damage": 2,
        "radius": 2
    },
    "yellow": {
        "color": colors.YELLOW.rgb,
        "damage": 3,
        "radius": 2
    },
    "green": {
        "color": colors.LIGHT_GREEN.rgb,
        "damage": 4,
        "radius": 2
    },
    "blue": {
        "color": colors.BLUE.rgb,
        "damage": 5,
        "radius": 3
    },
    "purple": {
        "color": colors.LIGHT_MAGENTA.rgb,
        "damage": 10,
        "radius": 4
    }
}


class Bullet(Projectile):
    __slots__ = ["bullettype", "angle", "speed"]

    def __init__(self, center: tuple, angle = 90, *, owner, bullettype = "red", **kwargs):
        self.bullettype = bullettype
        self.angle = angle
        super().__init__(center = center, owner = owner, **kwargs)

    @property
    def color(self):
        if self.bullettype:
            return bullettypes[self.bullettype]["color"]
        else:
            return bullettypes["red"]["color"]

    @property
    def damage(self):
        if self.bullettype:
            return bullettypes[self.bullettype]["damage"]
        else:
            return bullettypes["red"]["damage"]

    @property
    def radius(self):
        if self.bullettype:
            return bullettypes[self.bullettype]["radius"]
        else:
            return bullettypes["red"]["radius"]

    @property
    def xmove(self):
        xy = degreesToXY(self.angle)
        return xy["x"] * self.speed

    @property
    def ymove(self):
        xy = degreesToXY(self.angle)
        for k, v in xy.items():
            v *= self.speed
        return xy["y"] * self.speed

    @property
    def uuid_offset(self):
        return self.radius + 3

    def update(self, clock, screen, gm, **kwargs):
        self.x += self.xmove * clock.get_time_secs()
        self.y += self.ymove * clock.get_time_secs()
        if not self.is_on_screen(screen):
            gm.discard(self)
        super().update(gm=gm, clock=clock, screen=screen)

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

    def draw(self, screen, debugscreen, **kwargs):
        pygame.draw.circle(screen, self.color, self.safecenter, self.radius)
        super().draw(screen = screen, debugscreen = debugscreen)
