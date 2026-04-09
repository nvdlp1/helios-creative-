from gtuner import *
from creative_helper import *

combo = Combo()


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    if get_actual(3):
        combo.set_val(STICK_1_Y, 100)

    return combo.buttons, combo.sticks
