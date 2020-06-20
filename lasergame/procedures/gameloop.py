import pygame
import random

from digicolor import colors

from lasergame.lib import nygame
from lasergame.lib.constants import game
from lasergame.lib.pgutils import write
from lasergame.lib.gamemanager import GameManager
from lasergame.procedures import controllerview
from lasergame.objects.ship import Ship
from lasergame.objects.star import Star


def gameloop():
    pygame.init()

    if game.debug:
        controllerview.init()

    clock = nygame.time.Clock()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))

    gm = GameManager(clock)

    # Pixel-scale the screen up to something seeable on a monitor.
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    # Window title.
    pygame.display.set_caption("LaserGame v0 by DigiSoft")

    # Draw stars?
    for i in range(150):
        center = (random.randint(0, game.width), random.randint(0, game.height))
        gm.add(Star(center))

    gm.add(Ship(20, 25, game.center, 90, colors.BLUE.rgb))

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        if game.debug:
            write(bigscreen, (-8, 8), f"{clock.get_fps():0.2f}", color=colors.LIGHT_GREEN.rgb)
            write(bigscreen, (-8, 24), f"{len(gm)} objects", color=colors.LIGHT_GREEN.rgb)
            bigscreen.blit(controllerview.controllersurface(), (0, 0))
        pygame.display.flip()

    running = True

    while running:
        # Window close button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Update objects
        gm.update(events, screen)

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # Draw objects
        gm.draw(screen)

        refresh()
        clock.tick_busy_loop(game.framerate)


pygame.quit()
