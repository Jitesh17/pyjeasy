# from __future__ import annotations
import cv2
import numpy as np
from pyjeasy.image_utils.edit import resize_img
from torch._C import Size

from jaitool.structures.bbox import BBox
from pyjeasy.check_utils import check_value
import printj
from printj import red as error


# from ..bbox import BBox


def draw_bbox(
        img: np.ndarray, bbox: BBox,
        color=None, thickness: int = 2, text: str = None, label_thickness: int = None,
        label_color: list = None, show_bbox: bool = True, show_label: bool = True,
        label_orientation: str = 'top'
) -> np.ndarray:
    if color is None:
        color = [0, 255, 255]
    result = img.copy()
    print(type(bbox))
    if type(bbox) == BBox:
        xmin, ymin, xmax, ymax = bbox.to_int().to_list()
    elif type(bbox) == tuple:
        xmin, ymin, xmax, ymax = bbox
    elif type(bbox) == list:
        [xmin, ymin, xmax, ymax] = bbox
    else:
        raise TypeError
    if show_bbox:
        cv2.rectangle(img=result, pt1=(xmin, ymin), pt2=(xmax, ymax), color=color, thickness=thickness)
    if text is not None and show_label:
        text_thickness = label_thickness if label_thickness is not None else thickness
        text_color = label_color if label_color is not None else color
        result = draw_bbox_text(img=result, bbox=bbox, text=text, color=text_color, thickness=text_thickness,
                                orientation=label_orientation)
    return result


def draw_bbox_text(img: np.ndarray, bbox: BBox, text: str, color=None,
                   font_face: int = cv2.FONT_HERSHEY_COMPLEX, thickness: int = 2,
                   orientation: str = 'top') -> np.ndarray:
    # check_value(orientation, valid_value_list=['top', 'bottom', 'left', 'right'])
    if color is None:
        color = [0, 255, 255]
    result = img.copy()
    bbox_h, bbox_w = bbox.shape()
    target_textbox_h, target_textbox_w = bbox_h, bbox_w
    font_scale = 1
    [textbox_w, textbox_h], _ = cv2.getTextSize(text=text, fontFace=font_face, fontScale=font_scale,
                                                thickness=thickness)
    orientation = orientation.lower()
    if orientation in ['top', 'bottom']:
        font_scale = font_scale * (target_textbox_w / textbox_w)
        [textbox_w, textbox_h], _ = cv2.getTextSize(text=text, fontFace=font_face, fontScale=font_scale,
                                                    thickness=thickness)
        textbox_org_x = int(0.5 * (target_textbox_w - textbox_w) + bbox.xmin)
        if orientation == 'top':
            textbox_org_y = int(bbox.ymin - 0.2 * textbox_h)
        elif orientation == 'bottom':
            textbox_org_y = int(bbox.ymax + 1.2 * textbox_h)
        else:
            raise Exception
    elif orientation in ['left', 'right']:
        font_scale = font_scale * (target_textbox_h / textbox_h)
        [textbox_w, textbox_h], _ = cv2.getTextSize(text=text, fontFace=font_face, fontScale=font_scale,
                                                    thickness=thickness)
        textbox_org_y = int(0.5 * (target_textbox_h + textbox_h) + bbox.ymin)
        if orientation == 'left':
            textbox_org_x = int(bbox.xmin - 1.2 * textbox_w)
        elif orientation == 'right':
            textbox_org_x = int(bbox.xmax + 0.2 * textbox_w)
        else:
            raise Exception
    else:
        raise Exception
    textbox_org = (textbox_org_x, textbox_org_y)
    cv2.putText(img=result, text=text, org=textbox_org, fontFace=font_face, fontScale=font_scale, color=color,
                thickness=thickness, bottomLeftOrigin=False)
    return result


def draw_mask_image(img: np.ndarray, mask_image: np.ndarray, color=None, scale: int = 255,
                    interpolation: str = 'area', alpha: float = 0.3, beta: float = 1, gamma: float = 0) -> np.ndarray:
    if color is None:
        color = [255, 255, 0]
    result = img.copy()
    _mask_image = mask_image.copy()
    if img.shape[:2] != _mask_image.shape[:2]:
        _mask_image = resize_img(
            src=_mask_image, size=Size.from_cv2_shape(img.shape), interpolation_method=interpolation
        )
    colored_mask = ((_mask_image.reshape(-1).reshape(1, -1).T * color)
                    .reshape(_mask_image.shape[0], _mask_image.shape[1], 3)) / scale
    colored_mask = colored_mask.astype('uint8')
    cv2.addWeighted(src1=colored_mask, alpha=alpha, src2=result, beta=beta, gamma=gamma, dst=result)
    return result


def draw_mask_bool(
        img: np.ndarray, mask_bool: np.ndarray, color=None,
        transparent: bool = False, alpha: float = 0.3, beta: float = 1, gamma: float = 0) -> np.ndarray:
    """

    Returns
    -------
    np.ndarray
    """
    if color is None:
        color = [255, 255, 0]
    result = img.copy()
    if not transparent:
        result[mask_bool] = color
    else:
        mask_image = np.zeros(shape=result.shape[:2], dtype=np.uint8)
        mask_image[mask_bool] = 255
        result = draw_mask_image(img=result, mask_image=mask_image, color=color, scale=255,
                                 alpha=alpha, beta=beta, gamma=gamma)
    return result


