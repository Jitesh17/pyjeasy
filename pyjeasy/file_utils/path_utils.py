import glob
import inspect
import os
from typing import List

# from ..constants import opencv_compatible_img_extensions
from .file_utils import dir_exists


def get_script_path() -> str:
    return os.path.abspath((inspect.stack()[1])[1])

def get_script_dir_path() -> str:
    caller_script_path = os.path.abspath((inspect.stack()[1])[1])
    caller_script_dir = os.path.dirname(caller_script_path)
    return caller_script_dir
