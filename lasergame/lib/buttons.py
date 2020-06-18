from pygame import locals as pygame_locals

from lasergame.lib.constants import buttons as button_constants
from lasergame.lib.attrdict import AttrDict

buttonsdict = {}
for k, v in button_constants._values.items():
    buttonsdict[k] = getattr(pygame_locals, v)
buttons = AttrDict(buttonsdict)
