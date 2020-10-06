import os, sys
import printj

""" File exists """


def check_path_exists(url: str, raise_error: bool=True) -> bool:
    if os.path.exists(url):
        return True
    else:
        if raise_error:
            printj.red(f'Path not found./n{url}')
            raise Exception
        else:
            return False


def check_file_exists(file_path: str, raise_error: bool=True) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        if raise_error:
            printj.red(f'File not found./n{file_path}')
            raise Exception
        else:
            return False


def check_dir_exists(dir_path: str, raise_error: bool=True) -> bool:
    if os.path.isdir(dir_path):
        return True
    else:
        if raise_error:
            printj.red(f'Directory not found./n{dir_path}')
            raise Exception
        else:
            return False


def check_link_exists(link_url: str, raise_error: bool=True) -> bool:
    if os.path.islink(link_url):
        return True
    else:
        if raise_error:
            printj.red(f'Link not found./n{link_url}')
            raise Exception
        else:
            return False


def check_file_exists_in_dir(file_path: str, dir_path: str, raise_error: bool=True) -> bool:
    onlyfiles = [f for f in os.listdir(
        dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    if file_path in onlyfiles:
        return True
    else:
        if raise_error:
            printj.red(f'File "{file_path}" not found in the directory "{dir_path}".')
            raise Exception
        else:
            return False


""" check objects """


def check_value(value, check_from, raise_error: bool = True, verbose: bool = True) -> bool:
    if value in check_from:
        return True
    else:
        if verbose:
            message = f'{value} is not valid.\n\
                Valid options are {check_from}.'
            printj.red(message)
        if raise_error:
            raise ValueError
        return False


def check_required_keys(item_dict: dict, required_keys: list, var_name: str = None, raise_error: bool=True):
    missing_keys = []
    # provided_keys = []
    for required_key in required_keys:
        if required_key not in item_dict.keys():
            missing_keys.append(required_key)
        # else:
        #     provided_keys.append(required_key)
    if len(missing_keys) > 0:
        if var_name:
            printj.red(f"Variable Name: {var_name}")
        printj.red(f"Required keys are missing from item_dict.")
        printj.red(f"provided_keys: {item_dict.keys()}")
        printj.red(f"missing_keys: {missing_keys}")
        if raise_error:
            raise KeyError
        return False
    return True



def check_type(item, valid_type_list: list, raise_error: bool=True):
    if type(item) not in valid_type_list:
        printj.red(f"Invalid type: {type(item)}")
        printj.red(f"Valid types: {valid_type_list}")
        if raise_error:
            raise TypeError
        return False
    return True

def check_type_from_list(item_list: list, valid_type_list: list, raise_error: bool=True):
    check_type(item_list, valid_type_list=[list])
    for item in item_list:
        result = check_type(item=item, valid_type_list=valid_type_list, raise_error=raise_error)
        if not result:
            return False
    return True
            
def isOverlapping1D(box1, box2) -> bool:
    """
    box1 = (xmin1, xmax1)
    box2 = (xmin2, xmax2)
    isOverlapping1D(box1,box2) = xmax1 >= xmin2 and xmax2 >= xmin1
    """
    return box1[1] >= box2[0] and box2[1] >= box1[0]


def isOverlapping2D(box1, box2, input_type: str = "dict_x_min_max") -> bool:
    """
    box1 = (x:(xmin1,xmax1),y:(ymin1,ymax1))
    box2 = (x:(xmin2,xmax2),y:(ymin2,ymax2))
    isOverlapping2D(box1,box2) = isOverlapping1D(box1.x, box2.x) and 
                                isOverlapping1D(box1.y, box2.y)
    """
    if input_type == "dict_x_min_max":
        return isOverlapping1D(box1["x"], box2["x"]) and isOverlapping1D(box1["y"], box2["y"])
    # elif input_type == "list_point_min_max":
    #     return isOverlapping1D((box1[0]), box2[0]) and isOverlapping1D(box1.y, box2.y)
    else:
        raise NotImplementedError


def isOverlapping3D(box1, box2, input_type: str = "dict_min_max") -> bool:
    """
    box1 = (x:(xmin1,xmax1),y:(ymin1,ymax1),z:(zmin1,zmax1))
    box2 = (x:(xmin2,xmax2),y:(ymin2,ymax2),z:(zmin2,zmax2))
    isOverlapping3D(box1,box2) = isOverlapping1D(box1.x, box2.x) and 
                                isOverlapping1D(box1.y, box2.y) and
                                isOverlapping1D(box1.z, box2.z)
    """
    raise NotImplementedError
