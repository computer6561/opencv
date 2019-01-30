#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:41:46 2019

@author: sunil
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "/home/sunil/opencv/imgdataset/";
    img1 = path+'4.2.01.tiff'
    
    img1 = cv2.imread(img1,1)
    
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    r,g,b = cv2.split(img1)
    
    titles=['OG img','Red','Green','Blue']
    images = [cv2.merge((r,g,b)),r,g,b]
    cmaps = ['gray','Reds','Greens','Blues']
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(images[i],cmap=cmaps[i])
    plt.show()     
        
if __name__=="__main__":
    main()        