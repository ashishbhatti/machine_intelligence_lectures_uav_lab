'''
Draw shapes and text
1. Circle
2. Rectangle
3. Line
4. Text
'''

import cv2
import numpy as np


img = np.zeros((512,512,3), np.uint8)    # black image, creating own image
# img[:] = 255, 0, 0                       # Makes img a blue image
img[:] = 255, 255, 255                   # white image


# whatever shape you want to draw, basically uses its name
cv2.circle(img, (256,256), 150, (0,69,255), cv2.FILLED)                   # center coordinates, radius, (0, 69, 255) orange color, 5 is thickness (cv2.FILLED if filling)
cv2.rectangle(img, (130,226), (382,285), (255, 255, 255), cv2.FILLED)     # upper left vertex coordinates, lower right vertex coordinates, white color, thickness or cv2.FILLED
cv2.line(img, (130, 296), (382, 296), (255, 255, 255), 2)                 # first end point coordinates, second end point coordinates, white line
cv2.putText(img, "Murtaza's workshop", (137, 265), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 69, 255), 2)      # Text, starting coordinates, font, scale (font size sort of), orange color, thickness


cv2.imshow("Image",img)
cv2.waitKey(0)
