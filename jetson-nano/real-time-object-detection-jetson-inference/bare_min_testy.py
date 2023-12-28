import jetson.inference
import jetson.utils
import cv2

''' # opencv is not needed,
You can run the complete detection part using jetson inference and utils.
But to use the opencv functions, we import cv2, and convert image to a format,
opencv understands.
'''

# create a network
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold = 0.5)

# webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
