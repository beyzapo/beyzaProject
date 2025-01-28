# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

cam=cv2.VideoCapture(0)

if not cam.isOpened():
    print("kamera tanımlanmadı")
    exit()
    

while True:
    ret, frame=cam.read()
    
    if not ret:
        print("kamera görüntü okuyamıyor")
        break
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1)==ord("q"):
        
       print("görüntü sonlandırıldı")
       break
 
cam.release()
cv2.destroyAllWindows()
     