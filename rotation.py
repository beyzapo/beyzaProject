# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:31:18 2025

@author: HP
"""

# -- coding: utf-8 --

import cv2
import numpy as np

img = cv2.imread("talisca.jpg")


print(img.shape)


rows,cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
img_rotation = cv2.warpAffine(img,rotation_matrix,(int (cols*1.2) ,int (rows*1.2)))


cv2.imshow("fb",img)
cv2.imshow("rotated image",img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()