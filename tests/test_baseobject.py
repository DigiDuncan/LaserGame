from lasergame.classes.baseobject import BaseObject


def test_w():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.w == 5


def test_h():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.h == 11


def test_width():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.width == 5


def test_height():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.height == 11


def test_size():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.size == (5, 11)


def test_x():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.x == 1


def test_y():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.y == 3


def test_left():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.left == 1


def test_centerx():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.centerx == int(1 + (5 / 2))


def test_right():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.right == 1 + 5


def test_top():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.top == 3


def test_centery():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.centery == int(3 + (11 / 2))


def test_bottom():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.bottom == 3 + 11


def test_topleft():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.topleft == (1, 3)


def test_midtop():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.midtop == (int(1 + (5 / 2)), 3)


def test_topright():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.topright == (1 + 5, 3)


def test_midleft():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.midleft == (1, int(3 + (11 / 2)))


def test_center():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.center == (int(1 + (5 / 2)), int(3 + (11 / 2)))


def test_midright():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.midright == (1 + 5, int(3 + (11 / 2)))


def test_bottomleft():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.bottomleft == (1, 3 + 11)


def test_midbottom():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.midbottom == (int(1 + (5 / 2)), 3 + 11)


def test_bottomright():
    bo = BaseObject(w=5, h=11, x=1, y=3)
    assert bo.bottomright == (1 + 5, 3 + 11)
