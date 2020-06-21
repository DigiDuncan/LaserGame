import importlib.resources as pkg_resources

import pygame
from digicolor import colors

from lasergame.objects.gameobject import GameObject
import lasergame.data.sprites.buttons as buttonsprites

image_cache = {}

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


def get_image(name):
    image = image_cache.get(name)
    if image is None:
        image_file = pkg_resources.open_binary(buttonsprites, f"{name}.png")
        image = pygame.image.load(image_file)
        image.set_colorkey(colors.LIGHT_MAGENTA.rgb)
        image_cache[name] = image
    return image


class Controller(GameObject):
    __slots__ = ["buttons", "show"]

    def __init__(self):
        self.buttons = None
        self.show = False
        super().__init__()

    def update(self, gm, events, **kwargs):
        self.buttons = {btn.name: btn.held for btn in gm.input.buttons}
        self.show = gm.state.debug

    def draw(self, debugscreen, **kwargs):
        if not self.show:
            return
        surface = get_image("controller").copy()

        for name, (active, inactive) in buttonmap.items():
            if self.buttons[name]:
                if active is not None:
                    surface.blit(get_image(active), (0, 0))
            else:
                if inactive is not None:
                    surface.blit(get_image(inactive), (0, 0))

        debugscreen.blit(surface, self.center)
