
import os
from typing import Union

import cv2
from jaitool.structures.bbox import BBox
from pyjeasy.file_utils import make_dir_if_not_exists
from pyjeasy.image_utils import img_extentions, show_image


def crop(img_path: str, crop_box: Union[BBox, list] = None, image_show: bool = False, image_write: str = None, gray_mode: bool = False, create_folder: bool = True):
    """
    crop_box :  [xmin, ymin, xmax, ymax] or BBox instance
    """
    if isinstance(crop_box, list):
        crop_box = BBox.from_list(crop_box)
    img_rgb = cv2.imread(img_path)
    if crop_box:
        crop_img = img_rgb[crop_box.ymin:crop_box.ymax,
                           crop_box.xmin:crop_box.xmax]
    else:
        crop_img = img_rgb
    if gray_mode:
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_GRAY2BGR)

    if image_show:
        show_image(crop_img)
    if image_write:
        if any(img_extentions) not in image_write:
            if create_folder:
                make_dir_if_not_exists(image_write)
                i = 1
                while os.path.exists(f"{image_write}/{i}.png"):
                    i = i + 1
                image_write = f"{image_write}/{i}.png"
            else:
                image_write += '.jpg'

        cv2.imwrite(image_write, crop_img)


if __name__ == '__main__':
    img_path = "/home/jitesh/3d/data/coco_data/ed/test_data/test_1.jpg"
    # crop_box = BBox(14, 6, 301, 307)
    crop_box = [14, 6, 301, 307]
    crop(img_path, crop_box, True)
