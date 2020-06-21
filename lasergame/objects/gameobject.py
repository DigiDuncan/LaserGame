import uuid

from lasergame.lib.pgutils import write


class GameObject:
    def __init__(self, center=(0, 0), z=0):
        self.center = center
        self.z = z
        self.uuid = uuid.uuid4()

    def update(self, **kwargs):
        pass

    def draw(self, screen):
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

    def draw_uuid(self, screen):
        write(screen, (self.center[0], self.center[1] - 8), (str(self.uuid)[:8] + "..."), size = 8)
