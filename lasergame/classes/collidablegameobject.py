from lasergame.classes.gameobject import GameObject


class CollidableGameObject(GameObject):
    def __init__(self, **kwargs):
        self.boundingBox = None
        super().__init__(**kwargs)

    def update(self, gm, **kwargs):
        self.showuuid = gm.input.SELECT.held and gm.state.debug

    def collide(self, other, **kwargs):
        pass
