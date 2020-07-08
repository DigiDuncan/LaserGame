import pygame

from digicolor import colors

from lasergame.classes.menu import Menu, SceneMenuItem, PlaceholderMenuItem
from lasergame.lib import conf
from lasergame.lib.pgutils import write


class TestMenu:
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.inputmanager = game.im
        self.items = [
            SceneMenuItem(self.game, "back", "BACK TO MAIN MENU", scene = "mainmenu"),
            PlaceholderMenuItem(self.game, "p1", "PLACEHOLDER 1"),
            PlaceholderMenuItem(self.game, "p2", "PLACEHOLDER 2"),
            PlaceholderMenuItem(self.game, "p3", "PLACEHOLDER 3"),
            PlaceholderMenuItem(self.game, "p4", "PLACEHOLDER 4"),
            PlaceholderMenuItem(self.game, "p5", "PLACEHOLDER 5")
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
