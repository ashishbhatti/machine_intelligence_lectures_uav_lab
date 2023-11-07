'''
Author: Ashish Kumar
Date: November 18, 2023
Place: UAV Lab, IIT Kanpur

Topic: 
How to do the following?
1. Import an image in OpenCV and display it
2. Import frames of video and display them
3. Read video frames from a usb webcam
4. Read video frames from a csi webcam
'''

# ---------- importing an image --------------------------
# import cv2
# # print(cv2.__version__)                                  # version of opencv
# img = cv2.imread("../Resources/test_image.png")         # importing theimage
# cv2.imshow("Output", img)                               # showing the image
# cv2.waitKey(0)                                          # Delay of 0, i.e., infinite, so that Output window does not close right away

# ---------- importing a video ----------------------------
# import cv2
# frameWidth = 640                                        # framewidth is needed for resizing
# frameHeight = 480                                       # same as above
# cap = cv2.VideoCapture("../Resources/test_video1.mp4")  # create a videocapture object

# # infinite loop to read all the frames
# while True:
#     success, img = cap.read()                           # read one frame 
#     img = cv2.resize(img, (frameWidth, frameHeight))    # resize 
#     cv2.imshow("Results", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# ---------- run a usb webcam ---------------------------
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Results", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# ---------- run a csi webcam ---------------------------
# Refer to: https://youtu.be/dHvb225Pw1s
'''
NVIDIA Argus is a set of APIs for camera applications on NVIDIA 
Tegra platforms. It provies a way to interface with camera hardware, 
control camera settings, and capture processes or images or video streams.
'''

import cv2

# parameters for camera
frameWidth = 640
frameHeight = 480

# For CSI camera
flip = 0
camset = "nvarguscamerasrc sensor_id=0 ! \
   video/x-raw(memory:NVMM), width=1920, height=1080, framerate=30/1 ! \
   nvvidconv flip-method={} ! \
   video/x-raw, width=960, height=540, format=(string)BGRx ! \
   videoconvert ! \
   video/x-raw, format=(string)BGR ! appsink".format(flip)

cap = cv2.VideoCapture(camset, cv2.CAP_GSTREAMER)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Results", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break