import pygame
from pygame import locals

import digicolor

from lasergame.lib.attrdict import AttrDict
from lasergame.lib.constants import game
from lasergame.lib.constants import buttons as keys

colors = digicolor.colors
buttonsdict = {}
for k, v in keys._values.items():
    buttonsdict[k] = getattr(locals, v)
buttons = AttrDict(buttonsdict)


def gameloop():
    pygame.init()

    # Create the screen.
    screen = pygame.display.set_mode([game.width, game.height])

    running = True

    while running:
        # Window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Fill the background with white
        screen.fill(colors.BLACK.rgb)

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (game.center[0], game.center[1]), 75)

        # Flip [refresh?] the display
        pygame.display.flip()


pygame.quit()
