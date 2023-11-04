"""
Author: Ashish Kumar
Place: UAV Lab, IIT Kanpur
Date: November 04, 2023
"""

"""
Run this code to test the following:
1. The frame rates of face detection based on haar cascades.
2. If cvlib is working on jetson nano
"""

import cv2
import numpy as np
import time



# set the resolution to work with
w, h = 360, 240
fbRange = [6200, 6800]     # The desired area range of bounding box
pid = [0.4, 0.4, 0]
pError = 0


def findFace(img):
    '''
    Function takes a frame and performs face detection using Haar Cascade Classifier.
    Args:
        img: an image frame, there is no size constraints
    Returns:
        img: the image frame with bounding box and center drawn, for each detected face
        info: list of two items, center point coordinates and area of the biggest face detected
    '''

    # opencv has trouble finding haarcascade xml files, hence explicit path
    path2haarcascades = '/usr/share/opencv4/haarcascades/'

    faceCascade = cv2.CascadeClassifier(path2haarcascades + 'haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListCenter = []        # List of center point of all detected faces
    myFaceListArea = []          # List of area of bounding box of all the detected faces

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x + w//2
        cy = y + h//2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListCenter.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListCenter[i], myFaceListArea[i]]
    else:
        return img, [[0,0], 0]



def findFaceResnet(img):
    '''
    '''
    import cvlib

    # perform face detection using resnet
    faces, confidences = cvlib.detect_face(img)

    myFaceListCenter = []        # List of center point of all detected faces
    myFaceListArea = []          # List of area of bounding box of all the detected faces

    for (x1,y1,x2,y2) in faces:
        cv2.rectangle(img, (x1,y1), (x2, y2), (0,0,255), 2)
        cx = (x1 + x2)//2
        cy = (y1 + y2)//2
        area = (x2 - x1) * (y2 - y1)
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListCenter.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListCenter[i], myFaceListArea[i]]
    else:
        return img, [[0,0], 0]




def trackFace(info, w, pid, pError):
    '''
    Tracks the face about which info is provided
    Args:
        info : list of center point and area of face to be tracked
        w : width of the image
        pid : list of pid gains
        pError :  
    Returns:
        error: the error between center of frame and face x coordinate
        speed: the yaw angle or rotation speed
        fb: forward/backward movement
    '''

    area = info[1]
    x, y = info[0]

    # pid for the angle
    error = x - w//2                                 # w is width of the image, x is face center
    speed = pid[0]*error + pid[1]*(error - pError)
    speed = int(np.clip(speed, -100, 100))           # clip the speed between -100 and 100


    # forward / backward movement based on area of bounding box
    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20    # go back
    elif area < fbRange[0]:
        fb = 20     # go forward

    # if no faces
    if x == 0:
        speed = 0
        error = 0

    return error, speed, fb



if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    
    # variables for fps calculation
    fps_start_time = time.time()
    fps_frame_count = 0

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (w,h))

        # img, info = findFace(img)
        img, info = findFaceResnet(img)
        pError, speed, fb = trackFace(info, w, pid, pError)
        
        # Calculate FPS
        fps_frame_count += 1
        if fps_frame_count >= 1:
            fps_end_time = time.time()
            fps = fps_frame_count / (fps_end_time - fps_start_time)
            fps_frame_count = 0
            fps_start_time = fps_end_time
        

        cv2.putText(img, f'yaw: {speed}, movement: {fb}, FPS:{fps}', (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
        # display the frame in a window
        cv2.imshow('Output', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()