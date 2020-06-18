import pygame
import random
from pygame import locals

import digicolor

from lasergame.lib.attrdict import AttrDict
from lasergame.lib.constants import game
from lasergame.lib.constants import buttons as keys
from lasergame.objects.ship import Ship

colors = digicolor.colors
buttonsdict = {}
for k, v in keys._values.items():
    buttonsdict[k] = getattr(locals, v)
buttons = AttrDict(buttonsdict)


def gameloop():
    pygame.init()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    pygame.display.set_caption("LaserGame v0 by DigiDuncan")
    ship = Ship(20, 25, game.center, colors.BLUE.rgb)

    # Fill the background
    screen.fill(colors.BLACK.rgb)

    # Draw stars?
    for i in range(150):
        pygame.draw.circle(screen, colors.WHITE.rgb, (random.randint(0, game.width), random.randint(0, game.height)), 2)

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        pygame.display.flip()

    running = True

    while running:
        # Window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.KEYDOWN:
            #    if event.key == buttons.UP:
            #        ship.y -= 1
        if pygame.key.get_pressed()[buttons.UP]:
            ship.y -= 1
        if pygame.key.get_pressed()[buttons.DOWN]:
            ship.y += 1

        # Draw a ship.
        screen.fill(colors.BLACK.rgb)
        ship.draw(screen)

        refresh()


pygame.quit()
