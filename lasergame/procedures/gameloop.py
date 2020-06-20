import pygame
import random

from digicolor import colors

from lasergame.lib import nygame
from lasergame.lib.constants import game
from lasergame.lib.pgutils import write
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
    # Pixel-scale the screen up to something seeable on a monitor.
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    # Window title.
    pygame.display.set_caption("LaserGame v0 by DigiSoft")

    gameObjects = []

    # Draw stars?
    for i in range(150):
        gameObjects.append(Star(random.randint(0, game.width), random.randint(0, game.height)))

    gameObjects.append(Ship(20, 25, game.center, 90, colors.BLUE.rgb))

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        if game.debug:
            write(bigscreen, (-8, 8), f"{clock.get_fps():0.2f}", color=colors.LIGHT_GREEN.rgb)
            write(bigscreen, (-8, 24), f"{len(gameObjects)} objects", color=colors.LIGHT_GREEN.rgb)
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
        for o in gameObjects:
            o.update(events=events, clock=clock, gameobjects=gameObjects)

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # Draw objects
        for o in gameObjects:
            o.draw(screen)

        refresh()
        clock.tick_busy_loop(game.framerate)


pygame.quit()
