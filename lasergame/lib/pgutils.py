from typing import Literal

import pygame

from digicolor import colors

from lasergame.lib.assets import fonts, sounds
from lasergame.lib.attrdict import AttrDict


def write(screen, coords, text, *, color=colors.WHITE.rgb, align: Literal["left", "center", "right"] = "left",
          valign: Literal["top", "center", "bottom"] = "top", antialias: bool = True, font=None, size=None, background=None,
          blit = True):
    font_obj = fonts.get(font, size=size)
    textsurface = font_obj.render(text, antialias, color, background)
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
    if blit:
        screen.blit(textsurface, coords)
    return AttrDict({"surface": textsurface, "coords": coords})


def get_write_size(text, *, font=None, size=None):
    font_obj = fonts.get(font, size=size)
    return font_obj.size(text)


def draw_box(screen, center: tuple, width: int, height: int, *, color = colors.WHITE.rgb, thickness: int = 0):
    left = center[0] - int(width / 2)
    top = center[1] - int(height / 2)
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
    collision_box = pygame.draw.polygon(screen, color, uvw)
    return collision_box


def scale_rect(rect, factor):
    newrect = rect.inflate(rect.width * (factor - 1), rect.height * (factor - 1))
    newrect.x = rect.x * factor
    newrect.y = rect.y * factor
    return newrect


def play_sound(sound: str, channel = 0):
    ch = pygame.mixer.Channel(channel)
    snd = sounds.get(sound)
    ch.play(snd)
