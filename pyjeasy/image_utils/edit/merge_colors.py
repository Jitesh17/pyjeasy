import os
from datetime import datetime
from sys import exit as x

import cv2
import numpy as np
import printj
from PIL import Image
from pyjeasy.file_utils.file_func import make_dir_if_not_exists
from pyjeasy.image_utils.mask_lib import create_mask
from pyjeasy.image_utils.convert.image_utils_convert_data import id_to_color
from pyjeasy.image_utils.preview import show_image
from typing import List, Tuple, Union


def merge_colors(
    image_path, 
    color_to: Union[int, list, tuple]=None, 
    color_from: list=None, 
    except_colors: List[list]=None,
    except_bg_colors: bool=False, 
    show_preview: bool=False, 
    write_image_path: str=None, 
    verbose: bool=False
    ):
    """
    Change specific colors to a certain color in the given image.
    
    Input:
    image_path, color_to, 
    color_from: list=None, 
    except_colors: list=None,
    except_bg_colors: bool=False, # Backgroung is decided by the color region with largest area
    show_image: bool=False, 
    write_image_path: src=None
    """
    
    change_to = None
    colors = get_all_colors(img_path=image_path)
    if isinstance(color_to, int):
        change_to = id_to_color(color_to)
    elif isinstance(color_to, tuple):
        change_to = list(color_to)
    elif isinstance(color_to, list):
        change_to = color_to
    elif color_to == None:
        printj.cyan(f"All {len(colors)} colors in the image: {colors}")
    else:
        raise TypeError
    
    change_from_list = []
    if color_from:
        change_from_list = color_from
    
    if verbose:
        printj.cyan(f"All {len(colors)} colors in the image: {colors}")
        
    if except_bg_colors:
        except_colors = [list(colors[0][-1])]
        if verbose:
            printj.yellow(f"Background color is {except_colors}")
        
    if except_colors:
        for i, c in colors:
            if list(c) not in except_colors:
                change_from_list.append(list(reversed(list(c))))
            
    img_cv = cv2.imread(image_path)
    
    if color_to:
        for change_from in change_from_list:
            mask = create_mask(img_cv, change_from)
            img_cv[mask==255]=change_to
    else:
        printj.red(f"Input 'color_to' is empty")
    
    if show_preview:
        quit = show_image(img_cv)
        if quit:
            return quit
    if write_image_path:
        cv2.imwrite(write_image_path, img_cv)
        if verbose:
            printj.yellow(f"Writing image: {write_image_path}")
    return False

def get_all_colors(img=None, img_path=None) -> List[Tuple[int, int]]: 
    """
    Get all colors in the image.
    
    Input:
    img=None, img_path=None
    """
    if img_path:
        img = Image.open(img_path)
    return img.convert('RGB').getcolors()