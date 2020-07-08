import pygame
from pygame import locals as pygame_locals

from lasergame.lib.constants import buttons as button_constants
from lasergame.lib.attrdict import AttrDict


class ActionState:
    __slots__ = ["name", "keycodes", "pressed", "released", "held"]

    def __init__(self, name):
        self.name = name
        self.keycodes = set()
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
        self.actions = AttrDict()
        self.keycodes = {}
        self.exclusive_action_groups = []

    def _createOrGetAction(self, action):
        if action not in self.actions:
            self.actions[action] = ActionState(action)
        return self.actions[action]

    def _removeIfUnusedAction(self, action):
        if not self.actions[action].keycodes:
            del self.actions[action]

    def map(self, action, keycode):
        """Map a keycode to an action"""
        if keycode in self.keycodes:
            self.unmap_keycode(keycode)
        action_state = self._createOrGetAction(action)
        action_state.keycodes.add(keycode)
        self.keycodes[keycode] = action_state

    def unmap_action(self, action):
        """Remove all mappings for this action"""
        for keycode in self.actions[action].keycodes:
            self.unmap(keycode)

    def unmap(self, keycode):
        """Remove a single keycode input mapping"""
        action_state = self.keycodes[keycode]
        action_state.keycodes.remove(keycode)
        del self.keycodes[keycode]
        self._removeIfUnusedAction(action_state.name)

    def clear_map(self):
        """Remove all input mappings"""
        self.actions = AttrDict()
        self.keycodes = {}
        self.exclusive_action_groups = []

    def set_exclusive(self, actions):
        """Set multiple actions to be exclusive

        If more than one of these actions are held at the same time, all actions in the group are ignored.
        """
        actions = tuple(sorted(*actions))
        self.exclusive_action_groups.append(actions)

    def unset_exclusive(self, actions):
        """Remove a set of exclusive actions"""
        actions = tuple(sorted(*actions))
        self.exclusive_action_groups.remove(actions)

    def update(self, events):
        # Reset all actions
        for action in self.actions:
            action_state = self.actions[action]
            action_state.reset()

        # Set all pressed and released actions
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key in self.keycodes:
                    action_state = self.keycodes[e.key]
                    action_state.pressed = True
            elif e.type == pygame.KEYUP:
                if e.key in self.keycodes:
                    action_state = self.keycodes[e.key]
                    action_state.released = True

        # Set all held actions
        pygame_pressed = pygame.key.get_pressed()
        for keycode in self.keycodes:
            action_state = self.keycodes[keycode]
            action_state.held = pygame_pressed[keycode]

        # Check each exclusive action group to see if multiple actions have been triggered
        exclusive_actions_to_reset = set()
        for ex in self.exclusive_action_groups:
            held_count = 0
            for action in ex:
                if self.actions[action].held:
                    held_count += 1
                if held_count > 1:
                    # If multiple actions have triggered, the add all exclusive group actions to the list of actions that need to be reset
                    exclusive_actions_to_reset.update(ex)
                    break

        # Reset any actions that are breaking exclusive action group rules
        for action in exclusive_actions_to_reset:
            self.actions[action].held = False

    def load(self):
        # TODO: Replace this with a more generic load method
        self.clear_map()
        for action, pygame_key in button_constants.items():
            keycode = getattr(pygame_locals, pygame_key)
            self.map(action, keycode)
