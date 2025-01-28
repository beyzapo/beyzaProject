# -*- coding: utf-8 -*-

import cv2

cam=cv2.VideoCapture(0)

if not cam.isOpened():
    print("kamera tanımlanmadı")
    exit()
while True:
    ret, frame=cam.read()
    framegray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
     break

    cv2.imshow("kamera", frame)
    cv2.imshow("kameragray",framegray)
    
    if (cv2.waitKey(1)==ord("q")):
     break
 

cam.release()
cv2.destroyAllWindows()


