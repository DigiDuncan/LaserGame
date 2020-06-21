from pygame import locals as pygame_locals
import pygame

from lasergame.lib.constants import buttons as button_constants


class ButtonState:
    __slots__ = ["name", "key_code", "pressed", "released", "held"]

    def __init__(self, name, key_code):
        self.clear()
        self.name = name
        self.key_code = key_code

    def clear(self):
        self.pressed = False
        self.released = False
        self.held = False


class InputManager:
    __slots__ = ["UP", "LEFT", "RIGHT", "DOWN", "A", "B", "X", "Y", "L", "R", "SELECT", "START", "keycodes_to_buttons"]

    def __init__(self):
        self.keycodes_to_buttons = {}
        for name, pygame_key in button_constants.items():
            keycode = getattr(pygame_locals, pygame_key)
            button = ButtonState(name, keycode)
            setattr(self, name, button)
            self.keycodes_to_buttons[keycode] = button

    def clear(self):
        for button in self.keycodes_to_buttons.values():
            button.clear()

    def __getitem__(self, keycode):
        return self.keycodes_to_buttons[keycode]

    def __iter__(self):
        return iter(self.keycodes_to_buttons)

    @property
    def keycodes(self):
        return self.keycodes_to_buttons.keys()

    @property
    def buttons(self):
        return self.keycodes_to_buttons.values()

    def update(self, events):
        self.clear()

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key in self.keycodes:
                    self[e.key].pressed = True
            elif e.type == pygame.KEYUP:
                if e.key in self.keycodes:
                    self[e.key].released = True

        pygame_pressed = pygame.key.get_pressed()
        for keycode in self.keycodes:
            self[keycode].held = pygame_pressed[keycode]
