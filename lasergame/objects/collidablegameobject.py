from lasergame.objects.gameobject import GameObject


class CollidableGameObject(GameObject):
    def __init__(self, **kwargs):
        self.boundingBox = None
        super().__init__(**kwargs)

    def collide(self, other, **kwargs):
        pass
