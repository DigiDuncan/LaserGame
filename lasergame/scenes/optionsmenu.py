import pygame

from digicolor import colors

from lasergame.classes.menu import Menu, SceneMenuItem, IntValueMenuItem, BoolValueMenuItem
from lasergame.lib import conf
from lasergame.lib.pgutils import write


class OptionsMenu:
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.inputmanager = game.im
        self.items = [
            IntValueMenuItem(self.game, "framerate", "FRAMERATE", "framerate", 60, textoverrides = {0: "UNLOCKED", 69: "NICE"}),
            # Scale does not change.
            IntValueMenuItem(self.game, "scale", "SCALE", "scale", 4, minimum = 1, maximum = 5),
            # Nor does debug.
            BoolValueMenuItem(self.game, "debug", "DEBUG", "debug", True),
            SceneMenuItem(self.game, "back", "BACK TO MAIN MENU", scene = "mainmenu")
        ]
        self.menu = Menu(
            self.screen, conf.game.center, self.items, cursorsettings = {
                "color": colors.WHITE.rgb,
                "width": 8,
                "height": 8,
                "direction": "right"
            },
            fontsettings = {
                "color": colors.WHITE.rgb,
                "align": "center",
                "antialias": False,
                "font": "SinsGold",
                "size": 24
            }
        )

    def update(self, **kwargs):
        self.menu.update(im = self.inputmanager)

    def draw(self, **kwargs):
        write(self.screen, (conf.game.center[0], conf.game.center[1] - 50), "LaserGame",
              antialias = False, font = "EndlessBossBattleRegular", size = 24, align = "center")
        self.menu.draw()


pygame.quit()
