from typing import Literal

from digicolor import colors
from lasergame.lib import fonts

font = None


def write(screen, coords, text, *, color=colors.WHITE.rgb, align: Literal["left", "center", "right"] = "left", antialias: bool = True):
    textsurface = fonts.render(text, antialias=antialias, color=color)
    if coords[0] < 0:
        coords = (screen.get_width() + coords[0] - textsurface.get_width(), coords[1])
    if coords[1] < 0:
        coords = (coords[0], screen.get_height() + coords[1] - textsurface.get_height())
    if align == "center":
        coords = (coords[0] - (textsurface.get_width() / 2), coords[1])
    if align == "right":
        coords = (coords[0] - textsurface.get_width(), coords[1])
    screen.blit(textsurface, coords)
