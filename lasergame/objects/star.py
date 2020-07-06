import random

import pygame

from digicolor import colors

from lasergame.classes.gameobject import GameObject
from lasergame.lib.constants import zlayer


class Star(GameObject):
    __slots__ = ["twinkle", "size"]

    colors = [colors.LIGHT_GRAY.rgb] * 300 + [colors.WHITE.rgb] * 4 + [colors.LIGHT_YELLOW.rgb] * 4 + [colors.YELLOW.rgb]
    color_speed = 8

    def __init__(self, center, size = 2):
        self.twinkle = random.random() * len(self.colors)
        self.size = size
        super().__init__(center=center, z=zlayer.BACKGROUND)

    def update(self, clock, **kwargs):
        self.twinkle = (self.twinkle + (self.color_speed * clock.get_time_secs())) % len(self.colors)

    @property
    def color(self):
        color_index = int(self.twinkle)
        return self.colors[color_index]

    def draw(self, screen, **kwargs):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
