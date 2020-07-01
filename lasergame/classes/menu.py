import pygame
from typing import Literal

from digicolor import colors

from lasergame.classes.gameobject import GameObject
from lasergame.lib import conf
from lasergame.lib.pgutils import draw_triangle, write
from lasergame.lib.utils import clamp


class MenuItem:
    def __init__(self, game, name, text):
        self.game = game
        self.name = name
        self.text = text

    @property
    def displaytext(self):
        return self.text


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
    def __init__(self, game, name, text, value, default, *, textoverrides = {}, **kwargs):
        self.value = value
        self.default = default
        self._current = self.default
        self.textoverrides = textoverrides
        super().__init__(game, name, text)

    def increment(self):
        setattr(conf.settings, self.value, self._current)

    def decrement(self):
        setattr(conf.settings, self.value, self._current)

    @property
    def function(self):
        pass

    @property
    def displaytext(self):
        if self._current in self.textoverrides:
            currenttext = self.textoverrides[self._current]
        else:
            currenttext = self._current
        return f"< {self.text}: {currenttext} >"


class BoolValueMenuItem(ValueMenuItem):
    def toggle(self):
        self._current = not self._current

    def increment(self):
        self.toggle()
        super().increment()

    def decrement(self):
        self.toggle()
        super().increment()


class IntValueMenuItem(ValueMenuItem):
    def __init__(self, game, name, text, value, default, step = 1, minimum = 0, maximum = None, **kwargs):
        self.step = step
        self.min = minimum
        self.max = maximum
        super().__init__(game, name, text, value, default, **kwargs)

    def increment(self):
        self._current += self.step
        self._current = clamp(self.min, self._current, self.max)
        super().increment()

    def decrement(self):
        self._current -= self.step
        self._current = clamp(self.min, self._current, self.max)
        super().increment()


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
        # TODO: Make this dynamic.
        # This is just a value I tweaked until it looked ok.
        # It doesn't work for every font.
        return self.fontsize / 2 + 1

    @property
    def texttopY(self):
        return self.safey - (self.fontspacing * len(self.items) / 2)

    def update(self, *, im, **kwargs):
        # Scroll up and down the menu.
        if im.UP.pressed:
            self.selected -= 1
        if im.DOWN.pressed:
            self.selected += 1
        # Wrap the cursor around.
        self.selected = self.selected % len(self.items)
        # If we're selected on a ValueMenuItem, left and right decrement and increment its value.
        if isinstance(self.items[self.selected], ValueMenuItem):
            if im.LEFT.pressed:
                self.items[self.selected].decrement()
            if im.RIGHT.pressed:
                self.items[self.selected].increment()
        if im.START.pressed:
            self.items[self.selected].function

    def draw(self, **kwargs):
        # Write each menu option in order.
        for n, item in enumerate(self.items):
            write(self.screen, (self.x, self.texttopY + (n * self.fontspacing)), item.displaytext,
                  color = self.fontcolor, align = self.fontalign, antialias = self.fontantialias,
                  font = self.fontfont, size = self.fontsize)
        # Draw the cursor.
        draw_triangle(self.screen, self.cursorcolor,
                      (self.x - self.selector_x_offset, self.texttopY + (self.selected * self.fontspacing) + round(self.fontsize / 2) + 1),
                      self.cursorwidth, self.cursorheight, self.cursordirection)
