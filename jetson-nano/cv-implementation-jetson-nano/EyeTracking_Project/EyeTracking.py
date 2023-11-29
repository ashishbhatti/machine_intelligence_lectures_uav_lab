import cv2
import ObjectDetectionModule as odm
import SerialModule as sm
import numpy as np
import time

# parameters for camera
frameWidth = 640
frameHeight = 480

# For CSI camera
# flip = 0
# camset = "nvarguscamerasrc sensor_id=0 ! \
#    video/x-raw(memory:NVMM), width=1920, height=1080, framerate=30/1 ! \
#    nvvidconv flip-method={} ! \
#    video/x-raw, width=960, height=540, format=(string)BGRx ! \
#    videoconvert ! \
#    video/x-raw, format=(string)BGR ! appsink".format(flip)
# cap = cv2.VideoCapture(camset, cv2.CAP_GSTREAMER)

cap = cv2.VideoCapture(0)                                           # change to camset for CSI
ser = sm.initConnection('/dev/ttyACM0', 9600)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# previous pid errors initially
perrorLR, perrorUD = 0, 0


def findCenter(imgObject, objects):
    cx, cy = -1, -1
    if len(objects) != 0:
        x,y,w,h = objects[0][0]
        cx = x + w // 2
        cy = y + h // 2
        cv2.circle(imgObject, (cx,cy), 2, (0,255,0), cv2.FILLED)    # dot in center

        # visually show how far from center
        ih, iw, ic = imgObject.shape
        cv2.line(imgObject, (iw//2, cy), (cx, cy), (0,255,0), 1)    # horizontal line
        cv2.line(imgObject, (cx, ih//2), (cx, cy), (0,255,0), 1)    # vertical line

    return cx, cy, imgObject



def trackObject(cx, cy, w, h):

    global perrorLR, perrorUD

    # pid paramaters, only p and d
    kLR = [0.6, 0.1]
    kUD = [0.6, 0.1]

    if cx != -1:

        # left and right
        errorLR = w//2 - cx
        posX = kLR[0]*errorLR + kLR[1]*(errorLR - perrorLR)         # pd controller
        posX = int(np.interp(posX, [-w//2, w//2], [20, 160]))       # mapping pid answer to servo acceptable answer
        perrorLR = errorLR                                          # update error

        # up and down
        errorUD = h//2 - cy
        posY = kUD[0]*errorUD + kUD[1]*(errorUD - perrorUD)
        posY = int(np.interp(posY, [-h//2, h//2], [20, 160]))       # mapping pid answer to servo acceptable answer
        perrorUD = errorUD                                          # update error

        sm.sendData(ser, [posX, posY], 3)                           # note this is only being send if object detected



while True:
    success, img = cap.read()
    img = cv2.resize(img, (0,0), None, 0.3,0.3)

    # find the objects in image
    imgObject, objects = odm.findObjects(img, faceCascade, 1.08, 10)
    cx, cy, imgObject = findCenter(imgObject, objects)
    
    h,w,c = imgObject.shape
    cv2.line(imgObject, (w//2,0), (w//2,h), (255,0,255),1)
    cv2.line(imgObject, (0, h//2), (w,h//2), (255,0,255),1)
    
    trackObject(cx, cy, w, h)
    # time.sleep(1)

    # imgObject = cv2.resize(imgObject, (0,0), None, 3, 3)
    cv2.imshow("Image", imgObject)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sm.sendData(ser, [90,90], 3)                         # middling the servos 
        break
