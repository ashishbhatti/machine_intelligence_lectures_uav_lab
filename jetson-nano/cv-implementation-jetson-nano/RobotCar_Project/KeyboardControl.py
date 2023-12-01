'''
Grant permission to the port
sudo chmod 666 /dev/ttyACM0
'''

import cv2
import time
import SerialModule as sm

ser = sm.initConnection('/dev/ttyACM0', 9600)

### Run webcam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    key = cv2.waitKey(1)

    if key == ord('w'): sm.sendData(ser, [30,0], 4)
    elif key == ord('s'): sm.sendData(ser, [-30,0], 4)
    elif key == ord('a'): sm.sendData(ser, [40,10], 4)
    elif key == ord('d'): sm.sendData(ser, [40,-10], 4)
    elif key == ord('q'): break
    else: sm.sendData(ser, [0,0], 4)