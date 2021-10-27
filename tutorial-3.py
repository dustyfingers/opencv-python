import numpy as np
import cv2

# VideoCapture can also load video files using the filename
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # empty image that is the same size as frame 
    image = np.zeros(frame.shape, np.uint8)

    # how to draw
    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    image = cv2.line(image, (0, height), (width, 0), (255, 0, 0), 10)
    # -1 as the last argument (thickness) fills the shape
    image = cv2.rectangle(image, (100, 100), (250, 250), (0, 255, 0), 10)
    image = cv2.circle(image, (300, 300), 60, (0, 0, 255), -1)

    # how to display text
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Lou is awesome!', (20, height-10), font, 1, (0, 0, 0), 3, cv2.LINE_AA)

    # smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, width//2:] = smaller_frame

    cv2.imshow('Webcam Video', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()