from lasergame.classes.gameobject import GameObject
from lasergame.lib.constants import zlayer
from lasergame.lib.pgutils import write


class Score(GameObject):

    def __init__(self):
        self.score = 0
        super().__init__(z=zlayer.TEXT)

    def update(self, gm, events, **kwargs):
        self.score = gm.state.score

    def draw(self, screen, **kwargs):
        write(screen, (screen.get_width() / 2, 0), self.score, halign = "center", valign = "top", font = "m5x7")
