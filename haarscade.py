# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:26:28 2025

@author: HP
"""

import cv2


eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
   
    ret, frame = cam.read()
    if not ret:
        print("Kare okunamadı, çıkılıyor...")
        break

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

   
    cv2.imshow('Göz Tespiti', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()