from typing import Literal

import pygame

from digicolor import colors

from lasergame.lib import fonts


def write(screen, coords, text, *, color=colors.WHITE.rgb, align: Literal["left", "center", "right"] = "left", antialias: bool = True,
          font=None, size=None, background=None):
    textsurface = fonts.render(text, antialias=antialias, color=color, font=font, size=size, background=background)
    if coords[0] < 0:
        coords = (screen.get_width() + coords[0] - textsurface.get_width(), coords[1])
    if coords[1] < 0:
        coords = (coords[0], screen.get_height() + coords[1] - textsurface.get_height())
    if align == "center":
        coords = (coords[0] - (textsurface.get_width() / 2), coords[1])
    if align == "right":
        coords = (coords[0] - textsurface.get_width(), coords[1])
    screen.blit(textsurface, coords)


def draw_box(screen, center: tuple, width: int, height: int, *, color = colors.WHITE.rgb, thickness: int = 0):
    left = center[0] - (width / 2)
    top = center[1] - (height / 2)
    rect = pygame.Rect(left, top, width, height)
    return pygame.draw.rect(screen, color, rect, thickness)
