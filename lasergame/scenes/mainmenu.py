import math
import random

import pygame

from digicolor import colors

from lasergame.classes.menu import Menu, SceneMenuItem, QuitMenuItem
from lasergame.lib import conf, nygame
from lasergame.lib.pgutils import write

splashtexts = [
    "Splash text!",
    "Destroy them with lasers!",
    "Straight out of 1990!",
    "No Digi prefix!",
    "Super Nintendo, Sega Genesis!",
    "Natalie helped!",
    "Not on Switch (yet!)",
    "Not on Steam (yet!)",
    "Always aliased!"
]


class MainMenu:
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.bigscreen = game.bigscreen
        self.inputmanager = game.im
        self.items = [
            SceneMenuItem(self.game, "start", "START GAME", scene = "gameloop"),
            SceneMenuItem(self.game, "options", "OPTIONS", scene = "optionsmenu"),
            QuitMenuItem(self.game, "quit", "QUIT TO DESKTOP")
        ]
        self.menu = Menu(
            self.screen, (conf.game.center[0], conf.game.center[1] + 25), self.items, cursorsettings = {
                "color": colors.WHITE.rgb,
                "width": 8,
                "height": 8,
                "direction": "right"
            },
            fontsettings = {
                "color": colors.WHITE.rgb,
                "align": "center",
                "antialias": False,
                "font": "SinsGold.ttf",
                "size": 24
            }
        )
        self.splash = write(self.screen, (conf.game.center[0], conf.game.center[1] - 25), "SPLASH TEXT!",
                            antialias = False, font = "SinsGold.ttf", size = 16, align = "center",
                            color = colors.LIGHT_CYAN.rgb, blit = False)
        self.splashtext = random.choice(splashtexts).upper()

    @property
    def splashrot(self):
        return (1.5 * math.sin(5 * nygame.time.get_ticks_sec())) * 2.5

    def update(self, **kwargs):
        self.menu.update(im = self.inputmanager)
        self.splash = write(self.screen, (conf.game.center[0], conf.game.center[1] - 25), self.splashtext,
                            antialias = False, font = "SinsGold.ttf", size = 16, align = "center",
                            color = colors.LIGHT_CYAN.rgb, blit = False)
        self.splash["surface"] = pygame.transform.rotate(self.splash["surface"], self.splashrot)

    def draw(self, **kwargs):
        write(self.screen, (conf.game.center[0], conf.game.center[1] - 50), "LaserGame",
              antialias = False, font = "EndlessBossBattleRegular.ttf", size = 24, align = "center")
        self.menu.draw()
        self.screen.blit(self.splash["surface"], self.splash["coords"])


pygame.quit()
