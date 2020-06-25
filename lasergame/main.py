import pygame

from lasergame.lib.conf import game
from lasergame.procedures.gameloop import gameloop


def main():
    bigscreen = pygame.display.set_mode([game.windowwidth, game.windowheight])
    # Window title.
    pygame.display.set_caption("LaserGame v0 by DigiSoft")

    gameloop(bigscreen)


# This is needed, or else calling `python -m <name>` will mean that main() is called twice.
if __name__ == "__main__":
    main()
