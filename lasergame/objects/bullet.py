import pygame

from digicolor import colors

from lasergame.lib.buttons import buttons
from lasergame.lib.constants import game
from lasergame.lib.utils import clamp
from lasergame.objects.gameobject import GameObject


class Bullet(GameObject):
    def __init__(self, *, color = colors.RED.rgb, speed = 180, bullettype = "default", size = 2):
        self.color = color
        self.speed = speed
        self.bullettype = bullettype
        self.size = size
