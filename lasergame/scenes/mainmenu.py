import pygame

from digicolor import colors

from lasergame.lib import conf
# from lasergame.lib.gamemanager import GameManager
from lasergame.lib.pgutils import draw_triangle, write
# from lasergame.scenes.gameloop import GameLoop

selector_x_offset = 85


class MainMenu:
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.bigscreen = game.bigscreen
        self.inputmanager = game.im
        self.options = ["start", "exit", "fake"]
        # self.center = center
        # self.items = items
        self.selected = 0

    def refresh(self):
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(self.screen, (conf.game.windowwidth, conf.game.windowheight), self.bigscreen)
        # Show debug screen.
        pygame.display.flip()

    def draw(self):
        self.screen.fill(colors.BLACK.rgb)
        write(self.screen, (conf.game.center[0], conf.game.center[1] - 50), "LaserGame", align = "center", size = 32, font = "EndlessBossBattleRegular.ttf", antialias = False)
        write(self.screen, conf.game.center, "START GAME", align = "center", size = 9, font = "OldSchoolAdventures.ttf", antialias = False)
        write(self.screen, (conf.game.center[0], conf.game.center[1] + 20), "EXIT TO DESKTOP", align = "center", size = 9, font = "OldSchoolAdventures.ttf", antialias = False)
        draw_triangle(self.screen, colors.WHITE.rgb, (conf.game.center[0] - selector_x_offset, conf.game.center[1] + 5 + (20 * self.selected)), 8, 8)

    def update(self, events):
        if self.inputmanager.UP.pressed:
            self.selected -= 1
        elif self.inputmanager.DOWN.pressed:
            self.selected += 1
        self.selected = self.selected % len(self.options)
        if self.inputmanager.START.pressed:
            if self.options[self.selected] == "start":
                # Start the game.
                self.game.switch_scene("gameloop")
            elif self.options[self.selected] == "exit":
                # Exit to desktop.
                self.game.quit()


class MenuItem:
    def __init__(self, name, text, function):
        self.name = name
        self.text = text
        self.function = function


pygame.quit()
