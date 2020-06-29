from lasergame.classes.abc import Drawable, Updateable, Collidable


# A class that should be Updateable, Drawable, and Collidable
class AllClass:
    def update(self):
        pass

    def draw(self):
        pass

    @property
    def collision_box(self):
        pass


# A class that should be an Updateable but not a Drawable or Collidable
class UpdateClass:
    def update(self):
        pass


# A class that should be a Drawable but not an Updateable or Collidable
class DrawClass:
    def draw(self):
        pass


# A class that should be a Collidable but not an Updateable or Drawable
class CollideClass:
    @property
    def collision_box(self):
        pass


# A class that should be neither an Updateable, Drawable, or Collidable
class NoneClass:
    pass


def test_drawable_class():
    assert issubclass(NoneClass, Drawable) is False
    assert issubclass(DrawClass, Drawable) is True
    assert issubclass(UpdateClass, Drawable) is False
    assert issubclass(CollideClass, Drawable) is False
    assert issubclass(AllClass, Drawable) is True


def test_drawable_instance():
    assert isinstance(NoneClass(), Drawable) is False
    assert isinstance(DrawClass(), Drawable) is True
    assert isinstance(UpdateClass(), Drawable) is False
    assert isinstance(CollideClass(), Drawable) is False
    assert isinstance(AllClass(), Drawable) is True


def test_updateable_class():
    assert issubclass(NoneClass, Updateable) is False
    assert issubclass(DrawClass, Updateable) is False
    assert issubclass(UpdateClass, Updateable) is True
    assert issubclass(CollideClass, Updateable) is False
    assert issubclass(AllClass, Updateable) is True


def test_updateable_instance():
    assert isinstance(NoneClass(), Updateable) is False
    assert isinstance(DrawClass(), Updateable) is False
    assert isinstance(UpdateClass(), Updateable) is True
    assert isinstance(CollideClass(), Updateable) is False
    assert isinstance(AllClass(), Updateable) is True


def test_collidable_class():
    assert issubclass(NoneClass, Collidable) is False
    assert issubclass(DrawClass, Collidable) is False
    assert issubclass(UpdateClass, Collidable) is False
    assert issubclass(CollideClass, Collidable) is True
    assert issubclass(AllClass, Collidable) is True


def test_collidable_instance():
    assert isinstance(NoneClass(), Collidable) is False
    assert isinstance(DrawClass(), Collidable) is False
    assert isinstance(UpdateClass(), Collidable) is False
    assert isinstance(CollideClass(), Collidable) is True
    assert isinstance(AllClass(), Collidable) is True
