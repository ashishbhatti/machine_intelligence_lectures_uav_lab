"""
Author: Ashish Kumar
Place: UAV Lab, IIT Kanpur
Date: November 07, 2023
"""

"""
This code is to make you familiar with the Jetson Nano GPIO pins:
1. Be careful with circuit as you might end up damaging the Jetson Nano, if not careful.
2. Jetson Nano pins are different from Arduino Pins.
3. Jetson Nano GPIO is similar to RPi GPIO but not the same.

Refer the video: https://youtu.be/BBKpEgJKF0s
Refer the blog: https://jetsonhacks.com/2019/06/07/jetson-nano-gpio/

Pins: Pin 7 connected to the base of the transistor
"""

# import gpio libraries
import RPi.GPIO as GPIO

# Bring the already set pins to default mode, so you can set them up 
# GPIO.cleanup()  

# tell it, which numbering scheme you are using
# set the layout as the numbers given on board
GPIO.setmode(GPIO.BOARD)

# setup the pin to be output or input
GPIO.setup(7, GPIO.OUT)                   # arduino equivalent of pinmode, set pin 11 as ouput pin

# set GPIO to be True
GPIO.output(7, True)                      # instead of True, we can use 1

# set GPIO to be True
GPIO.output(7, False)                     # instead of False, we can use 1

GPIO.cleanup()  
