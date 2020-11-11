
import cv2
import numpy as np


def create_mask(img, color, difference=10):
    lower = np.array(color)-np.array([difference]*3)  # , dtype="uint8")
    upper = np.array(color)+np.array([difference]*3)  # , dtype="uint8")
    mask = cv2.inRange(img, lower, upper)
    return mask
