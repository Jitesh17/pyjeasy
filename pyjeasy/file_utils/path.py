from typing import List
import os, inspect, glob
from ..file_utils import dir_exists
from ..constants import opencv_compatible_img_extensions

def get_script_path() -> str:
    caller_script_path = os.path.abspath((inspect.stack()[1])[1])
    return caller_script_path

def get_script_dir() -> str:
    caller_script_path = os.path.abspath((inspect.stack()[1])[1])
    caller_script_dir = os.path.dirname(caller_script_path)
    return caller_script_dir

def get_filelist(dir_path: str) -> list:
    if not dir_exists:
        raise Exception(f"Directory not found: {dir_path}")
    return os.listdir(dir_path)

def find_path_matching_pattern(filepath_pattern: str) -> list:
    return glob.glob(filepath_pattern)

def get_pathlist(dir_path: str) -> list:
    filename_list = get_filelist(dir_path)
    return construct_pathlist(dir_path, filename_list)

def get_filename(path: str) -> str:
    return path.split('/')[-1]

def get_parent_dir(path: str) -> str:
    return path.split('/')[-2]

def get_rootname_from_filename(filename: str) -> str:
    return '.'.join(filename.split('.')[:-1])

def get_rootname_from_path(path: str) -> str:
    filename = get_filename(path)
    return get_rootname_from_filename(filename)

def get_extension_from_filename(filename: str) -> str:
    return filename.split('.')[-1]

def get_extension_from_path(path: str) -> str:
    filename = get_filename(path)
    return get_extension_from_filename(filename)

def get_dirpath_from_filepath(filepath: str) -> str:
    return '/'.join(filepath.split('/')[:-1])

def construct_pathlist(dir_path: str, filename_list: list):
    return ['{}/{}'.format(dir_path, filename) for filename in filename_list]

def truncate_path(path: str, degree: int) -> str:
    """
    degree  |   result
    ==================
    0       |   full path
    1       |   parent directory
    2       |   parent's parent directory
    ...
    """
    if degree < 0:
        raise IndexError('degree cannot be a negative integer')
    if degree == 0:
        return path
    return '/'.join(path.split('/')[0:-degree])

def rel_to_abs_path(rel_path: str) -> str:
    return os.path.abspath(rel_path)

def get_abs_path(rel_path: str, ref_dir: str):
    return os.path.normpath(f'{ref_dir}/{rel_path}')

def get_all_files_of_extension(dir_path: str, extension: str=None) -> list:
    filepaths = get_pathlist(dir_path)
    if extension is not None:
        filepaths_of_extension = []
        for filepath in filepaths:
            ext = get_extension_from_path(filepath)
            if ext == extension:
                filepaths_of_extension.append(filepath)
        filepaths = filepaths_of_extension
    return filepaths

def get_all_files_in_extension_list(dir_path: str, extension_list: list=None) -> list:
    filepaths = get_pathlist(dir_path)
    if extension_list is not None:
        filepaths_of_extension = []
        for filepath in filepaths:
            ext = get_extension_from_path(filepath)
            if ext in extension_list:
                filepaths_of_extension.append(filepath)
        filepaths = filepaths_of_extension
    return filepaths

def file_extension_exists_in_dir(dir_path: str, extension: str) -> bool:
    ext_filepaths = get_all_files_of_extension(dir_path, extension)
    if len(ext_filepaths) > 0:
        return True
    else:
        return False

def get_newest_filepath(dir_path: str, extension: str=None) -> str:
    filepaths = get_all_files_of_extension(dir_path, extension)
    if len(filepaths) > 0:
        return max(filepaths, key=os.path.getctime)
    else:
        return None

def get_next_dump_path(
    dump_dir: str, file_extension: str, label_length: int=6,
    starting_number: int=0, increment: int=1
    ):
    file_paths = get_all_files_of_extension(dir_path=dump_dir, extension=file_extension)
    file_paths.sort()

    newest_filepath = file_paths[-1] if len(file_paths) > 0 else None
    next_label_number = \
        int(get_rootname_from_path(newest_filepath)) + increment \
            if newest_filepath is not None else starting_number
    next_label_str = str(next_label_number)
    while len(next_label_str) < label_length:
        next_label_str = '0' + next_label_str
    dump_filename = f'{next_label_str}.{file_extension}'
    dump_path = f'{dump_dir}/{dump_filename}'
    return dump_path

def get_possible_rel_paths(path: str) -> List[str]:
    path_parts = path.split('/')
    return ['/'.join(path_parts[i:]) for i in range(len(path_parts))]

def get_possible_container_dirs(path: str) -> List[str]:
    path_parts = path.split('/')
    return ['/'] + ['/'.join(path_parts[:i]) for i in range(2, len(path_parts))]

def recursively_get_all_filepaths_of_extension(dirpath: str, extension: str):
    return [y for x in os.walk(dirpath) for y in glob.glob(os.path.join(x[0], f'*.{extension}'))]

