'''
We will use our keyboard to fly our drone.
To do this, we need to:
    1. Get the keyboard command first
    2. Implement using basic movements learnt in chapter 2.

We will create a new module called KeyPressModule.    
A module is a piece of code which can run individually and 
from other scripts as well, if other script wants to use its
functions.

Check: KeyPressModule.py

We will use pygame to get the commands from keyboard.
The idea of this library is to create games. So, whenever you are
trying to detect keypress, it has to be from within a game window.
So, we need to create that window.
'''


from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

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



while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    print(kp.getKey("s"))