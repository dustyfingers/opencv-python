import cv2
import random
from datetime import datetime

# load image, pick mode to load image in
# opencv uses BGR, not RGB to define its colors
img = cv2.imread('./assets/headshot.jpg', -1)

# type is a 3d numpy array
# print(type(img))
# print(img)

# print first row of img
# print(img[0])

# print middle pixels of first row of img
# print(img[0][45:400])

# how to change pixels
# for i in range(100):
#   for j in range(img.shape[1]):
#     img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# # write image
# now = datetime.now()
# filename = 'new_img_' + now.strftime('%d_%m_%Y_%H_%M_%S') + '.png'
# cv2.imwrite(f'./build/{filename}', img)

# how to copy and paste parts of the image
tag = img[100:200, 400:500]

img[300:400, 600:700] = tag

# first arg is label for window, second is image to display
cv2.imshow('My Face Edited', img)

# 0 waits an infinite amount of time until you press a key on the kb
cv2.waitKey(0)
cv2.destroyAllWindows()