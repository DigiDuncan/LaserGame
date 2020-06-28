from lasergame.classes.abc import Drawable, Updateable


# A class that should be both an Updateable and a Drawable
class BothClass:
    def update(self):
        pass

    def draw(self):
        pass


# A class that should be an Updateable but not a Drawable
class UpdateClass:
    def update(self):
        pass


# A class that should be a Drawable but not an Updateable
class DrawClass:
    def draw(self):
        pass


# A class that should be neither an Updateable or a Drawable
class NoneClass:
    pass


def test_drawable_class():
    assert issubclass(NoneClass, Drawable) is False
    assert issubclass(DrawClass, Drawable) is True
    assert issubclass(UpdateClass, Drawable) is False
    assert issubclass(BothClass, Drawable) is True


def test_updateable_class():
    assert issubclass(NoneClass, Updateable) is False
    assert issubclass(DrawClass, Updateable) is False
    assert issubclass(UpdateClass, Updateable) is True
    assert issubclass(BothClass, Updateable) is True


def test_drawable_instance():
    assert isinstance(NoneClass(), Drawable) is False
    assert isinstance(DrawClass(), Drawable) is True
    assert isinstance(UpdateClass(), Drawable) is False
    assert isinstance(BothClass(), Drawable) is True


def test_updateable_instance():
    assert isinstance(NoneClass(), Updateable) is False
    assert isinstance(DrawClass(), Updateable) is False
    assert isinstance(UpdateClass(), Updateable) is True
    assert isinstance(BothClass(), Updateable) is True
