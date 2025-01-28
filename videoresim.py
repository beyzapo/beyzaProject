# -*- coding: utf-8 -*-

import cv2

cam=cv2.VideoCapture(0)

while True:
  ret, frame=cam.read() 
  cv2.line(frame,(254,100),(70,100),(255,0,0),5)
  cv2.rectangle(frame,(100,100),(80,50),(0,0,255),2)
  cv2.circle(frame,(150,180),60,(120,120,120),2)
  cv2.putText(frame,"Mehmet Oguz",(100,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,100,0),3)
  cv2.imshow("kamera",frame)  
  if cv2.waitKey(1)==ord("q"):
      break
      
cam.release()
cv2.destroyAllWindows()
