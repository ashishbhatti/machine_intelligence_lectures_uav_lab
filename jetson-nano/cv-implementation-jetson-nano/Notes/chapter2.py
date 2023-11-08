'''
Fundamentals of image processing.
5 main functions which are very important while implementing different kinds of image processing techniques.
1. Grayscale conversion
2. Blurring 
3. Canny Edge Detector
4. Dilation
5. Erosion
'''

import cv2
import numpy as np

# for resizing images so they don't fillup the whole screen
resolution = 640, 480

# reading the image
# img = cv2.imread("../Resources/test_image.png")                                          # lenna image
img = cv2.imread("../Resources/test_image1.jpg")                                         # daddario image
img = cv2.resize(img, resolution)

# grayscale conversion
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blurring the image
# many methods of blurring, here using Gaussian Blur
imgBlur = cv2.GaussianBlur(imgGray, (3,3), 0)


# finding edges
# canny edge detector
imgCanny = cv2.Canny(imgBlur, 100, 150)

# dilation = increase thickness of edges, erosion = decreasing thickness of edges
kernel = np.ones((5,5), np.uint8)
imgDia = cv2.dilate(imgCanny, kernel, iterations=3)
imgErode = cv2.erode(imgDia, kernel, iterations=1)



# displying the image
cv2.imshow("Image", img)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilate", imgDia)
cv2.imshow("Image Erode", imgErode)

# wait for infinite time
cv2.waitKey(0)