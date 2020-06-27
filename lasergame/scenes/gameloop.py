import random

import pygame

from digicolor import colors

from lasergame.classes.inputlistener import InputListener
from lasergame.lib import conf
from lasergame.lib.gamemanager import GameManager
from lasergame.lib.pgutils import write
from lasergame.objects.box import Box
from lasergame.objects.controller import Controller
from lasergame.objects.framegraph import FrameGraph
from lasergame.objects.ship import Ship
from lasergame.objects.star import Star


class GameLoop():
    def __init__(self, *, game):
        self.game = game
        self.screen = game.screen
        self.debugscreen = game.debugscreen
        self.clock = game.clock
        self.gm = GameManager(inputmanager = game.im)

        # Draw stars?
        for i in range(150):
            center = (random.randint(0, conf.game.width), random.randint(0, conf.game.height))
            self.gm.add(Star(center))

        # Add objects to the GameManager.
        self.gm.add(InputListener())
        self.gm.add(Ship(20, 25, conf.game.center, 90, colors.BLUE.rgb, bulletrate=10))
        self.gm.add(Box((conf.game.center[0] + 100, conf.game.center[1])))
        self.gm.add(Controller())
        self.gm.add(FrameGraph())

    def update(self, events):
        if self.gm.input.START.pressed:
            self.game.pause()
            return
        # Update objects
        self.gm.update(clock=self.clock, events=events, screen=self.screen)

        self.gm.collide()

    def draw(self):
        # Draw objects
        self.gm.draw(screen = self.screen, debugscreen = self.debugscreen)
        # Create debug information.
        if self.gm.state.debug:
            write(self.debugscreen, (-8, 8 + 61), f"{self.clock.get_fps():0.2f}", color=colors.LIGHT_GREEN.rgb)
            write(self.debugscreen, (-8, 24 + 61), f"{len(self.gm)} objects", color=colors.LIGHT_GREEN.rgb)


pygame.quit()
