from __future__ import annotations

# from typing import List
import numpy as np


# import cv2
# from shapely.geometry import Point as ShapelyPoint
# from shapely.geometry.polygon import Polygon as ShapelyPolygon
# from shapely.ops import cascaded_union, unary_union, polygonize
# from shapely.geometry import LineString
# from imgaug.augmentables.polys import Polygon as ImgAugPolygon, PolygonsOnImage as ImgAugPolygons
# import imgaug


# from logger import logger
#
# from ..constants import number_types
# from ..check_utils import check_type, check_type_from_list, check_value
# from ..utils import get_class_string

# from .point import Point, Point2D_List, Point3D_List, Point2D, Point3D
# from .keypoint import Keypoint2D, Keypoint3D
# from .bbox import BBox


class Polygon:
    def __init__(self, points: list, dimensionality: int = 2):
        # check_type(item=points, valid_type_list=[list])
        # check_type_from_list(item_list=points, valid_type_list=number_types)
        # check_type(item=dimensionality, valid_type_list=[int])

        if isinstance(points, np.ndarray):
            # self.points = points.tolist()
            self.points = points
        elif isinstance(points, list):
            self.points = points
        else:
            # logger.error(f'Expected type(points) in [list, np.ndarray]')
            raise Exception
        self.dimensionality = dimensionality
        self._check_valid()

    def _check_valid(self):
        if len(self.points) % self.dimensionality != 0:
            # logger.error(f"len(self.points) is not divisible by self.dimensionality={self.dimensionality}")
            raise Exception
#
#     def __len__(self) -> int:
#         return len(self.points) // self.dimensionality
#
#     def has_valid_num_points(self) -> bool:
#         return len(self) >= 3
#
#     def check_valid_num_points(self):
#         if self.has_valid_num_points():
#             logger.error(f'A polygon must be defined by at least 3 points.')
#             logger.error(f'len(self.points) // self.dimensionality == {len(self.points) // self.dimensionality} < 3')
#             raise Exception
#
#     def __str__(self):
#         return f"{get_class_string(self)}: {self.points}"
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other) -> Polygon:
#         if isinstance(other, Point2D) and self.dimensionality == 2:
#             return Polygon.from_point2d_list(
#                 point2d_list=Point2D_List([point + other for point in self.to_point2d_list()]))
#         elif isinstance(other, Keypoint2D) and self.dimensionality == 2:
#             return Polygon.from_point2d_list(
#                 point2d_list=Point2D_List([point + other.point for point in self.to_point2d_list()]))
#         elif isinstance(other, Point3D) and self.dimensionality == 3:
#             return Polygon.from_point3d_list(
#                 point3d_list=Point3D_List([point + other for point in self.to_point3d_list()]))
#         elif isinstance(other, Keypoint3D) and self.dimensionality == 3:
#             return Polygon.from_point3d_list(
#                 point3d_list=Point3D_List([point + other.point for point in self.to_point3d_list()]))
#         elif isinstance(other, (int, float)):
#             return Polygon.from_list(
#                 points=[val + other for val in self.to_list(demarcation=False)],
#                 dimensionality=self.dimensionality, demarcation=False
#             )
#         else:
#             logger.error(f'Cannot add {type(other)} to Polygon')
#             raise TypeError
#
#     def __sub__(self, other) -> Polygon:
#         if isinstance(other, Point2D) and self.dimensionality == 2:
#             return Polygon.from_point2d_list(
#                 point2d_list=Point2D_List([point - other for point in self.to_point2d_list()]))
#         elif isinstance(other, Keypoint2D) and self.dimensionality == 2:
#             return Polygon.from_point2d_list(
#                 point2d_list=Point2D_List([point - other.point for point in self.to_point2d_list()]))
#         elif isinstance(other, Point3D) and self.dimensionality == 3:
#             return Polygon.from_point3d_list(
#                 point3d_list=Point3D_List([point - other for point in self.to_point3d_list()]))
#         elif isinstance(other, Keypoint3D) and self.dimensionality == 3:
#             return Polygon.from_point3d_list(
#                 point3d_list=Point3D_List([point - other.point for point in self.to_point3d_list()]))
#         elif isinstance(other, (int, float)):
#             return Polygon.from_list(
#                 points=[val - other for val in self.to_list(demarcation=False)],
#                 dimensionality=self.dimensionality, demarcation=False
#             )
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Polygon')
#             raise TypeError
#
#     def __mul__(self, other) -> Polygon:
#         if isinstance(other, (int, float)):
#             return Polygon.from_list(
#                 points=[val * other for val in self.to_list(demarcation=False)],
#                 dimensionality=self.dimensionality, demarcation=False
#             )
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Polygon')
#             raise TypeError
#
#     def __truediv__(self, other) -> Polygon:
#         if isinstance(other, (int, float)):
#             return Polygon.from_list(
#                 points=[val / other for val in self.to_list(demarcation=False)],
#                 dimensionality=self.dimensionality, demarcation=False
#             )
#         else:
#             logger.error(f'Cannot divide {type(other)} from Polygon')
#             raise TypeError
#
#     def __eq__(self, other: Polygon) -> bool:
#         if isinstance(other, Polygon):
#             vals = self.to_list(demarcation=False)
#             other_vals = other.to_list(demarcation=False)
#             return len(vals) == len(other_vals) and all([val0 == val1 for val0, val1 in zip(vals, other_vals)])
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, polygon: Polygon) -> Polygon:
#         return polygon
#
#     def copy(self) -> Polygon:
#         return Polygon(points=self.points, dimensionality=self.dimensionality)
#
#     def to_int(self) -> Polygon:
#         return Polygon(points=[int(val) for val in self.points], dimensionality=self.dimensionality)
#
#     def to_float(self) -> Polygon:
#         return Polygon(points=[float(val) for val in self.points], dimensionality=self.dimensionality)
#
#     def to_list(self, demarcation: bool = False) -> list:
#         if demarcation:
#             return np.array(self.points).reshape(-1, self.dimensionality).tolist()
#         else:
#             return self.points
#
#     def to_point_list(self) -> list:
#         return [Point(coords=coords) for coords in self.to_list(demarcation=True)]
#
#     def to_shapely(self) -> ShapelyPolygon:
#         return ShapelyPolygon(self.to_list(demarcation=True))
#
    def to_contour(self) -> np.ndarray:
        return np.array(self.to_int().to_list()).reshape(-1, 1, self.dimensionality)
