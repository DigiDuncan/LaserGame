import importlib.resources as pkg_resources

import pygame
from digicolor import colors

from lasergame.objects.gameobject import GameObject
import lasergame.data.sprites.buttons as buttonsprites

image_cache = {
    "dpad-up": None,
    "dpad-none": None,
    "r-off": None,
    "r-on": None,
    "x-off": None,
    "y-off": None,
    "b-off": None,
    "x-on": None,
    "y-on": None,
    "b-on": None,
    "start-off": None,
    "select-off": None,
    "a-off": None,
    "a-on": None,
    "l-off": None,
    "start-on": None,
    "select-on": None,
    "l-on": None,
    "dpad-down": None,
    "dpad-left": None,
    "dpad-right": None
}

buttonmap = {
    "UP": ("dpad-up", None),
    "DOWN": ("dpad-down", None),
    "LEFT": ("dpad-left", None),
    "RIGHT": ("dpad-right", None),
    "A": ("a-on", "a-off"),
    "B": ("b-on", "b-off"),
    "X": ("x-on", "x-off"),
    "Y": ("y-on", "y-off"),
    "L": ("l-on", "l-off"),
    "R": ("r-on", "r-off"),
    "SELECT": ("select-on", "select-off"),
    "START": ("start-on", "start-off"),
}


class Controller(GameObject):
    __slots__ = ["buttons"]

    def __init__(self):
        for name in image_cache.keys():
            image_file = pkg_resources.open_binary(buttonsprites, f"{name}.png")
            image = pygame.image.load(image_file)
            image.set_colorkey(colors.LIGHT_MAGENTA.rgb)
            image_cache[name] = image
        self.buttons = None
        super().__init__()

    def update(self, gm, events, **kwargs):
        self.buttons = {btn.name: btn.held for btn in gm.input.buttons}

    def draw(self, debugscreen, **kwargs):
        surface = pygame.Surface((147, 80))
        surface.fill(colors.LIGHT_GRAY.rgb)
        surface.blit(image_cache["dpad-none"], (0, 0))

        for name, (active, inactive) in buttonmap.items():
            if self.buttons[name] and active:
                surface.blit(image_cache[active], (0, 0))
            elif inactive is not None:
                surface.blit(image_cache[inactive], (0, 0))

        debugscreen.blit(surface, self.center)
