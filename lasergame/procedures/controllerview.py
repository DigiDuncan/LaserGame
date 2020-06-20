import importlib.resources as pkg_resources
import pygame

from digicolor import colors

import lasergame.data.sprites.buttons as buttondata
from lasergame.lib.buttons import buttons
# from lasergame.lib.pgutils import write

images = {
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
    buttons.UP: ("dpad-up", None),
    buttons.DOWN: ("dpad-down", None),
    buttons.LEFT: ("dpad-left", None),
    buttons.RIGHT: ("dpad-right", None),
    buttons.A: ("a-on", "a-off"),
    buttons.B: ("b-on", "b-off"),
    buttons.X: ("x-on", "x-off"),
    buttons.Y: ("y-on", "y-off"),
    buttons.L: ("l-on", "l-off"),
    buttons.R: ("r-on", "r-off"),
    buttons.SELECT: ("select-on", "select-off"),
    buttons.START: ("start-on", "start-off"),
}


# Load images.
def load_images():
    for name in images.keys():
        image = pkg_resources.open_binary(buttondata, f"{name}.png")
        pg_image = pygame.image.load(image)
        pg_image.set_colorkey(colors.LIGHT_MAGENTA.rgb)
        images[name] = pg_image


def controllersurface():
    # Create the viewport.
    controllersurface = pygame.Surface((147, 80))
    controllersurface.fill(colors.LIGHT_GRAY.rgb)
    controllersurface.blit(images["dpad-none"], (0, 0))

    pressed = pygame.key.get_pressed()

    for button, (active, inactive) in buttonmap.items():
        if pressed[button] and active:
            controllersurface.blit(images[active], (0, 0))
        elif inactive is not None:
            controllersurface.blit(images[inactive], (0, 0))

    return controllersurface


def init():
    load_images()
