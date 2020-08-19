# -*- coding: utf-8 -*-
"""
Author: Jitesh Gosar
"""
import glob
import numpy as np
import cv2


class Image2Video:
    def __init__(self, input_path: str, output_path: str, fps: int):
        self.input_path = input_path
        self.output_path = output_path
        self.fps = fps
        self.size = size
    
    def run(self):
        txtfiles = []
        img_array = []
        for filename in glob.glob(self.input_path+'/*.png'):
            txtfiles.append(filename)
        txtfiles.sort()
        print(txtfiles)
        for filename in txtfiles:
            print(filename)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)


        out = cv2.VideoWriter(self.output_path+'.mp4',
                            cv2.VideoWriter_fourcc(*'DIVX'), self.fps, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
    
    @staticmethod
    def fast(path: str, fps: int=24):
        # path = "/home/jitesh/3d/blender/hospital_3d/animation/cam2"
        txtfiles = []
        img_array = []
        for filename in glob.glob(path+'/*.png'):
            txtfiles.append(filename)
        txtfiles.sort()
        print(txtfiles)
        for filename in txtfiles:
            print(filename)
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)


        out = cv2.VideoWriter(path+'.mp4',
                            cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
