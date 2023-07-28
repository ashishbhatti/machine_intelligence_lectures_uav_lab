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
import math

# --------- Initialization --------
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
x,y = 500,500
a = 0          # angle
yaw = 0


# ------- Parameters --------------
fSpeed = 117/10              # Forward Speed in cm/sec (actual speed was 15 cm/s)
aSpeed = 360/10              # Angular Speed Degrees/s
interval = 0.25              # time interval to calculate

dInterval = fSpeed * interval           # distance in one time unit (interval above)
aInterval = aSpeed * interval           # angle in one time unit

points = []

def getKeyboardInput():
    # defining params left-right, forward-backward, up-down, yaw-velocity
    lr, fb, ud, yv  = 0, 0, 0, 0
    speed = 15
    d = 0
    global x,y,yaw, a

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"): 
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"): 
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"): 
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed
    
    if kp.getKey("a"): 
        yv = -speed
        yaw -= aInterval
    elif kp.getKey("d"): 
        yv = speed
        yaw += aInterval


    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    
    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0,0,255), cv2.FILLED)
    cv2.putText(img, f'({points[-1][0] - 500/100}, {points[-1][1] - 500/100})m',
        (points[-1][0]+10, points[-1][1] + 30))

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000,1000,3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)