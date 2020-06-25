import pygame

from lasergame.classes.gameobject import GameObject
from lasergame.lib.conf import game
from lasergame.lib.utils import clamp


colorlist = []
for i in range(61):
    r = 0
    g = 0
    if i < 30:
        r = 255
        g = int(255 / 30 * i)
    if 61 > i >= 30:
        r = int(255 / 30 * (30 - (i - 30)))
        g = 255
    if i == 61:
        r = 0
        g = 255
    colorlist.append((r, g, 0))


class FrameGraph(GameObject):
    __slots__ = ["_fps", "show", "surface"]

    def __init__(self):
        self._fps = 60
        self.show = False
        self.surface = pygame.Surface((100, 61), flags=pygame.SRCALPHA)
        super().__init__()

    @property
    def color(self):
        return colorlist[clamp(0, self._fps, 60)]

    def update(self, gm, clock, **kwargs):
        self.show = gm.state.debug
        self._fps = int(clock.get_fps())

    def draw(self, debugscreen, **kwargs):
        if not self.show:
            return
        if not self.color:
            return
        self.surface.scroll(dx=-1)
        for i in range(61):
            self.surface.set_at((99, i), (0, 0, 0, 0))
        self.surface.set_at((99, (60 - self._fps)), self.color)

        debugscreen.blit(self.surface, (game.windowwidth - self.surface.get_width(), 0))
