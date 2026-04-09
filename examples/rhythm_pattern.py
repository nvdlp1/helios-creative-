from gtuner import *
from creative_helper import *
import copy

combo = Combo()
combo.active = False
combo.prev_rb = 0.0
combo.rhythm = None

RHYTHM_SHOT = {
    "index": [STICK_1_Y, STICK_1_Y, STICK_1_Y, STICK_1_Y, STICK_1_Y, STICK_1_Y],
    "val": [100, 65, 25, -25, -75, -100],
    "timer": [26, 1, 1, 1, 1, 20],
}


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    rb = get_actual(3)

    if rb and not combo.prev_rb:
        combo.active = True
        combo.rhythm = copy.deepcopy(RHYTHM_SHOT)

    if combo.active and combo.rhythm is not None:
        if combo.set_val_from_dict(combo.rhythm):
            combo.active = False
            combo.rhythm = None

    combo.prev_rb = rb
    return combo.buttons, combo.sticks
