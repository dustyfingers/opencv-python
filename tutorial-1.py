import cv2

# load image, pick mode to load image in
img = cv2.imread('./assets/headshot.jpg', cv2.IMREAD_UNCHANGED)
# prints a matrix representing the image. neat!
# print(img)

# first arg is label for window, second is image to display
cv2.imshow('My Face', img)

# 0 waits an infinite amount of time until you press a key on the kb
cv2.waitKey(0)
cv2.destroyAllWindows()
