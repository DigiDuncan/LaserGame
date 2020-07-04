import pygame

from lasergame.lib import sounds


def test_sounds():
    pygame.mixer.init()
    sound = sounds.get("laser-1")
    assert sound is not None
