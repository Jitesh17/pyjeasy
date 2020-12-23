import cv2
import numpy as np


def create_mask(img, color, difference=10, min_limit=0, max_limit=255):
    lower = np.array([max(min_limit, a - difference) for a in color])  # , dtype="uint8")
    upper = np.array([min(max_limit, a + difference) for a in color])  # , dtype="uint8")
    mask = cv2.inRange(img, lower, upper)
    return mask
