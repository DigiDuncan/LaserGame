import random

import pygame

from digicolor import colors

from lasergame.objects.gameobject import GameObject


class Star(GameObject):
    colors = [colors.LIGHT_GRAY.rgb] * 300 + [colors.WHITE.rgb] * 4 + [colors.LIGHT_YELLOW.rgb] * 4 + [colors.YELLOW.rgb]
    color_speed = 8

    def __init__(self, center):
        self.twinkle = random.random() * len(self.colors)
        super().__init__(center=center)

    def update(self, clock, **kwargs):
        self.twinkle = (self.twinkle + (self.color_speed * clock.get_time_secs())) % len(self.colors)

    @property
    def color(self):
        color_index = int(self.twinkle)
        return self.colors[color_index]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 2)
