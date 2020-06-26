import importlib.resources as pkg_resources

import pygame

import lasergame.data.fonts

font_cache = {}


def get_fontpath(name):
    if name == pygame.font.get_default_font():
        fontpath = name
    else:
        with pkg_resources.path(lasergame.data.fonts, name) as p:
            fontpath = p
    return str(fontpath)


def get(name=None, size=None):
    """Load a font

    The font will be loaded from cache, if available

    font = fonts.get()
    font = fonts.get(size=16)
    font = fonts.get("freesansbold.ttf", size=16)
    """
    if name is None:
        name = pygame.font.get_default_font()
    if size is None:
        size = 16
    key = (name, size)
    font = font_cache.get(key)
    if font is None:
        font = pygame.font.Font(get_fontpath(name), size)
        font_cache[key] = font
    return font


def render(text, *, font=None, size=None, antialias=False, color=(0, 0, 0), background=None):
    """Render text to a surface

    font = fonts.render("Text")
    font = fonts.render("Text", font="freesansbold.ttf")
    font = fonts.render("Text", size=16)
    font = fonts.render("Text", antialias=True)
    font = fonts.render("Text", color=(0x80, 0x80, 0x80))
    font = fonts.render("Text", background=(0xFF, 0x00, 0xFF))
    """
    font_obj = get(font, size)
    textsurface = font_obj.render(text, antialias, color, background)
    return textsurface


def test_get():
    blk = (0x00, 0x00, 0x00)
    gry = (0x80, 0x80, 0x80)
    pygame.init()
    screen = pygame.display.set_mode([200, 200])
    screen.fill(blk)

    font = get()
    rendered = font.render("TEST 1", False, gry)
    screen.blit(rendered, (0, 0))

    font = get(size=12)
    rendered = font.render("TEST 2", False, gry)
    screen.blit(rendered, (0, 20))

    font = get("freesansbold.ttf")
    rendered = font.render("TEST 3", False, gry)
    screen.blit(rendered, (0, 40))

    font = get("freesansbold.ttf", 20)
    rendered = font.render("TEST 4", False, gry)
    screen.blit(rendered, (0, 60))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def test_render():
    blk = (0x00, 0x00, 0x00)
    gry = (0x80, 0x80, 0x80)
    mga = (0xFF, 0x00, 0xFF)
    pygame.init()
    screen = pygame.display.set_mode([200, 200])
    screen.fill(blk)

    rendered = render("TEST 1", color=gry)
    screen.blit(rendered, (0, 0))

    rendered = render("TEST 2", size=12, color=gry)
    screen.blit(rendered, (0, 20))

    rendered = render("TEST 3", font="freesansbold.ttf", color=gry)
    screen.blit(rendered, (0, 40))

    rendered = render("TEST 4", font="freesansbold.ttf", size=20, color=gry)
    screen.blit(rendered, (0, 60))

    rendered = render("TEST 5", color=gry, antialias=True)
    screen.blit(rendered, (0, 80))

    rendered = render("TEST 6", size=12, color=gry, antialias=True)
    screen.blit(rendered, (0, 100))

    rendered = render("TEST 7", font="freesansbold.ttf", color=gry, antialias=True)
    screen.blit(rendered, (0, 120))

    rendered = render("TEST 8", font="freesansbold.ttf", size=20, color=gry, antialias=True)
    screen.blit(rendered, (0, 140))

    rendered = render("TEST 9", color=blk, background=mga)
    screen.blit(rendered, (0, 160))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    test_get()
    test_render()
