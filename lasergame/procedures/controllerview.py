import importlib.resources as pkg_resources
import pygame

import lasergame.data.sprites.buttons as buttondata
from lasergame.lib.constants import buttons
# from lasergame.lib.pgutils import write

# Load images.


# Image coords.
coords = {
    "layout": (0, 0)

}


def add_image(surface, name):
    image = pkg_resources.read_binary(buttondata, f"{name}.png")
    pg_image = pygame.image.load(image)
    surface.blit(pg_image, coords[name])


def controllersurface():

    # Create the viewport.
    controllersurface = pygame.Surface((80, 147))
    add_image(controllersurface, "layout")

    if pygame.key.get_pressed()[buttons.UP]:
        pass
    if pygame.key.get_pressed()[buttons.DOWN]:
        pass
    if pygame.key.get_pressed()[buttons.LEFT]:
        pass
    if pygame.key.get_pressed()[buttons.RIGHT]:
        pass

    return controllersurface
