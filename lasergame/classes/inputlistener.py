from lasergame.classes.gameobject import GameObject


class InputListener(GameObject):
    __slots__ = []

    def update(self, gm, events, **kwargs):
        if (gm.input.SELECT.pressed or gm.input.START.pressed) and (gm.input.SELECT.held and gm.input.START.held):
            gm.state.debug = not gm.state.debug
