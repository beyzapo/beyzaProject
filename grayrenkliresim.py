# -*- coding: utf-8 -*-

import cv2

resim=cv2.imread("IMG_5495.JPG")
cv2.imshow("IMG_5495.JPG",resim)

grayresim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("beyza",grayresim)

if cv2.waitKey(0)== ord("s"):
   cv2.imwrite("beyza.jpg",resim)
if cv2.waitKey(0)== ord("q"):
   cv2.destroyWindow("IMG_5495.JPG")
if cv2.waitKey(0)== ord("w"):
  cv2.destroyWindow("beyza")






