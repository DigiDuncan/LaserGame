from lasergame.classes.gameobject import GameObject


class InputListener(GameObject):
    __slots__ = []

    def update(self, gm, events, **kwargs):
        # If SELECT and START are pressed, debug toggle.
        if (gm.input.actions.SELECT.pressed or gm.input.actions.START.pressed) and (gm.input.actions.SELECT.held and gm.input.actions.START.held):
            gm.state.debug = not gm.state.debug
