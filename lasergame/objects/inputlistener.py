import pygame

from lasergame.lib.buttons import buttons
from lasergame.objects.gameobject import GameObject


class InputListener(GameObject):
    def update(self, gm, **kwargs):
        if pygame.key.get_pressed()[buttons.SELECT] and pygame.key.get_pressed()[buttons.START]:
            gm.state.debug = not gm.state.debug

    def draw(self, screen, **kwargs):
        pass
