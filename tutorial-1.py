import cv2

# load image, pick mode to load image in
img = cv2.imread('./assets/headshot.jpg', cv2.IMREAD_UNCHANGED)
# prints a matrix representing the image. neat!
# print(img)

# resize image to 400 x 400 explicitly
# img = cv2.resize(img, (400, 400))

# resize image to half its original size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate an image by 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# how to write an image -- you can convert images from one format to another!!
cv2.imwrite('./build/new_img.png', img)

# first arg is label for window, second is image to display
cv2.imshow('My Face', img)

# 0 waits an infinite amount of time until you press a key on the kb
cv2.waitKey(0)
cv2.destroyAllWindows()
