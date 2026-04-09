"""Pure-Python helper utilities for Creative scripts.

These helpers are intended to be copied into production scripts as needed.
They do not depend on Creative internals.
"""

import math

FRAMES_PER_SECOND = 120


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def deadzone(value, threshold=10.0):
    if abs(value) <= threshold:
        return 0.0
    return value


def is_pressed(value, threshold=0.0):
    return value > threshold


def just_pressed(current_value, previous_value, threshold=0.0):
    return current_value > threshold and previous_value <= threshold


def just_released(current_value, previous_value, threshold=0.0):
    return current_value <= threshold and previous_value > threshold


def frames(seconds, fps=FRAMES_PER_SECOND):
    return int(round(seconds * fps))


def milliseconds(ms, fps=FRAMES_PER_SECOND):
    return int(round((ms / 1000.0) * fps))


def normalize_stick(value, threshold=10.0):
    value = deadzone(value, threshold)
    return clamp(value, -100.0, 100.0)


def get_polar(x_value, y_value):
    return math.degrees(math.atan2(y_value, x_value)) % 360.0


def set_polar(radius, angle):
    angle = angle % 360.0
    angle_rad = math.radians(angle)
    x_value = clamp(radius * math.cos(angle_rad), -100.0, 100.0)
    y_value = clamp(radius * math.sin(angle_rad), -100.0, 100.0)
    return x_value, y_value
