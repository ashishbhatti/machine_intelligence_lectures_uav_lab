'''
How to crop and resize images?
'''


import cv2
import numpy as np

img = cv2.imread("../Resources/test_image.png")

# to know shape of image, to know how much to crop
print(img.shape)                                          # (512, 512, 3)

# resizing the image
imgResize1 = cv2.resize(img, (640, 480))                  # change by exact pixel resolution
imgResize2 = cv2.resize(img, (0,0), None, 0.5, 0.5)       # change by scale percentage, better, preserves aspect ratio of image
print(imgResize2.shape)


# cropping the image
# image is an image, where to begin the matrix and where to end
imgCrop = img[50:400, 100:400]


cv2.imshow("Image", img)
cv2.imshow("Image Resize 1",imgResize1)
cv2.imshow("Image Resize 2",imgResize2)
cv2.imshow("Image Crop",imgCrop)
cv2.waitKey(0)