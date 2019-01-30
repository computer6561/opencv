#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:08:46 2019

@author: sunil
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "/home/sunil/opencv/imgdataset/";
    img1 = path+"4.1.01.tiff"
    img2 = path+"lena_color_256.tif"
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img3 = cv2.bitwise_and(img1,img2)
    img4 = cv2.bitwise_or(img1,img2)
    img5 = cv2.bitwise_not(img1)
    img6 = cv2.bitwise_xor(img1,img2)
    
    titles=['Original 1','Original 1','AND','OR','NOT','X-OR']
    images = [img1,img2,img3,img4,img5,img6]
    

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(images[i])
    plt.show()     
        
if __name__=="__main__":
    main()        