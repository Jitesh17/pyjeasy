# import os, sys
import numpy as np


# import pandas as pd
# import printj

def dist(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))
