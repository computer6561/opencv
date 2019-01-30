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
    windowName = "Preview"
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame = cap.read()
        
        #Change color BGR to RGB
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        colorpic = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        #Blue Color
        low = np.array([100,50,50])
        high = np.array([140,255,255])
        
        #image mask
        img_mask = cv2.inRange(hsv,low,high)
        
        #filter specified color object
        filteredPic = cv2.bitwise_and(colorpic,colorpic,mask=img_mask)
        
        #Show Original Pictures
        plt.subplot(1,3,1)
        plt.title("Original Pic")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(colorpic)
        
        #Masked Pictures
        plt.subplot(1,3,2) 
        plt.title("Masked Pic")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_mask)
        
        #Filtered Pictures
        plt.subplot(1,3,3) 
        plt.title("Filtered Pic")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(filteredPic)
        
        
        plt.show()
    cap.release()
    
if __name__=="__main__":
   main()    