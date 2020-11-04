from itertools import groupby
from operator import itemgetter
from typing import List, Any
import printj
from pyjeasy.check_utils import check_type, check_type_from_list


def group_consecutive_numbers_from_list(input_data: list) -> list:
    result: List[List[Any]] = []
    for k, g in groupby(enumerate(input_data), lambda ix: ix[0] - ix[1]):
        result.append(list(map(itemgetter(1), g)))
    return result


def flat_list(input_data: list) -> list:
    return [item for sublist in input_data for item in sublist]


def unflatten_list(flat_list: List[Any], part_sizes: List[int]):
    check_type(flat_list, valid_type_list=[list])
    check_type_from_list(part_sizes, valid_type_list=[int])
    if sum(part_sizes) != len(flat_list):
        printj.red(
            f'sum(part_sizes) == {sum(part_sizes)} != {len(flat_list)} == len(flat_list)')
        raise Exception
    slice_list = sizes2slices(part_sizes=part_sizes)
    return [flat_list[slice0] for slice0 in slice_list]


def sizes2slices(part_sizes: List[int]) -> List[slice]:
    slice_list = []
    left_idx = 0
    right_idx = None
    for part_size in part_sizes:
        if right_idx is None:
            right_idx = part_size
        else:
            left_idx = right_idx
            right_idx += part_size
        slice_list.append(slice(left_idx, right_idx))
    return slice_list


if __name__ == "__main__":
    data = [1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
    group_data = group_consecutive_numbers_from_list(data)
    print(f'group_data: {group_data}')
    flat_data = flat_list(group_data)
    print(f'flat_data: {flat_data}')
