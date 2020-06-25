import random

import pygame

from digicolor import colors

from lasergame.classes.inputlistener import InputListener
from lasergame.lib import nygame
from lasergame.lib.conf import game
from lasergame.lib.gamemanager import GameManager
from lasergame.lib.pgutils import write
from lasergame.objects.box import Box
from lasergame.objects.controller import Controller
from lasergame.objects.framegraph import FrameGraph
from lasergame.objects.ship import Ship
from lasergame.objects.star import Star


def gameloop():
    pygame.init()

    clock = nygame.time.Clock()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))
    debugscreen = pygame.Surface((game.windowwidth, game.windowheight), flags=pygame.SRCALPHA)

    gm = GameManager()

    # Pixel-scale the screen up to something seeable on a monitor.
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    # Window title.
    pygame.display.set_caption("LaserGame v0 by DigiSoft")

    # Draw stars?
    for i in range(150):
        center = (random.randint(0, game.width), random.randint(0, game.height))
        gm.add(Star(center))

    # Add objects to the GameManager.
    gm.add(InputListener())
    gm.add(Ship(20, 25, game.center, 90, colors.BLUE.rgb, bulletrate=100))
    gm.add(Box((game.center[0] + 100, game.center[1])))
    gm.add(Controller())
    gm.add(FrameGraph())

    def refresh():
        # Create debug information.
        if gm.state.debug:
            write(debugscreen, (-8, 8 + 61), f"{clock.get_fps():0.2f}", color=colors.LIGHT_GREEN.rgb)
            write(debugscreen, (-8, 24 + 61), f"{len(gm)} objects", color=colors.LIGHT_GREEN.rgb)
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        # Show debug screen.
        bigscreen.blit(debugscreen, (0, 0))
        pygame.display.flip()

    running = True

    while running:
        # Window close button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Update objects
        gm.update(clock=clock, events=events, screen=screen)
        gm.collide()

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        debugscreen.fill((0, 0, 0, 0))

        # Draw objects
        gm.draw(screen = screen, debugscreen = debugscreen)

        refresh()
        clock.tick_busy_loop(game.framerate)


pygame.quit()
