import pygame

from digicolor import colors

from lasergame.lib.buttons import buttons
from lasergame.lib.constants import game
from lasergame.objects.gameobject import GameObject


class Bullet(GameObject):
    def __init__(self, center: tuple, *, color = colors.RED.rgb, speed = 180, bullettype = "default", radius = 2):
        self.color = color
        self.speed = speed
        self.bullettype = bullettype
        self.radius = radius
        super().__init__(center=center)

    def update(self, clock, screen, gm, **kwargs):
        self.x += self.speed * clock.get_time_secs()
        if not self.is_on_screen(screen):
            gm.discard(self)
        self.showuuid = pygame.key.get_pressed()[buttons.SELECT] and gm.state.debug

    def is_on_screen(self, screen):
        return self.x + self.radius > 0 \
            and self.x - self.radius < screen.get_width() \
            and self.y + self.radius > 0 \
            and self.y - self.radius < screen.get_height()

    def draw(self, screen, debugscreen, **kwargs):
        boundingBox = pygame.draw.circle(screen, self.color, (int(self.center[0]), int(self.center[1])), self.radius)
        self.draw_uuid(debugscreen, self.radius * 3 + 8)
        return boundingBox
