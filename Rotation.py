#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:58:25 2019

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
        
        #Translate
        rows,columns,channels = img1.shape
        R= cv2.getRotationMatrix2D((columns/2,rows/2),-23,0.8)
      #  R=np.array([[  0.92050485,   0.39073113, -39.83820569],[ -0.39073113,   0.92050485,  60.1889632 ]])
        print(R)
        outimg = cv2.warpAffine(img1,R,(columns,rows))
        #Show Original Pictures
        plt.title("Rotated Image")
        plt.xticks([])
        plt.yticks([])
        plt.imshow(outimg)
        
        plt.show()
    
if __name__=="__main__":
   main()    