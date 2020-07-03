import pygame

from digicolor import colors

from lasergame.classes.projectile import Projectile

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
    __slots__ = ["speed", "bullettype", "speed"]

    def __init__(self, center: tuple, *, owner, speed = 180, bullettype = "red", **kwargs):
        self.bullettype = bullettype
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

    def update(self, clock, screen, gm, **kwargs):
        self.x += self.speed * clock.get_time_secs()
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

    @property
    def collision_box(self):
        return pygame.Rect(self.left, self.top, self.radius * 2, self.radius * 2)

    def draw(self, screen, debugscreen, **kwargs):
        pygame.draw.circle(screen, self.color, self.safecenter, self.radius)
        self.draw_uuid(debugscreen, self.radius * 3 + 8)
        return self.collision_box
