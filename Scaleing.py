#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:26:06 2019

@author: sunil
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
   
        imgpath = "/home/sunil/opencv/imgdataset/"
        img1 = imgpath+"4.1.01.tiff"
        #read Image
        img1 = cv2.imread(img1,1)

        #Change color BGR to RGB
        img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        
        #Resize
        outimg = cv2.resize(img1,None,fx=0.7,fy=0.5,interpolation=cv2.INTER_LINEAR)
       
        #Show Original Pictures
        plt.title("Scaled Image")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(outimg)
        
        plt.show()
    
if __name__=="__main__":
   main()    