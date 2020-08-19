import glob
import inspect
import os
from typing import List

import printj
# from ..constants import opencv_compatible_img_extensions
from pyjeasy.file_utils.file_func import dir_exists, path_exists
# from .file_func import dir_exists, path_exists
# from . import dir_exists

def get_script_path() -> str:
    return os.path.abspath((inspect.stack()[1])[1])

def get_script_dir_path() -> str:
    caller_script_path = os.path.abspath((inspect.stack()[1])[1])
    caller_script_dir = os.path.dirname(caller_script_path)
    return caller_script_dir

def find_path_matching_pattern(filepath_pattern: str) -> list:
    return glob.glob(filepath_pattern)

def get_filename(path: str) -> str:
    return path.split('/')[-1]

def get_extension_from_filename(filename: str) -> str:
    return filename.split('.')[-1]

def get_abs_path(rel_path: str) -> str:
    return os.path.abspath(rel_path)

def get_all_filepaths_of_extension_recursively(dirpath: str, extension: str):
    return [y for x in os.walk(dirpath) for y in glob.glob(os.path.join(x[0], f'*.{extension}'))]

def make_pathlist(dir_path: str, filename_list: list):
    return ['{}/{}'.format(dir_path, filename) for filename in filename_list]

if __name__ == "__main__":

    printj.yellow(inspect.stack())
    print(get_script_dir_path())
    print(get_script_path())
    print(path_exists(get_script_dir_path()))