'''
We can use functional programming to do this, but because we will have multiple LEDs,
we will have classes. We are going to create a class for our LED light, 
and based on that we will create an LED Object, and we can change it's color.
'''

import RPi.GPIO as GPIO
from time import sleep

# set the mode to internal pin mode, not the layout pin configuration 
GPIO.setmode(GPIO.BCM)

class ledRBG():
    def __init__(self, R, B, G):
        
        # define the pin values
        self.R = R
        self.B = B
        self.G = G

        # set pins to output
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)

    # method for changing color
    def color(self, myColor):

        # Red Color
        if myColor == 'red':
            GPIO.ouput(self.R, GPIO.LOW)
            GPIO.ouput(self.B, GPIO.HIGH)
            GPIO.ouput(self.G, GPIO.HIGH)

        # Blue Color
        elif myColor == 'blue':
            GPIO.ouput(self.R, GPIO.HIGH)
            GPIO.ouput(self.B, GPIO.LOW)
            GPIO.ouput(self.G, GPIO.HIGH)

        # Green Color
        elif myColor == 'green':
            GPIO.ouput(self.R, GPIO.HIGH)
            GPIO.ouput(self.B, GPIO.HIGH)
            GPIO.ouput(self.G, GPIO.LOW)

        # OFF
        elif myColor == 'off':
            GPIO.ouput(self.R, GPIO.HIGH)
            GPIO.ouput(self.B, GPIO.HIGH)
            GPIO.ouput(self.G, GPIO.HIGH)

        # White Color
        elif myColor == 'white':
            GPIO.ouput(self.R, GPIO.LOW)
            GPIO.ouput(self.B, GPIO.LOW)
            GPIO.ouput(self.G, GPIO.LOW)

        

def main():
    myLed = ledRBG(12, 27, 22)
    while True:
        myLed.color('red')
        sleep(1)
        myLed.color('blue')
        sleep(1)
        myLed.color('green')
        sleep(1)
        myLed.color('off')
        sleep(1)
        myLed.color('white')
        sleep(1)


if __name__ == "__main__":
    main()