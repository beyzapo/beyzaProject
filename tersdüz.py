# -*- coding: utf-8 -*-
import cv2


cam=cv2.VideoCapture(0)
while True:
  ret,frame=cam.read()
  if not ret:
     break
  frame2=cv2.flip(frame,1)
  cv2.imshow("resim1",frame)
  cv2.imshow("resim2",frame2)
  cv2.waitKey(1) & 0xFF == ord("q")

cam.release()
cv2.destroyAllWindows()
