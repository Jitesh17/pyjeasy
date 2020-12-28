import cv2
import sys
import numpy as np
from typing import Union


def show_image(img: np.ndarray, window_name: str = "Cv2 Image Viewer", window_width: Union[int, None] = None, sys_exit=None) -> bool:
    # Window Declaration
    if window_width is None:
        window_h, window_w = img.shape[:2]
    else:
        img_h, img_w = img.shape[:2]
        scale_factor = window_width / img_w
        window_w, window_h = int(scale_factor * img_w), int(scale_factor * img_h)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    if window_width is not None:
        cv2.resizeWindow(window_name, window_w, window_h)
    cv2.imshow(window_name, img)
    quit_flag = False
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('n'):
            break
        elif key == ord('q'):
            quit_flag = True
            if sys_exit:
                sys.exit(sys_exit)
            break
    cv2.destroyAllWindows()

    return quit_flag
