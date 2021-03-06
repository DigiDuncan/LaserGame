import pygame

from digicolor import colors

from lasergame.classes.collidablegameobject import CollidableGameObject
from lasergame.lib.constants import game, zlayer
from lasergame.lib.nygame import time
from lasergame.lib.pgutils import draw_triangle, play_sound
from lasergame.lib.utils import clamp
from lasergame.objects.projectiles.bullet import Bullet, bullettypes

from lasergame.objects.star import Star


class Ship(CollidableGameObject):
    __slots__ = ["width", "height", "color", "speed", "direction", "bulletrate", "_lastbullet", "_weaponselectindex"]

    directions = ["right", "down", "left", "up"]

    def __init__(self, width: int, height: int, center: tuple, speed, color: tuple = colors.WHITE.rgb, bulletrate = 10):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.direction = 0
        self.bulletrate = bulletrate
        self._lastbullet = 0
        self._weaponselectindex = 0
        super().__init__(center=center, z=zlayer.SHIP)

    @property
    def x(self):
        return self.center[0]

    @x.setter
    def x(self, value):
        value = clamp(0, value, game.width)
        self.center = (value, self.center[1])

    @property
    def y(self):
        return self.center[1]

    @y.setter
    def y(self, value):
        value = clamp(0, value, game.height)
        self.center = (self.center[0], value)

    @property
    def weaponselect(self):
        return list(bullettypes.keys())[self._weaponselectindex]

    def rotate_right(self):
        self.direction = (self.direction + 1) % 4

    def rotate_left(self):
        self.direction = (self.direction - 1) % 4

    @property
    def left(self):
        return self.x - int(self.width / 2)

    @property
    def top(self):
        return self.y - int(self.width / 2)

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height

    @property
    def collision_box(self):
        # return pygame.Rect(self.left, self.top, self.width, self.height)
        size = 6
        return pygame.Rect(self.x - (size / 2), self.y - (size / 2), size, size)

    @property
    def uuid_offset(self):
        return (self.width / 2) + 2

    def update(self, clock, gm, **kwargs):
        collisions = gm.collisions[self]
        for other in collisions:
            if isinstance(other, Bullet) and other.owner != self.uuid:
                gm.state.health -= 1
                play_sound(f"laser-7", 0)
                gm.discard(other)

        if gm.input.UP.held:
            self.y -= self.speed * clock.get_time_secs()
        if gm.input.DOWN.held:
            self.y += self.speed * clock.get_time_secs()
        if gm.input.LEFT.held:
            self.x -= self.speed * clock.get_time_secs()
        if gm.input.RIGHT.held:
            self.x += self.speed * clock.get_time_secs()

        if gm.input.A.held:
            if self._lastbullet + (1 / self.bulletrate) < time.get_ticks_sec():
                gm.add(Bullet((self.x + (self.height / 2), self.y), 90, owner = self.uuid, bullettype = self.weaponselect))
                play_sound(f"laser-{self._weaponselectindex + 1}", 0)
                self._lastbullet = time.get_ticks_sec()
        if gm.input.L.pressed:
            self._weaponselectindex = (self._weaponselectindex - 1) % len(bullettypes)
        elif gm.input.R.pressed:
            self._weaponselectindex = (self._weaponselectindex + 1) % len(bullettypes)
        elif gm.input.B.pressed:
            gm.add(Star(self.safecenter))

        super().update(gm=gm)

    def draw(self, screen, debugscreen, **kwargs):
        draw_triangle(screen, self.color, self.center, self.width, self.height, self.directions[self.direction])
        pygame.draw.circle(screen, bullettypes[self.weaponselect]["color"], self.safecenter, 2)
        super().draw(debugscreen = debugscreen)
        # return collision_box
        return pygame.Rect(self.x, self.y, 1, 1)
