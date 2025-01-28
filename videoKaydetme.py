import cv2

def nothing(x):
    pass

# Kamera açma
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Kamera açılamadı")
    exit()

# Video kaydetmek için codec ve dosya adı
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("kaydedilen0.avi", fourcc, 30.0, (640, 480))  # Çözünürlüğü kameraya göre ayarlayın


while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Kameradan görüntü alınamadı")
        break

    

    
    cv2.imshow("video", frame)

    # Video kaydetme
    out.write(frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) == ord("q"):
        print("Video bitti")
        break

# Kaynakları serbest bırakma
cam.release()
out.release()
