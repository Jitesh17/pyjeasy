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
        dim = (size.width, size.height)
    elif scale_percent != 0:

        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
    else:
        raise Exception
    return cv2.resize(src=img, dsize=dim, interpolation=interpolation)

def bool_mask_to_points_array(mask_bool: np.ndarray) -> np.ndarray:
    points = np.concatenate([[x] for x in np.where(mask_bool > 0)[::-1]], axis=0)
    return points