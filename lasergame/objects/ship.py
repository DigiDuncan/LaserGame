import pygame

from digicolor import colors

from lasergame.lib.buttons import buttons
from lasergame.lib.constants import game
from lasergame.lib.nygame import time
from lasergame.lib.utils import clamp
from lasergame.objects.gameobject import GameObject
from lasergame.objects.bullet import Bullet
from lasergame.objects.star import Star


class Ship(GameObject):
    directions = ["right", "down", "left", "up"]

    def __init__(self, width: int, height: int, center: tuple, speed, color: tuple = colors.WHITE.rgb, bulletrate = 10):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.direction = 0
        self.bulletrate = bulletrate
        self._lastbullet = 0
        super().__init__(center=center, z=1)

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

    def rotate_right(self):
        self.direction = (self.direction + 1) % 4

    def rotate_left(self):
        self.direction = (self.direction - 1) % 4

    def update(self, events, clock, gm, screen, **kwargs):
        if pygame.key.get_pressed()[buttons.UP]:
            self.y -= self.speed * clock.get_time_secs()
        if pygame.key.get_pressed()[buttons.DOWN]:
            self.y += self.speed * clock.get_time_secs()
        if pygame.key.get_pressed()[buttons.LEFT]:
            self.x -= self.speed * clock.get_time_secs()
        if pygame.key.get_pressed()[buttons.RIGHT]:
            self.x += self.speed * clock.get_time_secs()
        self.showuuid = pygame.key.get_pressed()[buttons.SELECT]

        if pygame.key.get_pressed()[buttons.A]:
            if self._lastbullet + (1 / self.bulletrate) < (time.get_ticks() / 10**9):
                gm.add(Bullet(self.center))
                self._lastbullet = time.get_ticks() / 10**9

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == buttons.L:
                    self.rotate_left()
                elif e.key == buttons.R:
                    self.rotate_right()
                elif e.key == buttons.B:
                    gm.add(Star((int(self.center[0]), int(self.center[1]))))

    def draw(self, screen):
        boundingBox = drawTriangle(screen, self.color, self.center, self.width, self.height, self.directions[self.direction])
        self.draw_uuid(screen)
        return boundingBox


def drawTriangle(screen, color, center, width, height, direction="right"):
    x, y = center
    left = x - (width / 2)
    right = x + (width / 2)
    top = y - (height / 2)
    bottom = y + (height / 2)
    middlex = x
    middley = y

    if direction == "up":
        u = (middlex, top)      # middle top (tip)
        v = (right, bottom)     # bottom right
        w = (left, bottom)      # bottom left
    elif direction == "right":
        u = (right, middley)    # middle right (tip)
        v = (left, bottom)      # bottom left
        w = (left, top)         # top left
    elif direction == "down":
        u = (middlex, bottom)   # middle bottom (tip)
        v = (left, top)         # top left
        w = (right, top)        # top right
    elif direction == "left":
        u = (left, middley)     # middle left (tip)
        v = (right, top)        # top right
        w = (right, bottom)     # bottom right
    else:
        raise ValueError("Unrecognized direction")
    uvw = (u, v, w)
    boundingBox = pygame.draw.polygon(screen, color, uvw)
    return boundingBox
