import pygame

from digicolor import colors

from lasergame.classes.gameobject import GameObject
from lasergame.lib import constants
from lasergame.lib.constants import zlayer
from lasergame.lib.pgutils import write
from lasergame.lib.utils import clamp


class Textbox(GameObject):
    def __init__(self, center: tuple, text: str, timetodeath: int, *,
                 height = 50, width = constants.game.width,
                 align = "left", valign = "top", color: tuple = colors.BLACK.rgb,
                 bordercolor: tuple = colors.WHITE.rgb, borderthickness: int = 1,
                 textspeed = 25,  # chars/sec
                 fontsettings: dict = {}):
        self.center = center
        self.text = text
        self.initialtime = self.timetodeath = timetodeath
        self.height = height
        self.width = width
        self.align = align
        self.valign = valign
        self.color = color
        self.bordercolor = bordercolor
        self.borderthickness = borderthickness
        self.textspeed = textspeed

        self.fontcolor = fontsettings.get("color", colors.WHITE.rgb)
        self.fontalign = fontsettings.get("align", "left")
        self.fontvalign = fontsettings.get("valign", "top")
        self.fontantialias = fontsettings.get("antialias", False)
        self.fontfont = fontsettings.get("font", None)
        self.fontsize = fontsettings.get("size", None)

        super().__init__(center=center, z=zlayer.TEXT)

    @property
    def left(self):
        if self.align == "left":
            return self.safex
        if self.align == "center":
            return int(self.safex + (self.width / 2))
        if self.align == "right":
            return int(self.safex + self.width)

    @property
    def top(self):
        if self.valign == "top":
            return self.safey
        if self.valign == "center":
            return int(self.safey + (self.height / 2))
        if self.valign == "bottom":
            return int(self.safey + self.height)

    @property
    def centerx(self):
        return self.left + (self.width / 2)

    @property
    def centery(self):
        return self.top + (self.width / 2)

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height

    @property
    def textcoords(self):
        tx = 0
        ty = 0
        if self.fontalign == "left":
            tx = self.left + self.borderthickness
        elif self.fontalign == "center":
            tx = self.centerx
        elif self.fontalign == "right":
            tx = self.righgt - self.borderthickness

        if self.fontvalign == "top":
            ty = self.top + self.borderthickness
        elif self.fontvalign == "center":
            ty = self.centery
        elif self.fontvalign == "bottom":
            ty = self.bottom - self.borderthickness

        return (tx, ty)

    @property
    def alive(self):
        return self.timetodeath > 0

    @property
    def timealive(self):
        return self.initialtime - self.timetodeath

    @property
    def displaytext(self):
        ci = self.timealive * self.textspeed
        currentindex = int(clamp(0, ci, len(self.text) - 1))
        return self.text[:currentindex]

    def update(self, gm, clock, **kwargs):
        self.timetodeath -= 1 / clock.get_fps()
        if not self.alive:
            gm.discard(self)

    def draw(self, screen, **kwargs):
        box = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(screen, self.color, box, 0)
        pygame.draw.rect(screen, self.bordercolor, box, self.borderthickness)
        if self.text != "":
            write(screen, self.textcoords, self.displaytext, color = self.fontcolor,
                  align = self.fontalign, valign = self.fontvalign,
                  antialias = self.fontantialias, font = self.fontfont, size = self.fontsize)
