from functools import lru_cache
import importlib
import importlib.resources

import pygame

image_root = "lasergame.data.sounds"
image_ext = "wav"


class SoundNotFoundError(Exception):
    def __init__(self, path):
        super().__init__(f"Unable to load sound: {path!r}")


def parse_path(path):
    subpath, _, filename = path.rpartition(".")
    module_path = image_root
    if subpath:
        module_path += "." + subpath
    filename = f"{filename}.{image_ext}"
    return module_path, filename


@lru_cache(maxsize=None)
def get(name):
    """Load a named sound

    The sound will be loaded from cache, if available

    sound = sounds.get("laser-1")
    """
    module_path, filename = parse_path(name)
    try:
        sound_module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        raise SoundNotFoundError(name)
    try:
        sound_file = importlib.resources.open_binary(sound_module, filename)
    except FileNotFoundError:
        raise SoundNotFoundError(name)
    sound = pygame.mixer.Sound(sound_file)
    return sound
