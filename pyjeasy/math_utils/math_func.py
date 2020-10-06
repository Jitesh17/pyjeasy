# import os, sys
import numpy as np


# import pandas as pd
# import printj

def dist(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = np.inf
    return result

def change_percent(a, b):
    try:
        result = 100*(a - b)/a
    except ZeroDivisionError:
        result = np.inf
    return result