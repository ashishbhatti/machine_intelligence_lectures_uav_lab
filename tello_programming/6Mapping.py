'''
Odometry Problem: How to localize the drone in the surroundings?

We will take the velocity information, to find the distance.
We will also use angular speed, to find the angle of drone,
or where it is headed. Based on this we will find the x,y coordinates
of the drone.

So, we will take the distance and angle and we will convert it into
cartesian coordinates, and plot it into a graph.

# Translation
Distance = Speed x Time

# Rotation
Angle (Heading) = AngularSpeed x Time

# How to calculate when both are pressed? forward and rotation
We will find coordinates after every unit of time, so we will
have intermediate positions.

'''

from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import numpy as np
import cv2

# --------- Initialization --------
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

# ------- Parameters --------------
fSpeed = 117/10              # Forward Speed in cm/sec (actual speed was 15 cm/s)
aSpeed = 360/10              # Angular Speed Degrees/s
interval = 0.25              # time interval to calculate

dInterval = fSpeed * interval           # distance in one time unit (interval above)
aInterval = aSpeed * interval           # angle in one time unit



def getKeyboardInput():
    # defining params left-right, forward-backward, up-down, yaw-velocity
    lr, fb, ud, yv  = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed
    
    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()
    
    return [lr, fb, ud, yv]

def drawPoints():
    cv2.circle(img, (300,500), 5, (0,0,255), cv2.FILLED)

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000,1000,3), np.uint8)
    drawPoints()
    cv2.imshow("Output", img)
    cv2.waitKey(1)