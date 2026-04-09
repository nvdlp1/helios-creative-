from gtuner import *
from creative_helper import *
import cv2

combo = Combo()
combo.frame_count = 0


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    frame = kwargs.get("frame")
    combo.frame_count += 1

    if frame is not None:
        rx = get_actual(STICK_1_X)
        ry = get_actual(STICK_1_Y)
        lx = get_actual(STICK_2_X)
        ly = get_actual(STICK_2_Y)

        cv2.putText(frame, "Creative Overlay", (40, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.putText(frame, "Frames: %d" % combo.frame_count, (40, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "R: (%.1f, %.1f)" % (rx, ry), (40, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "L: (%.1f, %.1f)" % (lx, ly), (40, 190),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    return combo.buttons, combo.sticks, frame
