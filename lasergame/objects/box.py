from digicolor import colors

from lasergame.lib.pgutils import write, draw_box
from lasergame.objects.bullet import Bullet
from lasergame.objects.collidablegameobject import CollidableGameObject


class Box(CollidableGameObject):
    __slots__ = ["center", "width", "height", "color", "_hits"]

    def __init__(self, center: tuple, width = 25, height = 25, color = colors.CYAN.rgb):
        self.color = color
        self.width = width
        self.height = height
        self._hits = 0
        super().__init__(center=center, z=1)

    def update(self, **kwargs):
        pass

    def draw(self, screen, **kwargs):
        self.boundingBox = draw_box(screen, self.center, self.width, self.height, color = self.color)
        write(screen, (self.center[0], self.center[1] - 8), str(self._hits), align = "center")
        return self.boundingBox

    def collide(self, other, **kwargs):
        if isinstance(other, Bullet):
            if self.boundingBox is None or other.boundingBox is None:
                return
            if self.boundingBox.colliderect(other.boundingBox):
                self._hits += 1
