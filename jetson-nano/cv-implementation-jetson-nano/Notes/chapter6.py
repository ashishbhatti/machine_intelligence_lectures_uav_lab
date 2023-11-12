'''
GPIO basics of Jetson Nano

How to use GPIO pins of Jetson Nano?
Very similar to RaspberryPi GPIO pins in terms of the numbers and layout, 
but when it comes to functionality they are quite different.
Especially when you are trying to use it with different components like an LED, Servo Motors, DC motors. 
So, things get a little bit different.


Differences from RaspberryPi.
1. Jetson Nano pins do not provide enough current, 
        so have to use a transistor as an amplifier, to get max current
        if you want to use servos, you have to use external servo driver.
2. when you have to use pwm pins, you will face difficulty as you have to configure them.

Its not as straightforward as RPi.
Idea is to use RPi.GPIO which is already installed on Jetson Nano.
'''

'''
RGB LED 140C05 is used in this chapter. It is RBG not RGB, so connect accordingly.

Pin connections written in order: Pin on Board = BCM = Color
11 = 17 = R
13 = 27 = B
15 = 22 = G

We will be using internal pin number (BCM) of the board.

If you put it as LOW it will turn ON
If you put it as HIGH it will turn OFF.
'''

import RPi.GPIO as GPIO
from time import sleep

#        R   B   G
pins = [17, 27, 22]

# set the mode to internal pin mode, not the layout pin configuration 
GPIO.setmode(GPIO.BCM)

# set pins to output
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)


# # Implemention blinking LED example for arduino
# while True:

#         # white light
#         GPIO.ouput(pins[0], GPIO.LOW)
#         GPIO.ouput(pins[1], GPIO.LOW)
#         GPIO.ouput(pins[2], GPIO.LOW)

#         sleep(1)

#         # All OFF
#         GPIO.ouput(pins[0], GPIO.HIGH)
#         GPIO.ouput(pins[1], GPIO.HIGH)
#         GPIO.ouput(pins[2], GPIO.HIGH)
        
#         sleep(1)


# changing the colors
while True:

        # Red Color
        GPIO.ouput(pins[0], GPIO.LOW)
        GPIO.ouput(pins[1], GPIO.HIGH)
        GPIO.ouput(pins[2], GPIO.HIGH)

        sleep(1)

        # Blue Color
        GPIO.ouput(pins[0], GPIO.HIGH)
        GPIO.ouput(pins[1], GPIO.LOW)
        GPIO.ouput(pins[2], GPIO.HIGH)
        
        sleep(1)

        # Green Color
        GPIO.ouput(pins[0], GPIO.HIGH)
        GPIO.ouput(pins[1], GPIO.HIGH)
        GPIO.ouput(pins[2], GPIO.LOW)

        sleep(1)


# set up LED Module so don't have to repeat the code. Check in Modules directory.