import pygame
from typing import Literal

from digicolor import colors

from lasergame.classes.gameobject import GameObject
from lasergame.lib import conf
from lasergame.lib.pgutils import draw_triangle, write


class MenuItem:
    def __init__(self, game, name, text):
        self.game = game
        self.name = name
        self.text = text

    @property
    def function(self):
        if self.functiontype == "quit":
            return self.game.quit()


class SceneMenuItem(MenuItem):
    def __init__(self, game, name, text, *, scene):
        self.scene = scene
        super().__init__(game, name, text)

    @property
    def function(self):
        return self.game.switch_scene(self.scene)


class QuitMenuItem(MenuItem):
    @property
    def function(self):
        return self.game.quit()


class ValueMenuItem(MenuItem):
    def __init__(self, game, name, text, value, default, step = 1):
        self.value = value
        self.default = default
        self.step = step
        self._current = self.default
        super().__init__(game, name, text)

    def increment(self):
        self._current += self.step
        setattr(conf.settings, self.value, self._current)

    def decrement(self):
        self._current -= self.step
        setattr(conf.settings, self.value, self._current)

    @property
    def function(self):
        pass


class Menu(GameObject):
    def __init__(self, screen: pygame.Surface, center, items: list, *, valign: Literal["top", "center", "bottom"] = "center",
                 cursorsettings: dict, fontsettings: dict, selector_x_offset = 85):
        self.screen = screen
        self.center = center
        self.items = items
        self.valign = valign
        self.cursorsettings = cursorsettings
        self.fontsettings = fontsettings
        self.selector_x_offset = selector_x_offset

        self.fontcolor = fontsettings.get("color", colors.WHITE.rgb)
        self.fontalign = fontsettings.get("align", "center")
        self.fontantialias = fontsettings.get("antialias", False)
        self.fontfont = fontsettings.get("font", None)
        self.fontsize = fontsettings.get("size", None)

        self.cursorcolor = cursorsettings.get("color", colors.WHITE.rgb)
        self.cursorwidth = cursorsettings.get("width", 8)
        self.cursorheight = cursorsettings.get("height", 8)
        self.cursordirection = cursorsettings.get("direction", "right")

        self.selected = 0

    @property
    def fontspacing(self):
        return self.fontsize * 2

    @property
    def texttopY(self):
        return self.safey - (self.fontspacing * len(self.items) / 2)

    def update(self, *, im, **kwargs):
        if im.UP.pressed:
            self.selected -= 1
        if im.DOWN.pressed:
            self.selected += 1
        self.selected = self.selected % len(self.items)
        if isinstance(self.items[self.selected], ValueMenuItem):
            if im.LEFT.pressed:
                self.items[self.selected].decrement()
            if im.RIGHT.pressed:
                self.items[self.selected].increment()
        if im.START.pressed:
            self.items[self.selected].function

    def draw(self, **kwargs):
        for n, item in enumerate(self.items):
            if isinstance(item, ValueMenuItem):
                itemtext = f"{item.text}: {item._current}"
            else:
                itemtext = item.text
            write(self.screen, (self.x, self.texttopY + (n * self.fontspacing)), itemtext,
                  color = self.fontcolor, align = self.fontalign, antialias = self.fontantialias,
                  font = self.fontfont, size = self.fontsize)
        draw_triangle(self.screen, self.cursorcolor,
                      (self.x - self.selector_x_offset, self.texttopY + (self.selected * self.fontspacing) + round(self.fontsize / 2) + 1),
                      self.cursorwidth, self.cursorheight, self.cursordirection)