#
#     def to_bbox(self) -> BBox:
#         points = np.array(self.to_list(demarcation=True))
#         xmin, ymin = points.min(axis=0)
#         xmax, ymax = points.max(axis=0)
#         return BBox(xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax)
#
#     def area(self) -> float:
#         return self.to_shapely().area
#
#     def centroid(self) -> Point:
#         return Point.from_shapely(self.to_shapely().centroid)
#
#     def contains_point(self, point: Point) -> bool:
#         return self.to_shapely().contains(point.to_shapely())
#
#     def contains_polygon(self, polygon: Polygon) -> bool:
#         return self.to_shapely().contains(polygon.to_shapely())
#
#     def contains_bbox(self, bbox: BBox) -> bool:
#         return self.to_shapely().contains(bbox.to_shapely())
#
#     def contains(self, obj) -> bool:
#         check_type(item=obj, valid_type_list=[Point, Polygon, BBox])
#         return self.to_shapely().contains(obj.to_shapely())
#
#     def within_polygon(self, polygon: Polygon) -> bool:
#         return self.to_shapely().within(polygon.to_shapely())
#
#     def within_bbox(self, bbox: BBox) -> bool:
#         return self.to_shapely().within(bbox.to_shapely())
#
#     def within(self, obj) -> bool:
#         check_type(item=obj, valid_type_list=[Polygon, BBox])
#         return self.to_shapely().within(obj.to_shapely())
#
#     def intersects_polygon(self, polygon: Polygon) -> bool:
#         return self.to_shapely().intersects(polygon)
#
#     def size(self) -> tuple:
#         return np.array(self.points).reshape(-1, self.dimensionality).shape
#
#     def resize(self, orig_frame_shape: list, new_frame_shape: list) -> Polygon:
#         if self.dimensionality != 2:
#             logger.error(f"Only resize of dimensionality 2 is supported at this time.")
#             logger.error(f"This polygon is dimensionality: {self.dimensionality}")
#             raise Exception
#         orig_frame_h, orig_frame_w = orig_frame_shape[:2]
#         new_frame_h, new_frame_w = new_frame_shape[:2]
#         h_scale = new_frame_h / orig_frame_h
#         w_scale = new_frame_w / orig_frame_w
#         new_point_list = []
#         for point in self.to_point_list():
#             point = Point.buffer(point)
#             [x, y] = point.coords
#             x *= w_scale
#             y *= h_scale
#             new_point = Point([x, y])
#             new_point_list.append(new_point)
#         return Polygon.from_point_list(point_list=new_point_list, dimensionality=2)
#
#     @classmethod
#     def from_list(self, points: list, dimensionality: int = 2, demarcation: bool = False) -> Polygon:
#         if demarcation:
#             flattened_list = np.array(points).reshape(-1).tolist()
#             return Polygon(points=flattened_list, dimensionality=dimensionality)
#         else:
#             return Polygon(points=points, dimensionality=dimensionality)
#
# @classmethod def from_point_list(self, point_list: list, dimensionality: int = 2) -> Polygon: check_type_from_list(
# item_list=point_list, valid_type_list=[Point]) result = [] for i, point in enumerate(point_list): numpy_array =
# np.array(point.to_list()) if numpy_array.shape != (dimensionality,): logger.error( f"Found point at index {i} of
# point_list with a shape of {numpy_array.shape} != {(dimensionality,)}") raise Exception result.extend(
# point.to_list()) return Polygon(points=result, dimensionality=dimensionality)
#
#     @classmethod
#     def fix_shapely_invalid(self, shapely_polygon: ShapelyPolygon) -> ShapelyPolygon:
#         line_non_simple = LineString(shapely_polygon.exterior.coords)
#         mls = unary_union(line_non_simple)
#         polygons = list(polygonize(mls))
#         return polygons[0]
#
#     @classmethod
#     def from_shapely(self, shapely_polygon: ShapelyPolygon, fix_invalid: bool = False) -> Polygon:
#         if not shapely_polygon.is_valid and fix_invalid:
#             shapely_polygon = Polygon.fix_shapely_invalid(shapely_polygon)
#
#         vals_tuple = shapely_polygon.exterior.coords.xy
#         numpy_array = np.array(vals_tuple).T[:-1]
#         flattened_list = numpy_array.reshape(-1).tolist()
#         dimensionality = numpy_array.shape[1]
#         return Polygon(points=flattened_list, dimensionality=dimensionality)
#
#     @classmethod
#     def from_contour(self, contour: np.ndarray) -> Polygon:
#         cont = contour.reshape(contour.shape[0], contour.shape[2]).tolist()
#         return self.from_list(points=cont, dimensionality=2, demarcation=True)
#
#     @classmethod
#     def from_polygon_list_to_merge(self, polygon_list: list) -> Polygon:
#         from shapely.geometry import MultiPolygon as ShapelyMultiPolygon
#         import matplotlib.pyplot as plt
#         import geopandas as gpd
#
#         valid_polygon_list = []
#         for polygon in polygon_list:
#             if polygon.size()[0] > 2:  # Filter out polygons with less than 3 vertices.
#                 valid_polygon_list.append(polygon)
#         # logger.red(valid_polygon_list)
#         merged_polygon = None
#         for i, valid_polygon in enumerate(valid_polygon_list):
#             if merged_polygon is None:
#                 merged_polygon = valid_polygon.to_shapely()
#                 logger.yellow(f"{i + 1}/{len(valid_polygon_list)}: type(merged_polygon): {type(merged_polygon)}")
#             else:
#                 if merged_polygon.intersects(valid_polygon.to_shapely()):
#                     logger.green(f"intersects!")
#                 else:
#                     logger.red(f"Not intersects!")
#                 if type(merged_polygon) is ShapelyPolygon:
#                     logger.cyan(f"Flag0")
#                     polygons = gpd.GeoSeries(merged_polygon)
#                     new_polygon = gpd.GeoSeries(valid_polygon.to_shapely())
#                     polygons.plot()
#                     new_polygon.plot()
#                     plt.show()
#                     if not merged_polygon.is_valid:
#                         logger.error(f"merged_polygon is not valid")
#                         raise Exception
#                     if not valid_polygon.to_shapely().is_valid:
#                         logger.error(f"New polygon is not valid")
#                         raise Exception
#                     if merged_polygon.intersects(valid_polygon.to_shapely()):
#                         merged_polygon = merged_polygon.union(valid_polygon.to_shapely())
#                     else:
#                         merged_polygon = cascaded_union([merged_polygon, valid_polygon.to_shapely()])
#                     if type(merged_polygon) is ShapelyMultiPolygon:
#                         logger.cyan(f"Hull")
#                         merged_polygon = merged_polygon.convex_hull
#                         if type(merged_polygon) is ShapelyPolygon:
#                             logger.green(f"Fixed!")
#                         elif type(merged_polygon) is ShapelyMultiPolygon:
#                             logger.error(f"Not Fixed!")
#                             raise Exception
#                         else:
#                             logger.error(f"Unknown type: {type(merged_polygon)}")
#                             raise Exception
#                 elif type(merged_polygon) is ShapelyMultiPolygon:
#                     logger.error(f"Polygon turned into MultiPolygon in shapely!")
#                     raise Exception
#                 else:
#                     logger.error(f"type(merged_polygon): {type(merged_polygon)}")
#                     raise Exception
#
# logger.yellow(f"{i + 1}/{len(valid_polygon_list)}: type(merged_polygon): {type(merged_polygon)}") # logger.yellow(
# f"{i+1}/{len(valid_polygon_list)}: type(merged_polygon.exterior): {type(merged_polygon.exterior)}") logger.blue(f"{
# i + 1}/{len(valid_polygon_list)}: valid_polygon.size(): {valid_polygon.size()}")
#
#         import sys
#         sys.exit()
#         union = cascaded_union([valid_polygon.to_shapely() for valid_polygon in valid_polygon_list])
#         return self.from_shapely(union)
#
#     def to_imgaug(self) -> ImgAugPolygon:
#         if self.dimensionality == 2:
#             return ImgAugPolygon(self.to_list(demarcation=True))
#         else:
#             raise NotImplementedError
#
#     @classmethod
#     def from_imgaug(cls, imgaug_polygon: ImgAugPolygon, fix_invalid: bool = False) -> Polygon:
#         return Polygon.from_shapely(imgaug_polygon.to_shapely_polygon(), fix_invalid=fix_invalid)
#
#     def to_point2d_list(self) -> Point2D_List:
#         if self.dimensionality != 2:
#             logger.error(
#                 f'Cannot convert polygon to Point2D_List because self.dimensionality=={self.dimensionality}!=2')
#             raise TypeError
#         return Point2D_List.from_list(self.to_list(demarcation=True))
#
#     @classmethod
#     def from_point2d_list(cls, point2d_list: Point2D_List) -> Polygon:
#         check_type(point2d_list, valid_type_list=[Point2D_List])
#         return Polygon.from_list(
#             points=point2d_list.to_list(demarcation=True),
#             dimensionality=2,
#             demarcation=True
#         )
#
#     def to_point3d_list(self) -> Point3D_List:
#         if self.dimensionality != 3:
#             logger.error(
#                 f'Cannot convert polygon to Point3D_List because self.dimensionality=={self.dimensionality}!=3')
#             raise TypeError
#         return Point3D_List.from_list(self.to_list(demarcation=True))
#
#     @classmethod
#     def from_point3d_list(cls, point3d_list: Point3D_List) -> Polygon:
#         check_type(point3d_list, valid_type_list=[Point3D_List])
#         return Polygon.from_list(
#             points=point3d_list.to_list(demarcation=True),
#             dimensionality=3,
#             demarcation=True
#         )
#
#
# class Segmentation:
#     def __init__(self, polygon_list: list = None):
#         if polygon_list is not None:
#             check_type(item=polygon_list, valid_type_list=[list])
#             check_type_from_list(item_list=polygon_list, valid_type_list=[Polygon])
#             for i, polygon in enumerate(polygon_list):
#                 if polygon.dimensionality != 2:
#                     logger.error(f"Found polygon of dimensionality {polygon.dimensionality} at index {i}")
#                     logger.error(f"All polygons must be of dimensionality 2.")
#                     raise Exception
#             self.polygon_list = polygon_list
#         else:
#             self.polygon_list = []
#
#     def __str__(self):
#         return f"{get_class_string(self)}: {self.polygon_list}"
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __len__(self) -> int:
#         return len(self.polygon_list)
#
#     def __getitem__(self, idx: int) -> Polygon:
#         if len(self.polygon_list) == 0:
#             logger.error(f"polygon_list is empty.")
#             raise IndexError
#         elif idx < 0 or idx >= len(self.polygon_list):
#             logger.error(f"Index out of range: {idx}")
#             raise IndexError
#         else:
#             return self.polygon_list[idx]
#
#     def __setitem__(self, idx: int, value: Polygon):
#         check_type(value, valid_type_list=[Polygon])
#         self.polygon_list[idx] = value
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self) -> Polygon:
#         if self.n < len(self.polygon_list):
#             result = self.polygon_list[self.n]
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#     def __add__(self, other) -> Segmentation:
#         if isinstance(other, Segmentation):
#             # TODO: Figure out why this error is thrown upon the below check.
#             # "ValueError: A LinearRing must have at least 3 coordinate tuples "
#
#             # for poly in self:
#             #     if other.contains(poly):
#             #         logger.error(f'Cannot add two segmentations that overlap.')
#             #         raise Exception
#
#             # TODO: Figure out how to merge polygons properly.
#             return Segmentation(self.polygon_list + other.polygon_list)
#         elif isinstance(other, (Point2D, Keypoint2D, int, float)):
#             return Segmentation([poly + other for poly in self])
#         else:
#             logger.error(f'Cannot add {type(other)} to Segmentation')
#             raise TypeError
#
#     def __sub__(self, other) -> Segmentation:
#         if isinstance(other, (Point2D, Keypoint2D, int, float)):
#             return Segmentation([poly - other for poly in self])
#         else:
#             logger.error(f'Cannot subtract {type(other)} from Segmentation')
#             raise TypeError
#
#     def __mul__(self, other) -> Segmentation:
#         if isinstance(other, (int, float)):
#             return Segmentation([poly * other for poly in self])
#         else:
#             logger.error(f'Cannot multiply {type(other)} with Segmentation')
#             raise TypeError
#
#     def __truediv__(self, other) -> Segmentation:
#         if isinstance(other, (int, float)):
#             return Segmentation([poly / other for poly in self])
#         else:
#             logger.error(f'Cannot divide {type(other)} from Segmentation')
#             raise TypeError
#
#     def __eq__(self, other: Segmentation) -> bool:
#         if isinstance(other, Segmentation):
#             vals = self.to_list(demarcation=False)
#             other_vals = other.to_list(demarcation=False)
#             return len(self) == len(other) and all([poly0 == poly1 for poly0, poly1 in zip(self, other)])
#         else:
#             return NotImplemented
#
#     @classmethod
#     def buffer(self, segmentation: Segmentation) -> Segmentation:
#         return segmentation
#
#     def copy(self) -> Segmentation:
#         return Segmentation(polygon_list=self.polygon_list)
#
#     def append(self, item: Polygon):
#         check_type(item, valid_type_list=[Polygon])
#         self.polygon_list.append(item)
#
#     def to_int(self) -> Segmentation:
#         return Segmentation([polygon.to_int() for polygon in self])
#
#     def to_float(self) -> Segmentation:
#         return Segmentation([polygon.to_float() for polygon in self])
#
#     def to_list(self, demarcation: bool = False) -> list:
#         return [polygon.to_list(demarcation=demarcation) for polygon in self]
#
#     def to_point_list(self) -> list:
#         return [polygon.to_point_list() for polygon in self]
#
#     def to_shapely(self) -> list:
#         return [polygon.to_shapely() for polygon in self]
#
    def to_contour(self) -> list:  # combine?
        return [polygon.to_contour() for polygon in self]
