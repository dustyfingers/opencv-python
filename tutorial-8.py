import numpy as np
import cv2

# VideoCapture can also load video files using the filename
cap = cv2.VideoCapture(0)

# classifiers are used to find features in an image, in this case faces and eyes 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # pass in grayscale image, scale factor minNeighbors
    # returns the matches for faces (given the arguments) in an image
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # region of interest not return on investment
        roi_gray = gray[x:x+w, y:y+w]
        roi_color = frame[x:x+w, y:y+w]

        eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 3)

    cv2.imshow('Webcam Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()