import pygame

from digicolor import colors

from lasergame.objects.gameobject import GameObject


class Star(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, colors.WHITE.rgb, (self.x, self.y), 2)
