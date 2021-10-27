import numpy as np
import cv2

# VideoCapture can also load video files using the filename
cap = cv2.VideoCapture(0)

print(cap)

while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()