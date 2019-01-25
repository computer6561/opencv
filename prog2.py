# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgpath = "/home/sunil/opencv/imgdataset/lena_color_256.tif"
    imgoutput = "/home/sunil/opencv/out.jpg"
    img = cv2.imread(imgpath,0)
    cv2.imwrite(imgoutput,img)
    cv2.imshow("Img",img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
   # plt.imshow(img, cmap='gray')
   # plt.show()

if __name__ == "__main__":
    main()    