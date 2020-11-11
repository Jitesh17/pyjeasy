import cv2
import numpy as np


def concat_images(imga, imgb, orientation: int = 0):
    """
    Combines two color image ndarrays side-by-side.
    orientation
    0: horizontal
    1: vertical
    """
    ha, wa = imga.shape[:2]
    hb, wb = imgb.shape[:2]
    max_h, max_w = np.max([ha, hb]), np.max([wa, wb])
    sum_h, sum_w = np.sum([ha, hb]), np.sum([wa, wb])

    if orientation == 0:  # horizontal
        new_img = np.zeros(shape=(max_h, sum_w, 3))
        new_img[:ha, :wa] = imga
        new_img[:hb, wa:wa+wb] = imgb
    elif orientation == 1:  # vertical
        new_img = np.zeros(shape=(sum_h, max_w, 3))
        new_img[:ha, :wa] = imga
        new_img[ha:ha+hb, :wb] = imgb
    else:
        raise Exception

    return new_img.astype('uint8')


def concat_n_images(img_list: list, orientation: int = 0):
    """
    Combines N color images from a list ndarray images
    orientation
    0: horizontal
    1: vertical
    """
    output = None
    for i, img in enumerate(img_list):
        if i == 0:
            output = img
        else:
            output = concat_images(output, img, orientation=orientation)
    return output