#
#     def to_bbox(self) -> BBox:
#         seg_bbox_list = [polygon.to_bbox() for polygon in self]
#         seg_bbox_xmin = min([seg_bbox.xmin for seg_bbox in seg_bbox_list])
#         seg_bbox_ymin = min([seg_bbox.ymin for seg_bbox in seg_bbox_list])
#         seg_bbox_xmax = max([seg_bbox.xmax for seg_bbox in seg_bbox_list])
#         seg_bbox_ymax = max([seg_bbox.ymax for seg_bbox in seg_bbox_list])
#         result_bbox = BBox(xmin=seg_bbox_xmin, ymin=seg_bbox_ymin, xmax=seg_bbox_xmax, ymax=seg_bbox_ymax).to_float()
#         return result_bbox
#
#     def area(self) -> float:
#         return sum([polygon.area() for polygon in self])
#
#     def centroid(self) -> Point:
#         poly_dim_valid = [polygon.dimensionality == 2 for polygon in self]
#         if False in poly_dim_valid:
#             logger.error(f'Found polygon of dimensionality != 2 in segmentation.')
#             logger.error(f'Dimensionalities found: {[polygon.dimensionality for polygon in self]}')
#             logger.error(f'Cannot calculate centroid.')
#             raise Exception
#         poly_c = [polygon.centroid() for polygon in self]
#         poly_a = [polygon.area() for polygon in self]
#         cxa = [c.coords[0] * a for c, a in zip(poly_c, poly_a)]
#         cya = [c.coords[1] * a for c, a in zip(poly_c, poly_a)]
#         sum_cxa, sum_cya, sum_a = sum(cxa), sum(cya), sum(poly_a)
#         calc_cx, calc_cy = sum_cxa / sum_a, sum_cya / sum_a
#         return Point(coords=[calc_cx, calc_cy])
#
#     def contains_point(self, point: Point) -> bool:
#         return any([polygon.contains_point() for polygon in self])
#
#     def contains_polygon(self, polygon: Polygon) -> bool:
#         return any([polygon.contains_polygon() for polygon in self])
#
#     def contains_bbox(self, bbox: BBox) -> bool:
#         return any([polygon.contains_bbox() for polygon in self])
#
#     def contains(self, obj) -> bool:
#         check_type(item=obj, valid_type_list=[Point, Polygon, BBox])
#         return any([polygon.contains(obj) for polygon in self])
#
#     def within_polygon(self, polygon: Polygon) -> bool:
#         return all([polygon.within_polygon() for polygon in self])
#
#     def within_bbox(self, bbox: BBox) -> bool:
#         return all([polygon.within_bbox(bbox) for polygon in self])
#
# def within(self, obj) -> bool: check_type(item=obj, valid_type_list=[Polygon, BBox]) if type(obj) is BBox:  #
# necessary? bbox_contains_seg = None for polygon in self: if len(polygon.to_list(demarcation=True)) < 3: continue
# poly_in_bbox = obj.contains(polygon) bbox_contains_seg = bbox_contains_seg and poly_in_bbox if bbox_contains_seg is
# not None else poly_in_bbox bbox_contains_seg = bbox_contains_seg if bbox_contains_seg is not None else False return
# bbox_contains_seg elif type(obj) is Polygon:  # necessary? poly_contains_seg = None for polygon in self: if len(
# polygon.to_list(demarcation=True)) < 3: continue poly_in_poly = obj.contains(polygon) poly_contains_seg =
# poly_contains_seg and poly_in_poly if poly_contains_seg is not None else poly_in_poly poly_contains_seg =
# poly_contains_seg if poly_contains_seg is not None else False return poly_contains_seg return all([polygon.within(
# obj) for polygon in self])
#
#     def merge(self) -> Segmentation:
#         return Segmentation(
#             polygon_list=[Polygon.from_polygon_list_to_merge(
#                 polygon_list=self.polygon_list
#             )]
#         )
#
#     def resize(self, orig_frame_shape: list, new_frame_shape: list) -> Segmentation:
#         new_polygon_list = []
#         for polygon in self:
#             polygon = Polygon.buffer(polygon)
#             new_polygon = polygon.resize(
#                 orig_frame_shape=orig_frame_shape, new_frame_shape=new_frame_shape
#             )
#             new_polygon_list.append(new_polygon)
#         return Segmentation(polygon_list=new_polygon_list)
#
#     @classmethod
#     def from_list(self, points_list: list, demarcation: bool = False) -> Segmentation:
#         return Segmentation(
#             polygon_list=[
#                 Polygon.from_list(
#                     points=points, dimensionality=2, demarcation=demarcation
#                 ) for points in points_list
#             ]
#         )
#
#     @classmethod
#     def from_point_list(self, point_list_list: list) -> Segmentation:
#         return Segmentation(
#             polygon_list=[
#                 Polygon.from_point_list(
#                     point_list=point_list, dimensionality=2
#                 ) for point_list in point_list_list
#             ]
#         )
#
#     @classmethod
#     def from_shapely(self, shapely_polygon_list: list) -> Segmentation:
#         shapely_polygon_list0 = shapely_polygon_list.copy()
#         del_idx_list = []
#         for i, shapely_polygon in enumerate(shapely_polygon_list0):
#             if shapely_polygon.size()[0] < 3:
#                 del_idx_list.append(i)
#         for i in del_idx_list[::-1]:
#             del shapely_polygon_list0[i]
#         return Segmentation(
#             polygon_list=[
#                 Polygon.from_shapely(
#                     shapely_polygon=shapely_polygon
#                 ) for shapely_polygon in shapely_polygon_list0
#             ]
#         )
#
#     @classmethod
#     def from_contour(self, contour_list: list, exclude_invalid_polygons: bool = False) -> Segmentation:
#         contour_list0 = contour_list.copy()
#         if exclude_invalid_polygons:
#             del_idx_list = []
#             for i in range(len(contour_list0)):
#                 if len(contour_list0[i]) < 3:
#                     del_idx_list.append(i)
#             for del_idx in del_idx_list[::-1]:
#                 del contour_list0[del_idx]
#
#         return Segmentation(
#             polygon_list=[
#                 Polygon.from_contour(
#                     contour=contour
#                 ) for contour in contour_list0
#             ]
#         )
#
#     def to_imgaug(self, img_shape: np.ndarray) -> ImgAugPolygons:
#         return ImgAugPolygons(
#             polygons=[poly.to_imgaug() for poly in self.polygon_list],
#             shape=img_shape
#         )
#
#     @classmethod
#     def from_imgaug(cls, imgaug_polygons: ImgAugPolygons, fix_invalid: bool = False) -> Segmentation:
#         return Segmentation(
#             polygon_list=[Polygon.from_imgaug(imgaug_polygon, fix_invalid=fix_invalid) for imgaug_polygon in
#                           imgaug_polygons.polygons]
#         )
#
#     def to_point2d_list_list(self) -> List[Point2D_List]:
#         return [polygon.to_point2d_list() for polygon in self]
#
#     @classmethod
#     def from_point2d_list_list(cls, point2d_list_list: List[Point2D_List]) -> Segmentation:
#         return Segmentation(
#             polygon_list=[Polygon.from_point2d_list(point2d_list) for point2d_list in point2d_list_list]
#         )
#
#     @classmethod
#     def __remove_out_of_image(cls, img_aug_polys: ImgAugPolygons, fully: bool = True,
#                               partly: bool = False) -> ImgAugPolygons:
#         result = img_aug_polys.copy()
#         result.remove_out_of_image(fully=fully, partly=partly)
#
#         return result
#
#     def remove_out_of_image(self, img_shape: np.ndarray, fully: bool = True, partly: bool = False) -> Segmentation:
#         """Remove polygons in segmentation that are outside of the frame.
#
#         Arguments:
#             img_shape {np.ndarray} -- [Shape of the frame.]
#
# Keyword Arguments: fully {bool} -- [If true, polygons that are fully outside of the frame will be removed.] (
# default: {True}) partly {bool} -- [If true, polygons that are partially outside of the frame will be removed.] (
# default: {False})
#
#         Returns:
#             [Segmentation] -- [Segmentation object]
#         """
#         if len(self) > 0:
#             result = self.to_imgaug(img_shape)
#             result = self.__remove_out_of_image(result, fully=fully, partly=partly)
#             result = self.__prune_imgaug_polys(result, img_shape=img_shape)
#             return Segmentation.from_imgaug(result)
#         else:
#             return self
#
#     @classmethod
#     def __clip_out_of_image(cls, img_aug_polys: ImgAugPolygons) -> ImgAugPolygons:
#         result = img_aug_polys.copy()
#         result.clip_out_of_image()
#
#         return result
#
#     def clip_out_of_image(self, img_shape: np.ndarray) -> Segmentation:
#         """Clip off all parts from all polygons that are outside of an image.
#
#         .. note::
#
#             The result can contain fewer polygons than the input did. That
#             happens when a polygon is fully outside of the image plane.
#
#         .. note::
#
#             The result can also contain *more* polygons than the input
#             did. That happens when distinct parts of a polygon are only
#             connected by areas that are outside of the image plane and hence
#             will be clipped off, resulting in two or more unconnected polygon
#             parts that are left in the image plane.
#
#         Returns
#         -------
#         Segmentation object
#
#         """
#         if len(self) > 0:
#             result = self.to_imgaug(img_shape)
#             result = self.__clip_out_of_image(result)
#             result = self.__prune_imgaug_polys(result, img_shape=img_shape)
#             return Segmentation.from_imgaug(result)
#         else:
#             return self
#
# @classmethod def __get_multipoly_inter_shapely(cls, imgaug_polys: ImgAugPolygons, img_shape: np.ndarray) -> list:
# h, w = img_shape[:2] result = [] for imgaug_poly in imgaug_polys: if imgaug_poly.coords.shape[0] < 3:
# logger.warning( f'Encountered imgaug_poly.coords.shape[0] < 3. imgaug_poly.coords.shape={
# imgaug_poly.coords.shape}') logger.warning(f'Ignoring polygon.') continue poly_shapely =
# imgaug_poly.to_shapely_polygon() poly_image = shapely.geometry.Polygon([(0, 0), (w, 0), (w, h), (0,
# h)]) multipoly_inter_shapely = poly_shapely.intersection(poly_image) result.append(multipoly_inter_shapely) return
# result
#
#     @classmethod
#     def __prune_imgaug_polys(cls, imgaug_polys: ImgAugPolygons, img_shape: np.ndarray) -> ImgAugPolygons:
#         multipoly_inter_shapely = cls.__get_multipoly_inter_shapely(imgaug_polys=imgaug_polys, img_shape=img_shape)
#         polys = [ImgAugPolygon.from_shapely(shape_obj) for shape_obj in multipoly_inter_shapely if
#                  type(shape_obj) is ShapelyPolygon]
#         return ImgAugPolygons(polys, shape=img_shape)
#
#     def imgaug_based_prune(self, img_shape: np.ndarray, fully: bool = True, partly: bool = False) -> Segmentation:
#         """Removes all polygons that are fully outside of the frame, and then crops out
#         the portions of the remaining polygons that are outside of the frame.
#         It also deletes any Non-Polygon shapes that are generated as a result.
#
#         Arguments:
#             img_shape {np.ndarray} -- [Size of frame]
#
#         Returns:
#             Segmentation -- [Segmentation object]
#         """
#         result = self.to_imgaug(img_shape)
#         result = self.__remove_out_of_image(result, fully=fully, partly=partly)
#         result = self.__prune_imgaug_polys(result, img_shape=img_shape)
#         result = self.__clip_out_of_image(result)
#         return result
