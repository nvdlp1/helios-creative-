from gtuner import *
from creative_helper import *

combo = Combo()


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    # Read inputs with get_actual().
    # Write outputs with combo.set_val().
    # Leave empty for pure passthrough.

    return combo.buttons, combo.sticks
