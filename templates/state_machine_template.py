from gtuner import *
from creative_helper import *

combo = Combo()

IDLE = 0
RUNNING = 1
COOLDOWN = 2

combo.state = IDLE
combo.timer = 0
combo.prev_rb = 0.0


# Configuration
RUN_FRAMES = 30
COOLDOWN_FRAMES = 12


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    rb = get_actual(3)

    if combo.state == IDLE:
        if rb and not combo.prev_rb:
            combo.state = RUNNING
            combo.timer = RUN_FRAMES

    elif combo.state == RUNNING:
        combo.set_val(STICK_1_Y, 100)
        combo.timer -= 1
        if combo.timer <= 0:
            combo.state = COOLDOWN
            combo.timer = COOLDOWN_FRAMES

    elif combo.state == COOLDOWN:
        combo.timer -= 1
        if combo.timer <= 0:
            combo.state = IDLE

    combo.prev_rb = rb
    return combo.buttons, combo.sticks
