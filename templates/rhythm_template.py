from gtuner import *
from creative_helper import *
import copy

combo = Combo()
combo.activated = False
combo.pattern = None
combo.prev_rb = 0.0

PATTERN = {
    "index": [STICK_1_Y, STICK_1_Y, STICK_1_Y, STICK_1_Y],
    "val": [100, 40, -40, -100],
    "timer": [12, 4, 4, 12],
}


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    rb = get_actual(3)

    if rb and not combo.prev_rb:
        combo.activated = True
        combo.pattern = copy.deepcopy(PATTERN)

    if combo.activated:
        if combo.set_val_from_dict(combo.pattern):
            combo.activated = False
            combo.pattern = None

    combo.prev_rb = rb
    return combo.buttons, combo.sticks
