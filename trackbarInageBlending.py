#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:34:34 2019

@author: sunil
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:27:06 2019

@author: sunil
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
def emptyFunction():
    pass

def main():
   
        imgpath = "/home/sunil/opencv/imgdataset/"
        img1 = imgpath+"4.1.03.tiff"
        img2 = imgpath+"4.1.08.tiff"
        #read Image
        img1 = cv2.imread(img1,1)
        img2 = cv2.imread(img2,1) 
        #Change color BGR to RGB
        img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        alpha = 0.8
        beta=0.2
        gamma = 0
        wt1 = cv2.addWeighted(img1,alpha,img2,beta,gamma)
        
        cv2.createTrackbar('Alpha',"rack",0,100,emptyFunction)
        
        #Transitions
        while(True):
            wt1 = cv2.addWeighted(img1,alpha,img2,beta,gamma)
            cv2.imshow('Transition',wt1)
            
            if(cv2.waitKey(1)==27):
                break
            
            alpha = cv2.getTrackbarPos('Alpha','Transition')/100
            beta=1-alpha
            
        cv2.destroyAllWindows()
    
if __name__=="__main__":
   main()    
   
   
   
   