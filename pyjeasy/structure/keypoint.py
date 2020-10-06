# from __future__ import annotations
# from typing import List
# import numpy as np
# from imgaug.augmentables.kps import Keypoint as ImgAug_Keypoint, KeypointsOnImage as ImgAug_Keypoints
# from logger import logger
from .point import Point2D  # , Point3D, Point2D_List, Point3D_List
# from ..check_utils import check_type, check_type_from_list, \
#     check_value, check_list_length
# from ..base.basic import BasicHandler


class Keypoint2D:
    def __init__(self, point: Point2D, visibility: int):
        # check_type(point, valid_type_list=[Point2D])
        self.point = point
        # check_value(visibility, valid_value_list=[0, 1, 2])
        self.visibility = visibility

#     def __str__(self) -> str:
#         return f"Keypoint2D({self.point.x},{self.point.y},{self.visibility})"
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Keypoint2D:
#         if isinstance(other, (Point2D, int, float)):
#             return Keypoint2D(point=self.point + other, visibility=self.visibility)
#         elif isinstance(other, Keypoint2D):
#             return Keypoint2D(point=self.point + other.point, visibility=int(max(self.visibility, other.visibility)))
#         else:
#             logger.error(f'Cannot add {type(other)} to Keypoint2D')
#             raise TypeError
#
#     def __sub__(self, other) -> Keypoint2D:
#         if isinstance(other, (Point2D, int, float)):
#             return Keypoint2D(point=self.point - other, visibility=self.visibility)
#         elif isinstance(other, Keypoint2D):
#             return Keypoint2D(point=self.point - other.point, visibility=int(max(self.visibility, other.visibility)))
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Keypoint2D')
#             raise TypeError
#
#     def __mul__(self, other) -> Keypoint2D:
#         if isinstance(other, (int, float)):
#             return Keypoint2D(point=self.point * other, visibility=self.visibility)
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Keypoint2D')
#             raise TypeError
#
#     def __truediv__(self, other) -> Keypoint2D:
#         if isinstance(other, (int, float)):
#             return Keypoint2D(point=self.point / other, visibility=self.visibility)
#         else:
#             logger.error(f'Cannot divide {type(other)} from Keypoint2D')
#             raise TypeError
#
#     def __eq__(self, other: Keypoint2D) -> bool:
#         if isinstance(other, Keypoint2D):
#             return self.point == other.point and self.visibility == other.visibility
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, kpt: Keypoint2D) -> Keypoint2D:
#         return kpt
#
#     def copy(self) -> Keypoint2D:
#         return Keypoint2D(point=self.point, visibility=self.visibility)
#
#     def to_list(self) -> list:
#         return self.point.to_list() + [self.visibility]
#
#     @classmethod
#     def from_list(cls, val_list: list) -> Keypoint2D:
#         check_list_length(val_list, correct_length=3, ineq_type='eq')
#         return Keypoint2D(
#             point=Point2D.from_list(val_list[:2]),
#             visibility=val_list[2]
#         )
#
#     def to_numpy(self) -> np.ndarray:
#         return np.array(self.to_list)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray) -> Keypoint2D:
#         return cls.from_list(arr.tolist())
#
#     def to_imgaug(self) -> ImgAug_Keypoint:
#         return ImgAug_Keypoint(x=self.point.x, y=self.point.y)
#
#     @classmethod
#     def from_imgaug(cls, imgaug_kpt: ImgAug_Keypoint, visibility: int = 2) -> Keypoint2D:
#         return Keypoint2D(point=Point2D(x=imgaug_kpt.x, y=imgaug_kpt.y), visibility=visibility)
#
#     @classmethod
#     def origin(cls, x: float = 0.0, y: float = 0.0, v: int = 0) -> Keypoint2D:
#         return Keypoint2D(point=Point2D(x=x, y=y), visibility=v)
#
#
# class Keypoint3D:
#     def __init__(self, point: Point3D, visibility: int):
#         check_type(point, valid_type_list=[Point3D])
#         self.point = point
#         check_value(visibility, valid_value_list=[0, 1, 2])
#         self.visibility = visibility
#
#     def __str__(self) -> str:
#         return f"Keypoint3D({self.point.x},{self.point.y},{self.point.z},{self.visibility})"
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Keypoint3D:
#         if isinstance(other, (Point3D, int, float)):
#             return Keypoint3D(point=self.point + other, visibility=self.visibility)
#         elif isinstance(other, Keypoint3D):
#             return Keypoint3D(point=self.point + other.point, visibility=int(max(self.visibility, other.visibility)))
#         else:
#             logger.error(f'Cannot add {type(other)} to Keypoint3D')
#             raise TypeError
#
#     def __sub__(self, other) -> Keypoint3D:
#         if isinstance(other, (Point3D, int, float)):
#             return Keypoint3D(point=self.point - other, visibility=self.visibility)
#         elif isinstance(other, Keypoint3D):
#             return Keypoint3D(point=self.point - other.point, visibility=int(max(self.visibility, other.visibility)))
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Keypoint3D')
#             raise TypeError
#
#     def __mul__(self, other) -> Keypoint3D:
#         if isinstance(other, (int, float)):
#             return Keypoint3D(point=self.point * other, visibility=self.visibility)
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Keypoint3D')
#             raise TypeError
#
#     def __truediv__(self, other) -> Keypoint3D:
#         if isinstance(other, (int, float)):
#             return Keypoint3D(point=self.point / other, visibility=self.visibility)
#         else:
#             logger.error(f'Cannot divide {type(other)} from Keypoint3D')
#             raise TypeError
#
#     def __eq__(self, other: Keypoint3D) -> bool:
#         if isinstance(other, Keypoint3D):
#             return self.point == other.point and self.visibility == other.visibility
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, kpt: Keypoint3D) -> Keypoint3D:
#         return kpt
#
#     def copy(self) -> Keypoint3D:
#         return Keypoint3D(point=self.point, visibility=self.visibility)
#
#     def to_list(self) -> list:
#         return self.point.to_list() + [self.visibility]
#
#     @classmethod
#     def from_list(cls, val_list: list) -> Keypoint3D:
#         check_list_length(val_list, correct_length=4, ineq_type='eq')
#         return Keypoint3D(
#             point=Point3D.from_list(val_list[:3]),
#             visibility=val_list[3]
#         )
#
#     def to_numpy(self) -> np.ndarray:
#         return np.array(self.to_list)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray) -> Keypoint3D:
#         return cls.from_list(arr.tolist())
#
#     @classmethod
#     def origin(cls, x: float = 0.0, y: float = 0.0, z: float = 0.0, v: int = 0) -> Keypoint3D:
#         return Keypoint3D(point=Point3D(x=x, y=y, z=z), visibility=v)
#
#
# class Keypoint2D_List(BasicHandler['Keypoint2D_List', 'Keypoint2D']):
#     def __init__(self, kpt_list: List[Keypoint2D] = None):
#         super().__init__(obj_type=Keypoint2D, obj_list=kpt_list)
#         self.kpt_list = self.obj_list
#
#     def __str__(self) -> str:
#         return str(self.to_list(demarcation=False))
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Keypoint2D_List:
#         if isinstance(other, (Keypoint2D, Point2D, int, float)):
#             return Keypoint2D_List(kpt_list=[kpt + other for kpt in self])
#         else:
#             logger.error(f'Cannot add {type(other)} to Keypoint2D_List')
#             raise TypeError
#
#     def __sub__(self, other) -> Keypoint2D_List:
#         if isinstance(other, (Keypoint2D, Point2D, int, float)):
#             return Keypoint2D_List(kpt_list=[kpt - other for kpt in self])
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Keypoint2D_List')
#             raise TypeError
#
#     def __mul__(self, other) -> Keypoint2D_List:
#         if isinstance(other, (int, float)):
#             return Keypoint2D_List(kpt_list=[kpt * other for kpt in self])
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Keypoint2D_List')
#             raise TypeError
#
#     def __truediv__(self, other) -> Keypoint2D_List:
#         if isinstance(other, (int, float)):
#             return Keypoint2D_List(kpt_list=[kpt / other for kpt in self])
#         else:
#             logger.error(f'Cannot divide {type(other)} from Keypoint2D_List')
#             raise TypeError
#
#     def __eq__(self, other: Keypoint2D_List) -> bool:
#         if isinstance(other, Keypoint2D_List):
#             return all([kpt0 == kpt1 for kpt0, kpt1 in zip(self, other)])
#         else:
#             return NotImplemented
#
#     def to_numpy(self, demarcation: bool = False) -> np.ndarray:
#         if demarcation:
#             return np.array([kpt.to_list() for kpt in self])
#         else:
#             return np.array([kpt.to_list() for kpt in self]).reshape(-1)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray, demarcation: bool = False) -> Keypoint2D_List:
#         if demarcation:
#             if arr.shape[-1] != 3:
#                 logger.error(f"arr.shape[-1] != 3")
#                 raise Exception
#             return Keypoint2D_List(
#                 kpt_list=[Keypoint2D.from_numpy(arr_part) for arr_part in arr]
#             )
#         else:
#             if len(arr.shape) != 1:
#                 logger.error(f"Expecting flat array when demarcation=False")
#                 logger.error(f"arr.shape: {arr.shape}")
#                 raise Exception
#             elif arr.shape[0] % 3 != 0:
#                 logger.error(f"arr.shape[0] % 3 == {arr.shape[0]} % 3 == {arr.shape[0] % 3} != 0")
#                 raise Exception
#             return Keypoint2D_List(
#                 kpt_list=[Keypoint2D.from_numpy(arr_part) for arr_part in arr.reshape(-1, 3)]
#             )
#
#     def to_list(self, demarcation: bool = False) -> list:
#         return self.to_numpy(demarcation=demarcation).tolist()
#
#     @classmethod
#     def from_list(cls, value_list: list, demarcation: bool = False) -> Keypoint2D_List:
#         return cls.from_numpy(arr=np.array(value_list), demarcation=demarcation)
#
#     def to_imgaug(self, img_shape: list) -> ImgAug_Keypoints:
#         return ImgAug_Keypoints(
#             keypoints=[kpt.to_imgaug() for kpt in self],
#             shape=img_shape
#         )
#
#     @classmethod
#     def from_imgaug(cls, imgaug_kpts: ImgAug_Keypoints) -> Keypoint2D_List:
#         return Keypoint2D_List(
#             kpt_list=[Keypoint2D.from_imgaug(imgaug_kpt) for imgaug_kpt in imgaug_kpts.keypoints]
#         )
#
#     def to_point_list(self) -> Point2D_List:
#         return Point2D_List([kpt.point for kpt in self])
#
#
# class Keypoint3D_List(BasicHandler['Keypoint3D_List', 'Keypoint3D']):
#     def __init__(self, kpt_list: List[Keypoint3D] = None):
#         super().__init__(obj_type=Keypoint3D, obj_list=kpt_list)
#         self.kpt_list = self.obj_list
#
#     def __str__(self) -> str:
#         return str(self.to_list(demarcation=False))
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#     def __add__(self, other) -> Keypoint3D_List:
#         if isinstance(other, (Keypoint3D, Point3D, int, float)):
#             return Keypoint3D_List(kpt_list=[kpt + other for kpt in self])
#         else:
#             logger.error(f'Cannot add {type(other)} to Keypoint3D_List')
#             raise TypeError
#
#     def __sub__(self, other) -> Keypoint3D_List:
#         if isinstance(other, (Keypoint3D, Point3D, int, float)):
#             return Keypoint3D_List(kpt_list=[kpt - other for kpt in self])
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Keypoint3D_List')
#             raise TypeError
#
#     def __mul__(self, other) -> Keypoint3D_List:
#         if isinstance(other, (int, float)):
#             return Keypoint3D_List(kpt_list=[kpt * other for kpt in self])
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Keypoint3D_List')
#             raise TypeError
#
#     def __truediv__(self, other) -> Keypoint3D_List:
#         if isinstance(other, (int, float)):
#             return Keypoint3D_List(kpt_list=[kpt / other for kpt in self])
#         else:
#             logger.error(f'Cannot divide {type(other)} from Keypoint3D_List')
#             raise TypeError
#
#     def __eq__(self, other: Keypoint3D_List) -> bool:
#         if isinstance(other, Keypoint3D_List):
#             return all([kpt0 == kpt1 for kpt0, kpt1 in zip(self, other)])
#         else:
#             return NotImplemented
#
#     def to_numpy(self, demarcation: bool = False) -> np.ndarray:
#         if demarcation:
#             return np.array([kpt.to_list() for kpt in self])
#         else:
#             return np.array([kpt.to_list() for kpt in self]).reshape(-1)
#
#     @classmethod
#     def from_numpy(cls, arr: np.ndarray, demarcation: bool = False) -> Keypoint3D_List:
#         if demarcation:
#             if arr.shape[-1] != 4:
#                 logger.error(f"arr.shape[-1] != 4")
#                 raise Exception
#             return Keypoint3D_List(
#                 kpt_list=[Keypoint3D.from_numpy(arr_part) for arr_part in arr]
#             )
#         else:
#             if len(arr.shape) != 1:
#                 logger.error(f"Expecting flat array when demarcation=False")
#                 logger.error(f"arr.shape: {arr.shape}")
#                 raise Exception
#             elif arr.shape[0] % 4 != 0:
#                 logger.error(f"arr.shape[0] % 4 == {arr.shape[0]} % 4 == {arr.shape[0] % 4} != 0")
#                 raise Exception
#             return Keypoint3D_List(
#                 kpt_list=[Keypoint3D.from_numpy(arr_part) for arr_part in arr.reshape(-1, 4)]
#             )
#
#     def to_list(self, demarcation: bool = False) -> list:
#         return self.to_numpy(demarcation=demarcation).tolist()
#
#     @classmethod
#     def from_list(cls, value_list: list, demarcation: bool = False) -> Keypoint3D_List:
#         return cls.from_numpy(arr=np.array(value_list), demarcation=demarcation)
#
#     def to_point_list(self) -> Point3D_List:
#         return Point3D_List([kpt.point for kpt in self])