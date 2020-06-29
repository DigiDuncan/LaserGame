import pygame

from digicolor import colors

from lasergame.classes.menu import Menu, SceneMenuItem, QuitMenuItem
from lasergame.lib import conf
from lasergame.lib.pgutils import write


class OptionsMenu:
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.bigscreen = game.bigscreen
        self.inputmanager = game.im
        self.items = [
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
                "font": "OldSchoolAdventures.ttf",
                "size": 9
            }
        )

    def refresh(self):
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(self.screen, (conf.game.windowwidth, conf.game.windowheight), self.bigscreen)
        # Show debug screen.
        pygame.display.flip()

    def update(self, **kwargs):
        self.menu.update(im = self.inputmanager)

    def draw(self, **kwargs):
        write(self.screen, (conf.game.center[0], conf.game.center[1] - 50), "LaserGame",
              antialias = False, font = "EndlessBossBattleRegular.ttf", size = 24, align = "center")
        self.menu.draw()


pygame.quit()