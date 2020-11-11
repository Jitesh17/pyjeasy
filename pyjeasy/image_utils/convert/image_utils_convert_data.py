# import os
# # from sys import exit as x
# from datetime import datetime

# import cv2
# import numpy as np

def id_to_color(RGBint):
    pixel_b = RGBint & 255
    pixel_g = (RGBint >> 8) & 255
    pixel_r = (RGBint >> 16) & 255
    
    return [pixel_b, pixel_g, pixel_r]
