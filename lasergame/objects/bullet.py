import pygame

from digicolor import colors

from lasergame.classes.collidablegameobject import CollidableGameObject

bulletcolors = {
    "red":    colors.RED.rgb,
    "orange": colors.DARK_ORANGE.rgb,
    "yellow": colors.YELLOW.rgb,
    "green":  colors.LIGHT_GREEN.rgb,
    "blue":   colors.BLUE.rgb,
    "purple": colors.LIGHT_MAGENTA.rgb
}


class Bullet(CollidableGameObject):
    __slots__ = ["speed", "bullettype", "radius"]

    def __init__(self, center: tuple, *, speed = 180, bullettype = "red", radius = 2):
        self.speed = speed
        self.bullettype = bullettype
        self.radius = radius
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
        super().update(gm=gm)

    def is_on_screen(self, screen):
        return self.x + self.radius > 0 \
            and self.x - self.radius < screen.get_width() \
            and self.y + self.radius > 0 \
            and self.y - self.radius < screen.get_height()

    def draw(self, screen, debugscreen, **kwargs):
        self.boundingBox = pygame.draw.circle(screen, self.color, (int(self.center[0]), int(self.center[1])), self.radius)
        self.draw_uuid(debugscreen, self.radius * 3 + 8)
        return self.boundingBox
