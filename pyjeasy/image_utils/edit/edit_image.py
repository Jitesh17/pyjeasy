import cv2
import numpy as np
from pyjeasy.check_utils import check_value


def resize_img(src: np.ndarray, size=(0, 0), scale_percent: float = 0,
               interpolation_method: str = 'area') -> np.ndarray:
    possible_methods = ['area', 'linear']
    check_value(interpolation_method, possible_methods)
    if interpolation_method.lower() == 'area':
        interpolation = cv2.INTER_AREA
    elif interpolation_method.lower() == 'linear':
        interpolation = cv2.INTER_LINEAR
    else:
        raise Exception

    img = src.copy()
    if size != (0, 0):
        dim = size
    elif scale_percent != 0:

        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
    else:
        raise Exception
    return cv2.resize(src=img, dsize=dim, interpolation=interpolation)


def bool_mask_to_points_array(mask_bool: np.ndarray) -> np.ndarray:
    points = np.concatenate(
        [[x] for x in np.where(mask_bool > 0)[::-1]], axis=0)
    return points


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
