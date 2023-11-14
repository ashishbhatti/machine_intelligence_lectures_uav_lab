# Eye Tracking Project

'''
# ------------------------------------------------------------------------------------
# Introduction 

Process of Eye Tracking
Idea is:
1. We have a camera inside our eye bot.
2. We get the image of the person.
3. Whenever a person moves, we will be able to track them.
4. 2 types of movements: Left and Right, Up and Down: We will consider both individually.

For the left and right movement.
Whenever the person moves left or right, we will move the camera such that the person's 
image moves towards the center.
So, always try to keep the center line, at the center of the object detected or person detected. 
So, camera rotation is required. 

What happens if you rotate too fast, and due to which, the person overshoots the center line?
For, the offset, we can rotate back, again it will overshoot. How to make it settle?
Gradual decrease in rotation speed, when you get closer to the object. 
So, you get slower and slower. (PID) Proportion, Integral and Derivative: 
These terms check the error and based on that error, we multiply the terms.

We can follow the same process in up and down, as well. 
Again we will have PID for smooth control, rather than jittery movement.
We will use proportional and derivative terms, and not integral terms. 
This will give us good results as it is, so we won't need integral.


# -------------------------------------------------------------------------------------
# Assembly 
Depending on the use case. Also check the tutorial video.


# -------------------------------------------------------------------------------------
# Wiring 

Servo1: Pan (Left Right)
    Ground: Arduino Ground (Common)
    VCC: 5V Arduino (Common)
    Signal: Arduino PWM Pin 9

Servo2: Tilt (Up Down)
    Ground: Arduino Ground (Common)
    VCC: 5V Arduino (Common)
    Signal: Arduino PWM Pin 10


# -------------------------------------------------------------------------------------
# Motor Center 

After the assembly and wiring, we will do the following:

1. Center our servos : Find the middle of our servo range.
2. Max and Min: Find the maximum and minimum of servo range.

Arduino -> Examples -> Servo -> Sweep

Using this we find the center of the servos, then mount the servo horn.
Then check the range of motion for the assembly.

Check: Eye_Center.ino

# -------------------------------------------------------------------------------------
# Serial Control 

Main arduino code that will run at the backend to receive the commands from our python code.
This will send the commands to our servo motors.

We are expecting 2 servo values, range 0 to 180, each one can have 3 digits max.

Check: EyeTracking.ino
Check: EyeTrackingWithoutDelay.ino

Test by sending values through serial monitor.

# -------------------------------------------------------------------------------------
# Python Code

EyeTracking_Project Folder: Contains everything that is related to this project.
Following files:
1. haarcascades file : will allow us to detect faces
2. ObjectDetectionModule: Has the function that will detect faces for us
3. SerialModule: That will send the command to motors.
4. test.png: for testing

All these are taken from previous chapters,
all we have done is created a new folder and copied the files in it.

but:
ObjectDetectionModule is updated so, version 1.2. 
We have just sorted the objects detected list, so the biggest object is the first.


EyeTracking.py file: Check it.

This file imports the modules we created and does the job.



# -------------------------------------------------------------------------------------
# Result

Run the EyeTracking.py file
'''