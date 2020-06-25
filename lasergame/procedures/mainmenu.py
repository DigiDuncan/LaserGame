import pygame

from digicolor import colors

from lasergame.lib import nygame
from lasergame.lib.conf import game
# from lasergame.lib.gamemanager import GameManager
from lasergame.lib.pgutils import write
from lasergame.procedures.gameloop import gameloop


def mainmenu(bigscreen: pygame.Surface):
    pygame.init()

    clock = nygame.time.Clock()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))

    # TODO: Use GameManager for input detection.
    # gm = GameManager()

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        # Show debug screen.
        pygame.display.flip()

    def draw():
        screen.fill(colors.BLACK.rgb)
        write(screen, (game.center[0], game.center[1] - 30), "LaserGame", align = "center", size = 20)
        write(screen, game.center, "Press START", align = "center", size = 12)

    running = True

    while running:
        # Window close button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop(bigscreen)
                    return

        draw()
        refresh()
        clock.tick_busy_loop(game.framerate)


pygame.quit()
