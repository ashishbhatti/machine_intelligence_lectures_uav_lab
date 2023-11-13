'''
# ----------------------------------------------------------------------------------------
# Working with arduino

Arduino is the most popular platform, for working with sensors and motors.

Steps:
1. We will connect sensors and motors to arduino.
2. We will communicate with arduino using serial communication (using the usb connection).
We won't need anything extra to connect arduino with nano, other than the arduino cable. 

So, we will connect it to one of usb ports of nano.


# ----------------------------------------------------------------------------------------
# Example to understand: Sending multiple values

 to send different brightness values to LED lights?
If you want to send analog output in arduino, it uses 8bits. That is 0 to 266.
Maximum digits we can have is 3 digits.

Let's say we have 2 LED brightnesses. How to send it to arduino? Say 50255.
To do this we will always have 3 digits for the brightness, whenever we are sending 
the value, we will make sure it has 3 digits for each value.

Now the message looks like this 050255
But to arduino it will look like this: 050255050255050255......
To help arduino know where to start, we will add a $ sign
$050255$050255 ......
After the dollar sign we will extract next six digits.
First 3 digits for first LED and last 3 for second LED.


## I faced a problem while installing arduino uno board libraries. The problem was IIT Kanpur
Firewall was not allowing the connection. If you connect and install using mobile data, it should work.

# --------------------------------------------------------------------------------------------------

# Arduino Code:
2 main funcions.
1. void setup(): which devices inputs and outputs
2. void loop(): write your actual code
3. Before setup you declare and initialize constants and variables


# ---------------------------------------------------------------------------------------------------

Read the code at the relative path below.
# ../Arduino/SerialArduino/SerialArduino.ino
Arduino Serial Read Code.


if you get an error that can't open serial port, access denied.
use !sudo chmod 666 /dev/ttyACM0

# ---------------------------------------------------------------------------------------------------

# SerialModule.py
Python Serial Write Module Read Cod.
1. Using serial library of python-3
2. We can talk to arduino using this.

!sudo apt-get install python3-serial
>>> import serial


'''
