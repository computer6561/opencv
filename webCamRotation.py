#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:08:25 2019

@author: sunil
"""



import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
   
        #imgpath = "/home/sunil/opencv/imgdataset/"
       # img1 = imgpath+"4.1.01.tiff"
        #read Image
        #img1 = cv2.imread(img1,1)
        cap = cv2.VideoCapture(0)
    
        if cap.isOpened():
            ret,frame = cap.read()
            #print(ret)
            #print(frame)
        else:
            ret = False
        img1 = frame
        #Change color BGR to RGB
        img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        cap.release()
        #Translate
        angle = 0
        scale  = 0.7
        rows,columns,channels = img1.shape
        while True:
            if angle==360:
                angle=0
            else:
                angle +=1
                
            R= cv2.getRotationMatrix2D((columns/2,rows/2),angle,scale)
            print(R)
            outimg = cv2.warpAffine(img1,R,(columns,rows))
            #Show Original Pictures
            plt.title("Rotated Image")
            plt.xticks([])
            plt.yticks([])
            plt.imshow(outimg) 
            plt.show()
            time.sleep(0)
            
if __name__=="__main__":
   main()     