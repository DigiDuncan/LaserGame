import uuid

from digicolor import colors

from lasergame.lib.pgutils import write
from lasergame.lib.conf import game


class GameObject:
    __slots__ = ["center", "z", "uuid", "showuuid"]

    def __init__(self, center=(0, 0), z=0):
        self.center = center
        self.z = z
        self.uuid = uuid.uuid4()
        self.showuuid = False

    def update(self, **kwargs):
        pass

    def draw(self, screen, **kwargs):
        pass

    @property
    def x(self):
        return self.center[0]

    @x.setter
    def x(self, value):
        self.center = (value, self.center[1])

    @property
    def y(self):
        return self.center[1]

    @y.setter
    def y(self, value):
        self.center = (self.center[0], value)

    def draw_uuid(self, screen, yoffset = 0):
        if self.showuuid:
            write(screen, (self.center[0] * game.scale, self.center[1] * game.scale - yoffset), (str(self.uuid)[:8] + "..."), align = "center", color = colors.CYAN.rgb, antialias = False)
