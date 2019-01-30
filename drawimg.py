#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:16:30 2019

@author: sunil
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:29:40 2019

@author: sunil
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img1 = np.zeros((256,256,3),np.uint8)
    cv2.line(img1,(0,99),(99,0),(255,0,0),1)
    cv2.rectangle(img1,(55,55),(140,140),(0,255,0),1)
    cv2.circle(img1,(180,180),40,(0,0,255),-1)
    cv2.ellipse(img1,(60,185),(55,35),0,0,270,(120,120,120),-1)
    points = np.array([[80,5],[125,5],[179,19],[230,30],[30,50]],np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(img1,[points],True,(0,255,134))
    
    #text-------------------------
    text1 = "Vehicle"
    cv2.putText(img1,text1,(60,160),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,234,123))
    
    plt.imshow(img1)
if __name__ == "__main__":
    main()    