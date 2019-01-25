# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath = "/home/sunil/opencv/imgdataset/lena_color_256.tif"
    img1 = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    plt.title("Display BGR color")
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img1, cmap='gray')
    plt.show()
    plt.title("Display RGB color")
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()    