from itertools import groupby
from operator import itemgetter
from typing import List, Any


def group_consecutive_numbers_from_list(input_data: list) -> list:
    result: List[List[Any]] = []
    for k, g in groupby(enumerate(input_data), lambda ix: ix[0] - ix[1]):
        result.append(list(map(itemgetter(1), g)))
    return result


def flat_list(input_data: list) -> list:
    return [item for sublist in input_data for item in sublist]


if __name__ == "__main__":
    data = [1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
    group_data = group_consecutive_numbers_from_list(data)
    print(f'group_data: {group_data}')
    flat_data = flat_list(group_data)
    print(f'flat_data: {flat_data}')
