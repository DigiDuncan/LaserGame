import pygame
from lasergame.lib import nygame

from digicolor import colors

from lasergame.lib import conf
from lasergame.lib.inputmanager import InputManager
from lasergame.lib.pgutils import write
from lasergame.scenes.gameloop import GameLoop
from lasergame.scenes.mainmenu import MainMenu


class Game():
    def __init__(self):
        self.active = None
        self.scenes = {}
        self.running = True
        self.paused = False
        self.clock = nygame.time.Clock()
        self.im = InputManager()

        # Create the screen.
        self.screen = pygame.Surface((conf.game.width, conf.game.height))
        self.bigscreen = pygame.display.set_mode([conf.game.windowwidth, conf.game.windowheight])
        self.debugscreen = pygame.Surface((conf.game.windowwidth, conf.game.windowheight), flags=pygame.SRCALPHA)

    def run(self):
        pygame.init()

        # Window title.
        pygame.display.set_caption("LaserGame v0 by DigiSoft")

        self.scenes = {
            "mainmenu": MainMenu(game = self),
            "gameloop": GameLoop(game = self)
        }
        self.switch_scene("mainmenu")

        while self.running:
            # Window close button
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()

            # Get input
            self.im.update(events=events)
            # Run current scene's update function (or not if we're paused.)
            paused = self.paused
            if not self.paused:
                self.active.update(events=events)
            if paused and self.im.START.pressed:
                self.unpause()
            # Fill the background
            self.screen.fill(colors.BLACK.rgb)
            self.debugscreen.fill((0, 0, 0, 0))
            # Run current scene's draw function
            self.active.draw()
            # Write "PAUSED" on the screen if we're, you know, paused.
            if self.paused:
                write(self.screen, conf.game.center, "PAUSED", align = "center", font = "EndlessBossBattleRegular.ttf", size = 32, antialias = False)
            # Final draw stage
            self.refresh(self.screen, self.bigscreen, self.debugscreen)
            # Timing loop
            self.clock.tick_busy_loop(conf.game.framerate)

    def refresh(self, screen, bigscreen, debugscreen):
        # Pixel-scale the screen to the bigscreen.
        pygame.transform.scale(screen, (conf.game.windowwidth, conf.game.windowheight), bigscreen)
        # Show debug screen.
        bigscreen.blit(debugscreen, (0, 0))
        # Flip [refresh?] the display.
        pygame.display.flip()

    def switch_scene(self, name):
        if self.scenes is None or self.scenes == {}:
            return
        self.active = self.scenes[name]

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def quit(self):
        self.running = False


def main():
    g = Game()
    g.run()


# This is needed, or else calling `python -m <name>` will mean that main() is called twice.
if __name__ == "__main__":
    main()