def find_moved_abs_path(
    old_path: str, container_dir: str,
    get_first_match: bool=True
) -> str:
    container_dirname = container_dir.split('/')[-1]
    new_path_list = []
    for possible_path in get_possible_rel_paths(path=old_path):
        if possible_path.split('/')[0] == container_dirname:
            found_path = f"{container_dir}/{'/'.join(possible_path.split('/')[1:])}"
            new_path_list.append(found_path)
            if get_first_match:
                break

    if len(new_path_list) == 0:
        new_path = None
    elif len(new_path_list) == 1:
        new_path = new_path_list[0]
    else:
        error_str = 'Found two possible matches with the given search criteria:'
        for path in new_path_list:
            error_str += f'\n\t{path}'
        error_str += 'In order to avoid unexpected behavior, please modify container_dir to contain only the desired path.'
        print(error_str)
        raise Exception
    return new_path

def find_longest_container_dir(path_list: List[str]) -> str:
    for path in path_list:
        if '/' not in path:
            raise Exception(f"'/' not in {path}")
    
    possible_container_dirs_set_list = [set(get_possible_container_dirs(path)) for path in path_list]
    common_container_dir_list = list(set.intersection(*possible_container_dirs_set_list))
    if len(common_container_dir_list) > 0:
        longest_idx, longest_str_len = None, None
        for i, common_container_dir in enumerate(common_container_dir_list):
            if longest_str_len is None or longest_str_len < len(common_container_dir):
                longest_idx = i
                longest_str_len = len(common_container_dir)
        return common_container_dir_list[longest_idx]
    else:
        error_str = "Couldn't find any common container directories from the paths:"
        for path in path_list:
            error_str += f'\n\t{path}'
        print(error_str)
        raise Exception

def find_shortest_common_rel_path(path_list: List[str]) -> str:
    for path in path_list:
        if '/' not in path:
            raise Exception(f"'/' not in {path}")

    possible_rel_paths_set_list = [set(get_possible_rel_paths(path)) for path in path_list]
    common_rel_path_list = list(set.intersection(*possible_rel_paths_set_list))
    if len(common_rel_path_list) > 0:
        shortest_idx, shortest_str_len = None, None
        for i, common_rel_path in enumerate(common_rel_path_list):
            if shortest_str_len is None or shortest_str_len < len(common_rel_path):
                shortest_idx = i
                shortest_str_len = len(common_rel_path)
        return common_rel_path_list[shortest_idx]
    else:
        error_str = "Couldn't find any common relative paths from the paths in path_list:"
        for path in path_list:
            error_str += f'\n\t{path}'
        print(error_str)
        raise Exception

def has_valid_img_extension(img_path: str) -> bool:
    img_extension = get_extension_from_path(img_path)
    return img_extension in opencv_compatible_img_extensions

def get_valid_image_paths(dir_path: str) -> List[str]:
    paths = get_pathlist(dir_path)
    return [path for path in paths if has_valid_img_extension(path)]

def get_filepaths_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [path for path in pathlist if os.path.isfile(path)]

def get_dirpaths_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [path for path in pathlist if os.path.isdir(path)]

def get_linkpaths_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [path for path in pathlist if os.path.islink(path)]

def get_mountpaths_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [path for path in pathlist if os.path.ismount(path)]

def get_filenames_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [get_filename(path) for path in pathlist if os.path.isfile(path)]

def get_dirnames_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [get_filename(path) for path in pathlist if os.path.isdir(path)]

def get_linknames_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [get_filename(path) for path in pathlist if os.path.islink(path)]

def get_mountnames_in_dir(dir_path: str) -> List[str]:
    pathlist = get_pathlist(dir_path)
    return [get_filename(path) for path in pathlist if os.path.ismount(path)]

def recursively_get_all_matches_under_dirpath(dirpath: str, target_name: str, target_type: str) -> list:
    """
    target_type
    'directory' or 'd': Recursively search for directory names that match target_name
    'file' or 'f': Recursively search for file names that match target_name
    """
    target_type = target_type.lower()
    assert target_type in ['directory', 'd', 'file', 'f']
    matches = []
    dirpath_queue = [dirpath]
    done_dirpaths = []
    while len(dirpath_queue) > 0:
        for current_dir in dirpath_queue:
            dirpaths = get_dirpaths_in_dir(current_dir)
            dirpath_queue.extend(dirpaths)
            if target_type in ['directory', 'd']:
                for path in dirpaths:
                    if get_filename(path) == target_name:
                        matches.append(path)
            elif target_type in ['file', 'f']:
                filepaths = get_filepaths_in_dir(current_dir)
                for path in filepaths:
                    if get_filename(path) == target_name:
                        matches.append(path)
            else:
                raise Exception
            done_dirpaths.append(current_dir)
        for done_dirpath in done_dirpaths:
            del dirpath_queue[dirpath_queue.index(done_dirpath)]
        done_dirpaths = []
    return matches