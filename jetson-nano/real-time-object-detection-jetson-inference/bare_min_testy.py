import jetson.inference
import jetson.utils
import cv2

''' # opencv is not needed,
You can run the complete detection part using jetson inference and utils.
But to use the opencv functions, we import cv2, and convert image to a format,
opencv understands.
'''

# create a network
net = jetson.inference.detectNet
