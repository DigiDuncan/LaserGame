import pygame
import random

import digicolor

from lasergame.lib.constants import game
from lasergame.objects.ship import Ship
from lasergame.objects.star import Star

colors = digicolor.colors


def gameloop():
    pygame.init()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    pygame.display.set_caption("LaserGame v0 by DigiDuncan")

    gameObjects = []

    # Draw stars?
    for i in range(150):
        gameObjects.append(Star(random.randint(0, game.width), random.randint(0, game.height)))

    gameObjects.append(Ship(20, 25, game.center, colors.BLUE.rgb))

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        pygame.display.flip()

    running = True

    while running:
        # Window close button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            #    if event.key == buttons.UP:
            #        ship.y -= 1

        # Update objects
        for o in gameObjects:
            o.update(events)

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # Draw objects
        for o in gameObjects:
            o.draw(screen)

        refresh()


pygame.quit()
