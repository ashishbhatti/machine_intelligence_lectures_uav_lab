'''
This project will try face tracking. We will try to figure 
out how to make the drone track a particualr object 
or full body. Firstly we will implement it using face, 
later on we can implement it on full body.

We will implement the following:

1. Forward-backward movement depending on the area of the 
bounding box. (check area range by testing)

2. We want the object to be in the center of image, 
yaw control.

How to solve the problem of overshooting in yaw control?
We will make the angular speed smaller as the object comes
closer to the center line.
Angular speed of zero, when the object is at the center.
This method is known as PID. It is a linear controller.
Using PID you can relate two different entities together 
which are not relatable by default.
'''

import cv2
import numpy as np

# detecting the face first
def findFace(img):
    """
    Finds faces in an image using the method proposed 
    by Viola-Jones. Famous method aka Haar-Cascades. It 
    uses a file which has all the parameters and information
    of the model, and helps us detect obejcts.
    """
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []                  # to store center points
    myFaceListArea = []              # to store area
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)


# running the webcam for now
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    findFace(img)
    cv2.imshow("Output", img)
    cv2.waitKey(1)