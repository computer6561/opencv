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
     filename = "/home/sunil/opencv/video/out.avi"
     cap = cv2.VideoCapture(0)
     i=0
     codec = cv2.VideoWriter_fourcc("W","M","V","2")
     framerate = 14
     resolution = (640,480)
     videofile = cv2.VideoWriter(filename,codec,framerate,resolution)
     if cap.isOpened():
         ret,frame = cap.read()
     else:
         ret = False
     while ret:
         ret,frame = cap.read()
         videofile.write(frame)
         i=i+1
         if((i<500)==False):
             print("Video Saved!!")
             break
     videofile.release()    
     cap.release()
if __name__=="__main__":
   main()    