from lasergame.classes.gameobject import GameObject


class CollidableGameObject(GameObject):
    @property
    def collision_box(self):
        return None

    def update(self, gm, **kwargs):
        self.showuuid = gm.input.SELECT.held and gm.state.debug

    def collide(self, other, **kwargs):
        pass
