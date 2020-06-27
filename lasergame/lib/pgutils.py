from typing import Literal

import pygame

from digicolor import colors

from lasergame.lib import fonts


def write(screen, coords, text, *, color=colors.WHITE.rgb, align: Literal["left", "center", "right"] = "left",
          valign: Literal["top", "center", "bottom"] = "top", antialias: bool = True, font=None, size=None, background=None):
    textsurface = fonts.render(text, antialias=antialias, color=color, font=font, size=size, background=background)
    if coords[0] < 0:
        coords = (screen.get_width() + coords[0] - textsurface.get_width(), coords[1])
    if coords[1] < 0:
        coords = (coords[0], screen.get_height() + coords[1] - textsurface.get_height())
    if align == "center":
        coords = (coords[0] - (textsurface.get_width() / 2), coords[1])
    if align == "right":
        coords = (coords[0] - textsurface.get_width(), coords[1])
    if valign == "center":
        coords = (coords[0], coords[1] - (textsurface.get_height() / 2))
    if valign == "bottom":
        coords = (coords[0], coords[1] - textsurface.get_height())
    screen.blit(textsurface, coords)


def draw_box(screen, center: tuple, width: int, height: int, *, color = colors.WHITE.rgb, thickness: int = 0):
    left = center[0] - (width / 2)
    top = center[1] - (height / 2)
    rect = pygame.Rect(left, top, width, height)
    return pygame.draw.rect(screen, color, rect, thickness)


def draw_triangle(screen, color, center, width, height, direction="right"):
    x, y = center
    left = x - (width / 2)
    right = x + (width / 2)
    top = y - (height / 2)
    bottom = y + (height / 2)
    middlex = x
    middley = y

    if direction == "up":
        u = (middlex, top)      # middle top (tip)
        v = (right, bottom)     # bottom right
        w = (left, bottom)      # bottom left
    elif direction == "right":
        u = (right, middley)    # middle right (tip)
        v = (left, bottom)      # bottom left
        w = (left, top)         # top left
    elif direction == "down":
        u = (middlex, bottom)   # middle bottom (tip)
        v = (left, top)         # top left
        w = (right, top)        # top right
    elif direction == "left":
        u = (left, middley)     # middle left (tip)
        v = (right, top)        # top right
        w = (right, bottom)     # bottom right
    else:
        raise ValueError("Unrecognized direction")
    uvw = (u, v, w)
    boundingBox = pygame.draw.polygon(screen, color, uvw)
    return boundingBox
