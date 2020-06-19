import pygame
import random

from digicolor import colors


from lasergame.lib import nygame
from lasergame.lib.constants import game
from lasergame.objects.ship import Ship
from lasergame.objects.star import Star


def write(screen, coords, text, *, color=colors.WHITE.rgb):
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    textsurface = font.render(text, True, color)
    if coords[0] < 0:
        coords = (screen.get_width() + coords[0] - textsurface.get_width(), coords[1])
    if coords[1] < 0:
        coords = (coords[0], screen.get_height() + coords[1] - textsurface.get_height())
    screen.blit(textsurface, coords)


def gameloop():
    pygame.init()

    clock = nygame.time.Clock()

    # Create the screen.
    screen = pygame.Surface((game.width, game.height))
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    pygame.display.set_caption("LaserGame v0 by DigiDuncan")

    gameObjects = []

    # Draw stars?
    for i in range(150):
        gameObjects.append(Star(random.randint(0, game.width), random.randint(0, game.height)))

    gameObjects.append(Ship(20, 25, game.center, 90, colors.BLUE.rgb))

    def refresh():
        # Pixel-scale the screen to the bigscreen and flip [refresh?] the display
        pygame.transform.scale(screen, (game.windowwidth, game.windowheight), bigscreen)
        write(bigscreen, (-8, 8), f"{clock.get_fps():0.2f}", color=colors.LIGHT_GREEN.rgb)
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
            o.update(events=events, clock=clock)

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # Draw objects
        for o in gameObjects:
            o.draw(screen)

        refresh()
        clock.tick_busy_loop(60)


pygame.quit()
