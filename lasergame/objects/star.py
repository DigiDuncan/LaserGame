import random

import pygame

from digicolor import colors

from lasergame.objects.gameobject import GameObject


class Star(GameObject):
    colors = [colors.LIGHT_GRAY.rgb, colors.WHITE.rgb, colors.LIGHT_YELLOW.rgb, colors.YELLOW.rgb]
    twinkle_wait = 64

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.twinkle = random.randint(0, self.twinkle_wait * 4)

    def update(self, events):
        self.twinkle = (self.twinkle + 1) % (self.twinkle_wait * 4)

    @property
    def color(self):
        color_index = int(self.twinkle / self.twinkle_wait)
        return self.colors[color_index]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 2)
