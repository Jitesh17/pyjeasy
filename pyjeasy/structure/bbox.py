# from __future__ import annotations
from numpy import floor, ceil
# from pandas.conftest import cls

from .point import Point2D  # , Point2D_List
from .keypoint import Keypoint2D


class BBox:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def __str__(self):
        class_string = str(type(self)).replace("<class '", "").replace("'>", "").split('.')[-1]
        return f"{class_string}: (xmin, ymin, xmax, ymax)=({self.xmin}, {self.ymin}, {self.xmax}, {self.ymax})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: BBox) -> BBox:
        if isinstance(other, BBox):
            xmin = min(self.xmin, other.xmin)
            ymin = min(self.ymin, other.ymin)
            xmax = max(self.xmax, other.xmax)
            ymax = max(self.ymax, other.ymax)
            return BBox(xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax).to_float()
        elif isinstance(other, (int, float)):
            return BBox(xmin=self.xmin + other, ymin=self.ymin + other, xmax=self.xmax + other, ymax=self.ymax + other)
        elif isinstance(other, Point2D):
            return BBox(xmin=self.xmin + other.x, ymin=self.ymin + other.y, xmax=self.xmax + other.x,
                        ymax=self.ymax + other.y)
        elif isinstance(other, Keypoint2D):
            return BBox(xmin=self.xmin + other.point.x, ymin=self.ymin + other.point.y, xmax=self.xmax + other.point.x,
                        ymax=self.ymax + other.point.y)
        else:
            # logger.error(f'Cannot add {type(other)} to BBox')
            raise TypeError

    #
    # def __sub__(self, other) -> BBox: if isinstance(other, BBox): raise NotImplementedError elif isinstance(other,
    # (int, float)): return BBox(xmin=self.xmin-other, ymin=self.ymin-other, xmax=self.xmax-other,
    # ymax=self.ymax-other) elif isinstance(other, Point2D): return BBox(xmin=self.xmin-other.x,
    # ymin=self.ymin-other.y, xmax=self.xmax-other.x, ymax=self.ymax-other.y) elif isinstance(other, Keypoint2D):
    # return BBox(xmin=self.xmin-other.point.x, ymin=self.ymin-other.point.y, xmax=self.xmax-other.point.x,
    # ymax=self.ymax-other.point.y) else: logger.error(f'Cannot subtract {type(other)} from BBox') raise TypeError
    #
    # def __mul__(self, other) -> BBox:
    #     if isinstance(other, (int, float)):
    #         return BBox(xmin=self.xmin*other, ymin=self.ymin*other, xmax=self.xmax*other, ymax=self.ymax*other)
    #     else:
    #         logger.error(f'Cannot multiply {type(other)} with BBox')
    #         raise TypeError
    #
    #
    # def __truediv__(self, other) -> BBox:
    #     if isinstance(other, (int, float)):
    #         return BBox(xmin=self.xmin/other, ymin=self.ymin/other, xmax=self.xmax/other, ymax=self.ymax/other)
    #     else:
    #         logger.error(f'Cannot divide {type(other)} from BBox')
    #         raise TypeError
    #
    # def __eq__(self, other: BBox) -> bool: if isinstance(other, BBox): return self.xmin == other.xmin and self.ymin
    # == other.ymin and self.xmax == other.xmax and self.ymax == other.ymax else: return NotImplemented

    @classmethod
    def buffer(cls, bbox: cls) -> cls:
        return bbox

    def copy(self) -> cls:
        return BBox(
            xmin=self.xmin,
            ymin=self.ymin,
            xmax=self.xmax,
            ymax=self.ymax
        )

    def to_int(self) -> BBox:
        return BBox(
            xmin=int(self.xmin),
            ymin=int(self.ymin),
            xmax=int(self.xmax),
            ymax=int(self.ymax)
        )

    def to_rounded_int(self, special: bool = False) -> BBox:
        """Rounds BBox object to have integer coordinates.

        Keyword Arguments: special {bool} -- [Round xmin and ymin down using floor, and round xmax and ymax using
        ceil.] (default: {False})

        Returns:
            BBox -- [description]
        """
        if not special:
            return BBox(
                xmin=round(self.xmin),
                ymin=round(self.ymin),
                xmax=round(self.xmax),
                ymax=round(self.ymax)
            )
        else:
            return BBox(
                xmin=floor(self.xmin),
                ymin=floor(self.ymin),
                xmax=ceil(self.xmax),
                ymax=ceil(self.ymax)
            )

    def to_float(self) -> BBox:
        return BBox(
            xmin=float(self.xmin),
            ymin=float(self.ymin),
            xmax=float(self.xmax),
            ymax=float(self.ymax)
        )

    def shape(self) -> list:
        """
        return [height, width]
        """
        width = self.xmax - self.xmin
        height = self.ymax - self.ymin
        return [height, width]

    def to_list(self, output_format: str = 'pminpmax') -> list:
        """
        output_format options:
            'pminpmax': [xmin, ymin, xmax, ymax]
            'pminsize': [xmin, ymin, width, height]
        """
        # check_value(output_format, valid_value_list=['pminpmax', 'pminsize'])
        if output_format == 'pminpmax':
            return [self.xmin, self.ymin, self.xmax, self.ymax]
        elif output_format == 'pminsize':
            bbox_h, bbox_w = self.shape()
            return [self.xmin, self.ymin, bbox_w, bbox_h]
        else:
            raise Exception

    @classmethod
    def from_list(cls, bbox: list, input_format: str = 'pminpmax') -> BBox:
        """
        input_format options:
            'pminpmax': [xmin, ymin, xmax, ymax]
            'pminsize': [xmin, ymin, width, height]
        """
        # check_value(input_format, valid_value_list=['pminpmax', 'pminsize'])
        if input_format == 'pminpmax':
            xmin, ymin, xmax, ymax = bbox
            return BBox(xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax)
        elif input_format == 'pminsize':
            xmin, ymin, bbox_w, bbox_h = bbox
            xmax, ymax = xmin + bbox_w, ymin + bbox_h
            return BBox(xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax)
        else:
            raise Exception
