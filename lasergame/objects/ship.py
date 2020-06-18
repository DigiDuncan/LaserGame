import pygame

from digicolor import colors

from lasergame.lib.buttons import buttons
from lasergame.lib.constants import game
from lasergame.lib.utils import clamp
from lasergame.objects.gameobject import GameObject


class Ship(GameObject):
    def __init__(self, base: int, height: int, center: tuple, speed, color: tuple = colors.WHITE.rgb):
        self.base = base
        self.height = height
        self.center = center
        self.color = color
        self.speed = speed

    @property
    def x(self):
        return self.center[0]

    @x.setter
    def x(self, value):
        value = clamp(0, value, game.width)
        self.center = (value, self.center[1])

    @property
    def y(self):
        return self.center[1]

    @y.setter
    def y(self, value):
        value = clamp(0, value, game.height)
        self.center = (self.center[0], value)

    def update(self, events):
        if pygame.key.get_pressed()[buttons.UP]:
            self.y -= self.speed
        if pygame.key.get_pressed()[buttons.DOWN]:
            self.y += self.speed
        if pygame.key.get_pressed()[buttons.LEFT]:
            self.x -= self.speed
        if pygame.key.get_pressed()[buttons.RIGHT]:
            self.x += self.speed

    def draw(self, screen):
        boundingBox = drawTriangle(screen, self.color, self.center, self.base, self.height)
        return boundingBox


def drawTriangle(screen, color, center, base, height):
    x, y = center
    b = base
    h = height
    u1 = x
    u2 = y - (h / 2)
    v1 = x - (b / 2)
    v2 = y + (h / 2)
    w1 = x + (b / 2)
    w2 = y + (h / 2)
    u = (u1, u2)
    v = (v1, v2)
    w = (w1, w2)
    uvw = (u, v, w)
    boundingBox = pygame.draw.polygon(screen, color, uvw)
    return boundingBox
