import pygame

from digicolor import colors


class Ship:
    def __init__(self, base: int, height: int, center: tuple, color: tuple = colors.WHITE.rgb):
        self.base = base
        self.height = height
        self.center = center
        self.color = color

        self.b = self.base
        self.h = self.height
        self.p1 = self.center[0]
        self.p2 = self.center[1]

    @property
    def u1(self):
        return self.p1

    @property
    def u2(self):
        return self.p2 - (self.h / 2)

    @property
    def v1(self):
        return self.p1 - (self.b / 2)

    @property
    def v2(self):
        return self.p2 + (self.h / 2)

    @property
    def w1(self):
        return self.p1 + (self.b / 2)

    @property
    def w2(self):
        return self.p2 + (self.h / 2)

    @property
    def u(self):
        return (self.u1, self.u2)

    @property
    def v(self):
        return (self.v1, self.v2)

    @property
    def w(self):
        return (self.w1, self.w2)

    @property
    def uvw(self):
        return [self.u, self.v, self.w]

    def draw(self, screen):
        return pygame.draw.polygon(screen, self.color, self.uvw)
