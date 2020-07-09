import re

import pygame
from pygame import locals as pygame_locals

from lasergame.lib.constants import buttons as button_constants


RE_VALID_ACTION_NAME = re.compile(r"^[A-Z][A-Z0-9_]*$")


class ActionState:
    __slots__ = ["name", "keycodes", "exclusive_groups", "pressed", "released", "held"]

    def __init__(self, name):
        self.name = name
        self.keycodes = set()
        self.exclusive_groups = set()
        self.pressed = False
        self.released = False
        self.held = False

    def reset(self):
        self.pressed = False
        self.released = False
        self.held = False


# "UP", "LEFT", "RIGHT", "DOWN", "A", "B", "X", "Y", "L", "R", "SELECT", "START", "FULLSCREEN", "WINDOW",
class InputManager:
    """Maps keycodes to actions

    Each keycode can be mapped to at most one action. If you try to map the same keycode to another action, the old mapping will be removed.
    Each action can be mapped to multiple keycodes. As long as at least one of the mapped keycodes are pressed, the action will be triggered.

    Certain actions can be set to be exclusive to each other. If multiple exclusive actions are held at the same time, they will be considered invalid and ignored.
    """
    __slots__ = ["actions", "keycodes", "exclusive_action_groups"]

    def __init__(self):
        self.actions = {}
        self.keycodes = {}
        self.exclusive_action_groups = set()

    def _createOrGetAction(self, name):
        if not RE_VALID_ACTION_NAME.match(name):
            raise ValueError(f"Invalid action name: {name}")
        if name not in self.actions:
            self.actions[name] = ActionState(name)
        return self.actions[name]

    def _removeIfUnusedAction(self, name):
        # If this action is not mapped to a keycode, remove it
        action = self.actions[name]
        if not action.keycodes:
            # Remove it from any exclusive groups it may be in
            for ex in list(action.exclusive_groups):
                self.unset_exclusive([action.name for action in ex])
                new_ex = list(ex)
                new_ex.remove(action)
                if len(new_ex) > 1:
                    self.set_exclusive(new_ex)
            # Remove it from the self.actions dictionary
            del self.actions[name]

    def map(self, action, keycode):
        """Map a keycode to an action

        Valid action names consist of the characters [A-Z0-9_] and the first character must be [A-Z].
        """
        if keycode in self.keycodes:
            self.unmap_keycode(keycode)
        action_state = self._createOrGetAction(action)
        action_state.keycodes.add(keycode)
        self.keycodes[keycode] = action_state

    def unmap_action(self, action):
        """Remove all mappings for this action"""
        for keycode in list(self.actions[action].keycodes):
            self.unmap(keycode)

    def unmap(self, keycode):
        """Remove a single keycode input mapping"""
        action = self.keycodes[keycode]
        action.keycodes.remove(keycode)
        del self.keycodes[keycode]
        self._removeIfUnusedAction(action.name)

    def clear_map(self):
        """Remove all input mappings"""
        self.actions.clear()
        self.keycodes.clear()
        self.exclusive_action_groups.clear()

    def set_exclusive(self, actions):
        """Set multiple actions to be exclusive

        If more than one of these actions are held at the same time, all actions in the group are ignored.
        """
        action_states = frozenset(self.actions[name] for name in actions)
        for action_state in action_states:
            action_state.exclusive_groups.add(action_states)
        self.exclusive_action_groups.add(action_states)

    def unset_exclusive(self, actions):
        """Remove a set of exclusive actions"""
        action_states = frozenset(self.actions[name] for name in actions)
        for action_state in action_states:
            action_state.exclusive_groups.remove(action_states)
        self.exclusive_action_groups.remove(action_states)

    def update(self, events):
        # Reset all actions
        for action in self.actions.values():
            action.reset()

        # Set all pressed and released actions
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key in self.keycodes:
                    action = self.keycodes[e.key]
                    action.pressed = True
            elif e.type == pygame.KEYUP:
                if e.key in self.keycodes:
                    action = self.keycodes[e.key]
                    action.released = True

        # Set all held actions
        pygame_pressed = pygame.key.get_pressed()
        for keycode in self.keycodes:
            action = self.keycodes[keycode]
            action.held = pygame_pressed[keycode]

        # Check each exclusive action group to see if multiple actions have been triggered
        exclusive_actions_to_reset = set()
        for ex in self.exclusive_action_groups:
            held_count = 0
            for action in ex:
                if action.held:
                    held_count += 1
                if held_count > 1:
                    # If multiple actions have triggered, the add all exclusive group actions to the list of actions that need to be reset
                    exclusive_actions_to_reset.update(ex)
                    break

        # Reset any actions that are breaking exclusive action group rules
        for action in exclusive_actions_to_reset:
            action.held = False

    def load(self):
        # TODO: Replace this with a more generic load method
        self.clear_map()
        for action, pygame_key in button_constants.items():
            keycode = getattr(pygame_locals, pygame_key)
            self.map(action, keycode)
        self.set_exclusive(("UP", "DOWN"))
        self.set_exclusive(("LEFT", "RIGHT"))

    def __getattr__(self, name):
        try:
            return self.actions[name]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
