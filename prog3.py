#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:29:40 2019

@author: sunil
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath = "/home/sunil/opencv/imgdataset/lena_color_256.tif"
    imgoutput = "/home/sunil/opencv/out.jpg"
    img = cv2.imread(imgpath,1)
    print(img)
    print(type(img))
    print(img.shape)
    print(img.size)
    cv2.imwrite(imgoutput,img)
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()    