# from __future__ import annotations
from typing import List
import numpy as np


# from shapely.geometry import Point as ShapelyPoint

# from logger import logger

# from ..constants import number_types
# from ..check_utils import check_type, check_type_from_list, check_list_length
# from ..utils import get_class_string
# from ..base.basic import BasicHandler


# TODO: Create a base class for Point2D, Point3D, Point2D_List, Point3D_List

class Point:
    def __init__(self, coordinates: list):
        # check_type(item=coordinates, valid_type_list=[list])
        # check_type_from_list(item_list=coordinates, valid_type_list=number_types)
        self.coordinates = coordinates
        self.dimensionality = len(coordinates)


#     def __str__(self):
#         return f"{get_class_string(self)}: {self.coords}"
#
#     def __repr__(self):
#         return self.__str__()
#
#     @classmethod
#     def buffer(cls, point: Point) -> Point:
#         return point
#
#     def copy(self) -> Point:
#         return Point(coords=self.coords)
#
#     def to_int(self) -> Point:
#         return Point(coords=[int(val) for val in self.coords])
#
#     def to_float(self) -> Point:
#         return Point(coords=[float(val) for val in self.coords])
#
#     def to_list(self) -> list:
#         return self.coords
#
#     def to_shapely(self) -> ShapelyPoint:
#         return ShapelyPoint(self.to_list())
#
#     @classmethod
#     def from_list(cls, coords: list) -> Point:
#         return Point(coords=coords)
#
#     @classmethod
#     def from_shapely(cls, shapely_point: ShapelyPoint) -> Point:
#         return Point(coords=[list(val)[0] for val in shapely_point.coords.xy])
#
#     def within(self, obj) -> bool:
#         return self.to_shapely().within(obj.to_shapely())
#
#
class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
#
#     def __str__(self):
#         return f"Point2D({self.x},{self.y})"
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other) -> Point2D:
#         if isinstance(other, Point2D):
#             return Point2D(x=self.x + other.x, y=self.y + other.y)
#         elif isinstance(other, (int, float)):
#             return Point2D(x=self.x + other, y=self.y + other)
#         else:
#             logger.error(f'Cannot add {type(other)} to Point2D')
#             raise TypeError
#
#     def __sub__(self, other) -> Point2D:
#         if isinstance(other, Point2D):
#             return Point2D(x=self.x - other.x, y=self.y - other.y)
#         elif isinstance(other, (int, float)):
#             return Point2D(x=self.x - other, y=self.y - other)
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Point2D')
#             raise TypeError
#
#     def __mul__(self, other) -> Point2D:
#         if isinstance(other, (int, float)):
#             return Point2D(x=self.x * other, y=self.y * other)
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Point2D')
#             raise TypeError
#
#     def __truediv__(self, other) -> Point2D:
#         if isinstance(other, (int, float)):
#             return Point2D(x=self.x / other, y=self.y / other)
#         else:
#             logger.error(f'Cannot divide {type(other)} from Point2D')
#             raise TypeError
#
#     def __eq__(self, other: Point2D) -> bool:
#         if isinstance(other, Point2D):
#             return self.x == other.x and self.y == other.y
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, val: Point2D) -> Point2D:
#         return val
#
#     def copy(self) -> Point2D:
#         return Point2D(x=self.x, y=self.y)
#
#     def to_list(self) -> list:
#         return [self.x, self.y]
#
#     @classmethod
#     def from_list(cls, coords: list) -> Point2D:
#         check_list_length(coords, correct_length=2)
#         return Point2D(x=coords[0], y=coords[1])
#
#     def to_numpy(self) -> np.ndarray:
#         return np.array(self.to_list())
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray) -> Point2D:
#         if arr.shape != (2,):
#             logger.error(f'Expected shape: (2,), got {arr.shape} instead.')
#             raise Exception
#         return cls.from_list(arr.tolist())
#
#     def to_shapely(self) -> ShapelyPoint:
#         return ShapelyPoint(self.to_list())
#
#     @classmethod
#     def from_shapely(cls, shapely_point: ShapelyPoint) -> Point2D:
#         return Point2D.from_list(coords=[list(val)[0] for val in shapely_point.coords.xy])
#
#     def within(self, obj) -> bool:
#         return self.to_shapely().within(obj.to_shapely())
#
#     @classmethod
#     def origin(cls, x: float = 0.0, y: float = 0.0) -> Point2D:
#         return Point2D(x=x, y=y)
#
#     def distance(self, other: Point2D) -> float:
#         if isinstance(other, Point2D):
#             return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
#         else:
#             raise TypeError
#
#
# class Point2D_List(BasicHandler['Point2D_List', 'Point2D']):
#     def __init__(self, point_list: List[Point2D]):
#         super().__init__(obj_type=Point2D, obj_list=point_list)
#         self.point_list = self.obj_list
#
#     def __str__(self) -> str:
#         return str(self.to_list(demarcation=True))
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Point2D_List:
#         if isinstance(other, (Point2D, int, float)):
#             return Point2D_List(point_list=[point + other for point in self])
#         else:
#             logger.error(f'Cannot add {type(other)} to Point2D_List')
#             raise TypeError
#
#     def __sub__(self, other) -> Point2D_List:
#         if isinstance(other, (Point2D, int, float)):
#             return Point2D_List(point_list=[point - other for point in self])
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Point2D_List')
#             raise TypeError
#
#     def __mul__(self, other) -> Point2D_List:
#         if isinstance(other, (int, float)):
#             return Point2D_List(point_list=[point * other for point in self])
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Point2D_List')
#             raise TypeError
#
#     def __truediv__(self, other) -> Point2D_List:
#         if isinstance(other, (int, float)):
#             return Point2D_List(point_list=[point / other for point in self])
#         else:
#             logger.error(f'Cannot divide {type(other)} from Point2D_List')
#             raise TypeError
#
#     def __eq__(self, other: Point2D_List) -> bool:
#         if isinstance(other, Point2D_List):
#             return all([p0 == p1 for p0, p1 in zip(self, other)])
#         else:
#             return NotImplemented
#
#     def to_numpy(self, demarcation: bool = True) -> np.ndarray:
#         if demarcation:
#             return np.array([point.to_list() for point in self])
#         else:
#             return np.array([point.to_list() for point in self]).reshape(-1)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray, demarcation: bool = True) -> Point2D_List:
#         if demarcation:
#             if arr.shape[-1] != 2:
#                 logger.error(f"arr.shape[-1] != 2")
#                 logger.error(f'arr.shape: {arr.shape}')
#                 raise Exception
#             return Point2D_List(
#                 point_list=[Point2D.from_numpy(arr_part) for arr_part in arr]
#             )
#         else:
#             if len(arr.shape) != 1:
#                 logger.error(f"Expecting flat array when demarcation=False")
#                 logger.error(f"arr.shape: {arr.shape}")
#                 raise Exception
#             elif arr.shape[0] % 2 != 0:
#                 logger.error(f"arr.shape[0] % 2 == {arr.shape[0]} % 2 == {arr.shape[0] % 2} != 0")
#                 raise Exception
#             return Point2D_List(
#                 point_list=[Point2D.from_numpy(arr_part) for arr_part in arr.reshape(-1, 2)]
#             )
#
#     def to_list(self, demarcation: bool = True) -> list:
#         return self.to_numpy(demarcation=demarcation).tolist()
#
#     @classmethod
#     def from_list(cls, value_list: list, demarcation: bool = True) -> Point2D_List:
#         return cls.from_numpy(arr=np.array(value_list), demarcation=demarcation)
#
#     def to_shapely_list(self) -> List[ShapelyPoint]:
#         return [point.to_shapely() for point in self]
#
#     @classmethod
#     def from_shapely(cls, shapely_point_list: List[ShapelyPoint]) -> Point2D_List:
#         return Point2D_List(point_list=[Point2D.from_shapely(shapely_point) for shapely_point in shapely_point_list])
#
#     def within(self, obj) -> bool:
#         if len(self) == 0:
#             return False
#         for point in self:
#             if not point.within(obj):
#                 return False
#         return True
#
#
# class Point3D:
#     def __init__(self, x: float, y: float, z: float):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"Point3D({self.x},{self.y},{self.z})"
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other) -> Point3D:
#         if isinstance(other, Point3D):
#             return Point3D(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)
#         elif isinstance(other, (int, float)):
#             return Point3D(x=self.x + other, y=self.y + other, z=self.z + other)
#         else:
#             logger.error(f'Cannot add {type(other)} to Point3D')
#             raise TypeError
#
#     def __sub__(self, other) -> Point3D:
#         if isinstance(other, Point3D):
#             return Point3D(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)
#         elif isinstance(other, (int, float)):
#             return Point3D(x=self.x - other, y=self.y - other, z=self.z - other)
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Point3D')
#             raise TypeError
#
#     def __mul__(self, other) -> Point3D:
#         if isinstance(other, (int, float)):
#             return Point3D(x=self.x * other, y=self.y * other, z=self.z * other)
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Point3D')
#             raise TypeError
#
#     def __truediv__(self, other) -> Point3D:
#         if isinstance(other, (int, float)):
#             return Point3D(x=self.x / other, y=self.y / other, z=self.z / other)
#         else:
#             logger.error(f'Cannot divide {type(other)} from Point3D')
#             raise TypeError
#
#     def __eq__(self, other: Point3D) -> bool:
#         if isinstance(other, Point3D):
#             return self.x == other.x and self.y == other.y and self.z == other.z
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, val: Point3D) -> Point3D:
#         return val
#
#     def copy(self) -> Point3D:
#         return Point3D(x=self.x, y=self.y, z=self.z)
#
#     def to_list(self) -> list:
#         return [self.x, self.y, self.z]
#
#     @classmethod
#     def from_list(cls, coords: list) -> Point3D:
#         check_list_length(coords, correct_length=3)
#         return Point3D(x=coords[0], y=coords[1], z=coords[2])
#
#     def to_numpy(self) -> np.ndarray:
#         return np.array(self.to_list())
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray) -> Point3D:
#         if arr.shape != (3,):
#             logger.error(f'Expected shape: (3,), got {arr.shape} instead.')
#             raise Exception
#         return cls.from_list(arr.tolist())
#
#     @classmethod
#     def origin(cls, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> Point3D:
#         return Point3D(x=x, y=y, z=z)
#
#     def distance(self, other: Point3D) -> float:
#         if isinstance(other, Point3D):
#             return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
#         else:
#             raise TypeError
#
#
# class Point3D_List(BasicHandler['Point3D_List', 'Point3D']):
#     def __init__(self, point_list: List[Point3D]):
#         super().__init__(obj_type=Point3D, obj_list=point_list)
#         self.point_list = self.obj_list
#
#     def __str__(self) -> str:
#         return str(self.to_list(demarcation=True))
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Point3D_List:
#         if isinstance(other, (Point3D, int, float)):
#             return Point3D_List(point_list=[point + other for point in self])
#         else:
#             logger.error(f'Cannot add {type(other)} to Point3D_List')
#             raise TypeError
#
#     def __sub__(self, other) -> Point3D_List:
#         if isinstance(other, (Point3D, int, float)):
#             return Point3D_List(point_list=[point - other for point in self])
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Point3D_List')
#             raise TypeError
#
#     def __mul__(self, other) -> Point3D_List:
#         if isinstance(other, (int, float)):
#             return Point3D_List(point_list=[point * other for point in self])
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Point3D_List')
#             raise TypeError
#
#     def __truediv__(self, other) -> Point3D_List:
#         if isinstance(other, (int, float)):
#             return Point3D_List(point_list=[point / other for point in self])
#         else:
#             logger.error(f'Cannot divide {type(other)} from Point3D_List')
#             raise TypeError
#
#     def __eq__(self, other: Point3D_List) -> bool:
#         if isinstance(other, Point3D_List):
#             return all([p0 == p1 for p0, p1 in zip(self, other)])
#         else:
#             return NotImplemented
#
#     def to_numpy(self, demarcation: bool = True) -> np.ndarray:
#         if demarcation:
#             return np.array([point.to_list() for point in self])
#         else:
#             return np.array([point.to_list() for point in self]).reshape(-1)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray, demarcation: bool = True) -> Point3D_List:
#         if demarcation:
#             if arr.shape[-1] != 3:
#                 logger.error(f"arr.shape[-1] != 3")
#                 logger.error(f'arr.shape: {arr.shape}')
#                 raise Exception
#             return Point3D_List(
#                 point_list=[Point3D.from_numpy(arr_part) for arr_part in arr]
#             )
#         else:
#             if len(arr.shape) != 1:
#                 logger.error(f"Expecting flat array when demarcation=False")
#                 logger.error(f"arr.shape: {arr.shape}")
#                 raise Exception
#             elif arr.shape[0] % 3 != 0:
#                 logger.error(f"arr.shape[0] % 3 == {arr.shape[0]} % 3 == {arr.shape[0] % 3} != 0")
#                 raise Exception
#             return Point3D_List(
#                 point_list=[Point3D.from_numpy(arr_part) for arr_part in arr.reshape(-1, 3)]
#             )
#
#     def to_list(self, demarcation: bool = True) -> list:
#         return self.to_numpy(demarcation=demarcation).tolist()
#
#     @classmethod
#     def from_list(cls, value_list: list, demarcation: bool = True) -> Point3D_List:
#         return cls.from_numpy(arr=np.array(value_list), demarcation=demarcation)
