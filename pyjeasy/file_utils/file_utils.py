"""
This is an example Calculator app which performs addition,
subtraction, multiplication and division. It will help me
demonstrate how to appropriately structure a Python project.
The coding style of the project is PEP8.
"""

__author__ = 'Jitesh Gosar'
__email__ = 'gosar95@gmail.com'
__license__ = 'MIT'
__date__ = 'Saturday, Jun 20, 2020'
__version__ = '0.0.1'


import os
import subprocess
import sys
from distutils.dir_util import copy_tree
from shutil import copyfile, rmtree

import printj


def path_exists(url: str) -> bool:
    return os.path.exists(url)

def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)

def dir_exists(dir_path: str) -> bool:
    return os.path.isdir(dir_path)

def link_exists(link_url: str) -> bool:
    return os.path.islink(link_url)

def file_exists_in_dir(file_path: str, dir_path: str) -> bool:
    onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return file_path in onlyfiles

def make_dir(dir_path: str):
    os.mkdir(dir_path)

def make_dir_if_not_exists(dir_path: str):
    if not dir_exists(dir_path):
        make_dir(dir_path)

def delete_file(path: str):
    os.unlink(path)  # Same as os.remove(path)

def delete_dir(dir_path: str):
    rmtree(dir_path)

def delete_dir_if_exists(dir_path: str):
    if dir_exists(dir_path):
        delete_dir(dir_path)

def delete_file_if_exists(file_path: str):
    if file_exists(file_path):
        delete_file(file_path)

def dir_files_list(dir_path: str) -> list:
    if not dir_exists(dir_path):
        raise Exception(f"Directory not found: {dir_path}")
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def dir_contents_list(dir_path: str) -> list:
    if not dir_exists(dir_path):
        raise Exception(f"Directory not found: {dir_path}")
    return os.listdir(dir_path)

def dir_length(dir_path: str) -> int:
    return len(os.listdir(dir_path))

def dir_is_empty(dir_path: str) -> bool:
    return dir_length(dir_path) == 0

def get_filename_from_path(path: str) -> str:
    return path.split("/")[-1]

def delete_all_files_in_dir(dir_path: str, ask_permission: bool=True, verbose: bool=True):
    if dir_is_empty(dir_path):
        if verbose:
            printj.yellow('Directory is already empty.')
    else:
        while True:
            if ask_permission:
                delete_command = input(f'Do you want to delete all of the files in dir "{dir_path}"? \nType yes/no:')
            else:
                delete_command = 'yes'
            if delete_command=='yes':
                filenames = os.listdir(dir_path)
                for filename in filenames:
                    path = os.path.join(dir_path, filename)
                    if file_exists(path):
                        delete_file(path)
                    else:
                        delete_dir(path)
                    if verbose:
                        printj.purple(f'Deleted {path}')
                break
            elif delete_command=='no':
                if verbose:
                    printj.green('The files are not deleted.')
                    printj.red('Program terminated')
                sys.exit()
            else:
                printj.cyan('That was an invalid input.\nTry again...')

def copy_file(src_path: str, dst_path: str, verbose: bool=True):
    copyfile(src_path, dst_path)
    if verbose:
        print(printj.ColorText.cyan(f'Copied "{src_path}"\n')\
            + printj.ColorText.yellow(f'to "{dst_path}"'))

def copy_dir(src_path: str, dst_path: str, verbose: bool=True):
    copy_tree(src_path, dst_path)
    if verbose:
        print(printj.ColorText.cyan(f'Copied "{src_path}"\n')\
            + printj.ColorText.yellow(f'to "{dst_path}"'))

def move_file(src_path: str, dst_path: str, verbose: bool=True):
    copy_file(src_path, dst_path, verbose=True)
    delete_file(src_path)
    if verbose:
        print(printj.ColorText.cyan(f'Moved "{src_path}"\n')\
            + printj.ColorText.yellow(f'to "{dst_path}"'))

def move_dir(src_path: str, dst_path: str, verbose: bool=True):
    copy_dir(src_path, dst_path, verbose=True)
    delete_dir(src_path)
    if verbose:
        print(printj.ColorText.cyan(f'Moved "{src_path}"\n')\
            + printj.ColorText.yellow(f'to "{dst_path}"'))

def create_softlink(src_path: str, dst_path: str, verbose: bool=True):
    if link_exists(dst_path):
        delete_file(dst_path)
    subprocess.run(f"ln -s {src_path} {dst_path}", shell=True)
    if verbose:
        print(printj.ColorText.cyan(f'Softlink created for "{src_path}"\n')\
            + printj.ColorText.yellow(f'to "{dst_path}"'))
