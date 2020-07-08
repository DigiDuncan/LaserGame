import pygame
from pygame.locals import DOUBLEBUF, FULLSCREEN

layers = []
output_surface = None


def set_mode(display_size, fullscreen=False):
    """Set the display mode

    This function will create the display window/screen at the newly requested size.

    The display_size argument is a pair of numbers representing the width and height of the window/screen output.
    The fullscreen argument is a boolean representing whether to create a window or a fullscreen display.

    In fullscreen mode, if a display_size is (0, 0), the full screen resolution will be used.

    Parameters
    ----------
    display_size : tuple
        The size of the display output the surface will be displayed on. The input layers will automatically scale to fit this.
    full_screen : bool, optional
        Whether to create a window or a fullscreen display.

    Returns
    -------
    The size of created output surface
    """
    global output_surface

    flags = DOUBLEBUF
    if fullscreen:
        flags = flags | FULLSCREEN
    output_surface = pygame.display.set_mode(display_size, flags)
    return output_surface.get_size()


def reset_layers():
    layers.clear()


def add_layer(surface):
    layers.append(surface)
    return surface


def remove_layer(surface):
    layers.remove(surface)


def flip():
    """Update the full display Surface to the screen

    This will update the contents of the entire display.
    The input surface will automatically be scaled to fit the window output.
    """
    for layer in layers:
        if layer.get_size() == output_surface.get_size():
            # If layer is the same size as the output, just blit it over
            output_surface.blit(layer, (0, 0))
        else:
            # If layer is a different size then the output, scale it to the output
            pygame.transform.scale(layer, output_surface.get_size(), output_surface)
    pygame.display.flip()
