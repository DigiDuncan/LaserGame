import pygame

from digicolor import colors

from lasergame.lib import nygame
from lasergame.lib.conf import game
# from lasergame.lib.gamemanager import GameManager
from lasergame.lib.pgutils import draw_triangle, write
from lasergame.procedures.gameloop import gameloop

options = ["start", "exit"]
selected = 0


def mainmenu(bigscreen: pygame.Surface):
    global selected
    selector_x_offset = 85

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
        write(screen, (game.center[0], game.center[1] - 50), "LaserGame", align = "center", size = 32, font = "EndlessBossBattleRegular.ttf", antialias = False)
        write(screen, game.center, "START GAME", align = "center", size = 9, font = "OldSchoolAdventures.ttf", antialias = False)
        write(screen, (game.center[0], game.center[1] + 20), "EXIT TO DESKTOP", align = "center", size = 9, font = "OldSchoolAdventures.ttf", antialias = False)
        draw_triangle(screen, colors.WHITE.rgb, (game.center[0] - selector_x_offset, game.center[1] + 5 + (20 * selected)), 8, 8)

    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    if selected == 0:
                        selected = 1
                    else:
                        selected = 0
                if event.key == pygame.K_RETURN:
                    if options[selected] == "start":
                        gameloop(bigscreen)
                    elif options[selected] == "exit":
                        running = False
                    return

        draw()
        refresh()
        clock.tick_busy_loop(game.framerate)


pygame.quit()
