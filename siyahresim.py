# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=np.zeros((255,255,3),dtype = np.uint8)




cv2.line(img,(254,100),(70,100),(255,0,0),5)
cv2.rectangle(img,(50,50),(110,100),(0,255,0),10)
cv2.circle(img,(150,180),60,(120,120,120),2)
cv2.putText(img,"Dzeko",(100,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,100,0),3)

cv2.imshow("resim",img)
cv2.waitKey(0)==ord("q")
cv2.destroyAllWindows()