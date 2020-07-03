import pygame

from digicolor import colors

from lasergame.classes.projectile import Projectile

bulletcolors = {
    "red":    colors.RED.rgb,
    "orange": colors.DARK_ORANGE.rgb,
    "yellow": colors.YELLOW.rgb,
    "green":  colors.LIGHT_GREEN.rgb,
    "blue":   colors.BLUE.rgb,
    "purple": colors.LIGHT_MAGENTA.rgb
}


class Bullet(Projectile):
    __slots__ = ["speed", "bullettype", "radius"]

    def __init__(self, center: tuple, *, speed = 180, bullettype = "red"):
        self.speed = speed
        self.bullettype = bullettype
        super().__init__(center=center)

    @property
    def color(self):
        if self.bullettype:
            return bulletcolors[self.bullettype]
        else:
            return bulletcolors["red"]

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
