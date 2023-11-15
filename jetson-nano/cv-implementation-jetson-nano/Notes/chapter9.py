# Robot Car Project

'''
1. Assembly and wiring
2. Motor Test (Arduino)
3. Motor Function (Arduino)
4. Motor Serial (Arduino)
5. Keyboard Control
'''

##############################################
'''
After the assemble and wiring, the first thing you should do when you are building a robot is to test the motors.
We will write the code in such a way that we know which direction we are moving in.
For that we will write code for the forward motion of motors. So, both motors rotating at the same RPM.

'''


'''
KeyboardControl

There are a few methods that we can use to get input from the keyboard.
Example: pygame, library used for creating games using python.

But here we will take a very simple approach, because our main aim is not to control with keyboard, but to make it autonomous.
So, we will use the cv2 library to get the input from the keyboard, and run the robot.

'''