import importlib.resources as pkg_resources
import math
import random

import pygame

from digicolor import colors

import lasergame.data
from lasergame.classes.menu import Menu, SceneMenuItem, QuitMenuItem
from lasergame.lib import conf, nygame
from lasergame.lib.assets import images
from lasergame.lib.pgutils import write, render_text, blit


splashtexts = pkg_resources.read_text(lasergame.data, "splashes.txt").splitlines()


class MainMenu(Menu):
    __slots__ = ["splashtext", "logo"]

    def __init__(self, *, game):
        self.splashtext = random.choice(splashtexts).upper()
        self.logo = images.get("digisoft-small")
        x, y = conf.game.center
        coords = x, y + 30
        super().__init__(
            game,
            coords,
            items = [
                SceneMenuItem(game, "start", "START GAME", scene = "gameloop"),
                SceneMenuItem(game, "options", "OPTIONS", scene = "optionsmenu"),
                SceneMenuItem(game, "test", "TEST MENU", scene = "testmenu"),
                QuitMenuItem(game, "quit", "QUIT TO DESKTOP")
            ],
            cursorsettings = {
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

    def draw(self, **kwargs):
        super().draw()
        splash = render_text(self.splashtext,
                             antialias = False,
                             font = "SinsGold",
                             size = 16,
                             color = colors.LIGHT_CYAN.rgb)
        splash_rot = (1.5 * math.sin(5 * nygame.time.get_ticks_sec())) * 2.5
        splash = pygame.transform.rotate(splash, splash_rot)
        write(self.screen, (0, -50), "LaserGame",
              antialias = False,
              font = "EndlessBossBattleRegular",
              size = 24,
              halign = "center",
              valign = "center",
              screen_halign = "center",
              screen_valign = "center")
        blit(self.screen, splash, (0, -25),
             halign="center",
             valign = "center",
             screen_halign = "center",
             screen_valign = "center")
        blit(self.screen, self.logo, (0, 0),
             halign="center",
             valign="bottom",
             screen_halign="center",
             screen_valign="bottom")


pygame.quit()
