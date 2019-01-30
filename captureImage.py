#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:27:06 2019

@author: sunil
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame = cap.read()
        //print(ret)
        //print(frame)
    else:
        ret = False
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.title("Display RGB color")
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap='gray')
    plt.show()
    cap.release()
if __name__=="__main__":
   main()    