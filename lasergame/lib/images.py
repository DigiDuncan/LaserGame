import importlib

import pygame

from digicolor import colors

image_root = "lasergame.data.images"
image_ext = "png"
image_cache = {}


class ImageNotFoundError(Exception):
    def __init__(self, path):
        super().__init__(f"Unable to load image: {path!r}")


def parse_path(path):
    subpath, _, filename = path.rpartition(".")
    module_path = image_root
    if subpath:
        module_path += "." + subpath
    filename = f"{filename}.{image_ext}"
    return module_path, filename


def get(name):
    """Load a named image

    The image will be loaded from cache, if available

    image = images.get("buttons.up")
    """
    image = image_cache.get(name)
    if image is None:
        module_path, filename = parse_path(name)
        try:
            image_module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            raise ImageNotFoundError(name)
        try:
            image_file = importlib.resources.open_binary(image_module, filename)
        except FileNotFoundError:
            raise ImageNotFoundError(name)
        image = pygame.image.load(image_file)
        image.set_colorkey(colors.LIGHT_MAGENTA.rgb)
        image_cache[name] = image
    return image
