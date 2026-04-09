from gtuner import *
from creative_helper import *
import cv2

combo = Combo()
combo.frame_count = 0

DEADZONE = 10.0


def apply_deadzone(value, threshold):
    if abs(value) <= threshold:
        return 0.0
    return value


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    frame = kwargs.get("frame")
    combo.frame_count += 1

    rx = apply_deadzone(get_actual(STICK_1_X), DEADZONE)
    ry = apply_deadzone(get_actual(STICK_1_Y), DEADZONE)
    lx = apply_deadzone(get_actual(STICK_2_X), DEADZONE)
    ly = apply_deadzone(get_actual(STICK_2_Y), DEADZONE)

    if frame is not None:
        cv2.putText(frame, "Deadzone Debug", (40, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.putText(frame, "Frames: %d" % combo.frame_count, (40, 95),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "R stick: (%.1f, %.1f)" % (rx, ry), (40, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "L stick: (%.1f, %.1f)" % (lx, ly), (40, 180),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "Threshold: %.1f" % DEADZONE, (40, 220),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    return combo.buttons, combo.sticks, frame
