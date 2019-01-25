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

def main():
   
        imgpath = "/home/sunil/opencv/imgdataset/"
        img1 = imgpath+"4.1.01.tiff"
        img2 = imgpath+"lena_color_256.tif"
        #read Image
        img1 = cv2.imread(img1,1)
        img2 = cv2.imread(img2,1) 
        #Change color BGR to RGB
        img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        add = img1 + img2
        sub1 = img1-img2
        sub2 = img2-img1
        mult = img1*img2
        div = img2/img1
        
        images = [img1,img2,add,sub1,sub2,mult,div]
        titles = ['pic1','pic2','add','sub1','sub2','mult','div']
        count = 7
        for i in range(count):
            #Show Original Pictures
            plt.subplot(1,count,i+1)
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
            plt.imshow(images[i])
        
        plt.show()
    
if __name__=="__main__":
   main()    