from lasergame.classes.gameobject import GameObject


class CollidableGameObject(GameObject):
    @property
    def uuid_offset(self):
        return 0

    @property
    def collision_box(self):
        return None

    def update(self, gm, **kwargs):
        self.showuuid = gm.input.SELECT.held and gm.state.debug

    def collide(self, other, **kwargs):
        pass

    def draw(self, debugscreen, **kwargs):
        self.draw_uuid(debugscreen, self.uuid_offset)
