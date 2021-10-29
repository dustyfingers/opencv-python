import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
# converts image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# run corner detection
# args: src image, # of corners to return, 'quality' of corners, min distance between corners
corners = cv2.goodFeaturesToTrack(gray, 100,  0.01, 5)

# display corners on screen by drawing circles
# change floats to ints
corners = np.int0(corners)
for corner in corners:
    # ravel() flattens the array [[2, 1]] ==> [2, 1]
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

# draw lines between corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)




cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()