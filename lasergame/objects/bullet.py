import pygame

from digicolor import colors

# from lasergame.lib.buttons import buttons
from lasergame.lib.constants import game
from lasergame.lib.utils import clamp
from lasergame.objects.gameobject import GameObject


class Bullet(GameObject):
    def __init__(self, center: tuple, *, color = colors.RED.rgb, speed = 180, bullettype = "default", size = 2):
        self.color = color
        self.speed = speed
        self.bullettype = bullettype
        self.size = size
        self.center = center

    @property
    def x(self):
        return self.center[0]

    @x.setter
    def x(self, value):
        self.center = (value, self.center[1])

    @property
    def y(self):
        return self.center[1]

    @y.setter
    def y(self, value):
        self.center = (self.center[0], value)

    def update(self, clock, **kwargs):
        self.x += self.speed * clock.get_time_secs()

    def draw(self, screen):
        boundingBox = pygame.draw.circle(screen, self.color, (int(self.center[0]), int(self.center[1])), self.size)

        return boundingBox
