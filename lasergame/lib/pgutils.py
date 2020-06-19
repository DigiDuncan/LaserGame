import pygame

from digicolor import colors


def write(screen, coords, text, *, color=colors.WHITE.rgb):
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    textsurface = font.render(text, True, color)
    if coords[0] < 0:
        coords = (screen.get_width() + coords[0] - textsurface.get_width(), coords[1])
    if coords[1] < 0:
        coords = (coords[0], screen.get_height() + coords[1] - textsurface.get_height())
    screen.blit(textsurface, coords)