def draw_keypoints_labels(
        img: np.ndarray, keypoints: list, keypoint_labels: list, color=None,
        font_face: int = cv2.FONT_HERSHEY_COMPLEX, thickness: int = 1,
        ignore_kpt_idx=None
):
    if ignore_kpt_idx is None:
        ignore_kpt_idx = []
    if color is None:
        color = [0, 0, 255]
    result = img.copy()

    # Define BBox enclosing keypoints
    keypoints_np = np.array(keypoints)
    if len(keypoints_np) > 0:
        kpts_xmin, kpts_ymin = np.min(keypoints_np, axis=0)
        kpts_xmax, kpts_ymax = np.max(keypoints_np, axis=0)
        kpts_bbox = BBox(xmin=kpts_xmin, ymin=kpts_ymin, xmax=kpts_xmax, ymax=kpts_ymax)
        bbox_h, bbox_w = kpts_bbox.shape()

        # Define target_textbox_w and initial font_scale guess.
        target_textbox_w = 0.1 * bbox_w  # Needs adjustment
        font_scale = 1 * (target_textbox_w / 93)

        # Find max_size_label_idx
        textbox_w, textbox_h = None, None
        max_size_label_idx = None
        for i, keypoint_label in enumerate(keypoint_labels):
            [label_w, label_h], _ = cv2.getTextSize(text=keypoint_label, fontFace=font_face, fontScale=font_scale,
                                                    thickness=thickness)
            if textbox_w is None or label_w > textbox_w:
                textbox_w, textbox_h = label_w, label_h
                max_size_label_idx = i

        # Prevent Divide By Zero Errors
        target_textbox_w = max(target_textbox_w, 1)
        textbox_w = max(textbox_w, 1)

        # Adjust to target_textbox_w
        retry_count = 0
        while abs(textbox_w - target_textbox_w) / target_textbox_w > 0.1 and retry_count < 3:
            retry_count += 1
            font_scale = font_scale * (target_textbox_w / textbox_w)
            [textbox_w, textbox_h], _ = cv2.getTextSize(text=keypoint_labels[max_size_label_idx], fontFace=font_face,
                                                        fontScale=font_scale, thickness=thickness)
            textbox_w = max(textbox_w, 1)
            textbox_h = max(textbox_h, 1)

        # Draw Label
        for i, [[x, y], keypoint_label] in enumerate(zip(keypoints, keypoint_labels)):
            if i not in ignore_kpt_idx:
                textbox_org_x = int(x - 0.5 * textbox_w)
                textbox_org_y = int(y - 0.5 * textbox_h)
                textbox_org = (textbox_org_x, textbox_org_y)
                cv2.putText(
                    img=result, text=keypoint_label, org=textbox_org, fontFace=font_face, fontScale=font_scale,
                    color=color,
                    thickness=thickness, bottomLeftOrigin=False
                )
    return result


def draw_keypoints(
        img: np.ndarray, keypoints: list, point_info_length: int = 2, show_keypoints: bool = True,
        radius: int = 4, color=None,
        keypoint_labels: list = None, show_keypoints_labels: bool = False, label_thickness: int = 1,
        label_color: list = None,
        ignore_kpt_idx=None
) -> np.ndarray:
    if ignore_kpt_idx is None:
        ignore_kpt_idx = []
    if color is None:
        color = [0, 0, 255]
    result = img.copy()
    _keypoints = []
    if point_info_length > 2:
        for e_list in keypoints:
            _keypoints.append(e_list[:2])
    elif point_info_length == 2:
        _keypoints = keypoints
    else:
        error(f'"point_info_length" can not be 1')
    if show_keypoints:
        for index, [x, y] in enumerate(_keypoints):
            if index not in ignore_kpt_idx:
                cv2.circle(
                    result,
                    (int(x), int(y)),
                    radius,
                    color,
                    -1,)

    if show_keypoints_labels:
        if keypoint_labels is not None:
            text_color = label_color if label_color is not None else color
            result = draw_keypoints_labels(
                img=result, keypoints=_keypoints, keypoint_labels=keypoint_labels, color=text_color,
                thickness=label_thickness,
                ignore_kpt_idx=ignore_kpt_idx
            )
        else:
            error(f"Need to provide keypoint_labels in order to show labels.")
            raise Exception
    return result


if __name__ == "__main__":
    height, width = 500, 500
    blank_image = np.zeros((height, width, 3), np.uint8)
    blank_image1 = blank_image
    blank_image = draw_bbox(
        blank_image, BBox(10, 200, 100, 400),
        color=[0, 255, 255], thickness=2, text='hi', label_thickness=2,
        label_color=[0, 100, 255],  # label_orientation='top'
        label_orientation='right'
    )
    # im = cv.imread('test.jpg')
    im = blank_image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(blank_image.shape, np.uint8)
    cv2.drawContours(mask, contours, -1, 255, 1)
    print(contours)
    blank_image1[mask] = (255, 255, 255)
    cv2.imshow('i', thresh)
    cv2.waitKey(10000)
    cv2.imshow('i', blank_image1)
    cv2.waitKey(10000)
