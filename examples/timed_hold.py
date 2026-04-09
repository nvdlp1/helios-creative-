from gtuner import *
from creative_helper import *

combo = Combo()
combo.active = False
combo.timer = 0
combo.prev_rb = 0.0

HOLD_FRAMES = 29


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    rb = get_actual(3)

    if rb and not combo.prev_rb and not combo.active:
        combo.active = True
        combo.timer = HOLD_FRAMES

    if combo.active:
        combo.set_val(16, 100)
        combo.timer -= 1
        if combo.timer <= 0:
            combo.active = False
            combo.timer = 0

    combo.prev_rb = rb
    return combo.buttons, combo.sticks
