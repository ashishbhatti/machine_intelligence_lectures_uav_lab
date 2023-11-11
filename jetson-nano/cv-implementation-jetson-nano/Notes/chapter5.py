'''
## Concept of Modules

Example of a building A car.
A car has many different components, engine, seats, wheels, entertainment system.
These components are manufactured in different factories, not in same place. But will be assembled together.

So, if one component is faulty, only that component needs to be replaced, rather than changing eerything.

# ------------------------------------------------------------------------------------------------------
Similarly, your project needs to be divided into separate components called modules.
This is done, so that the project is more manageable in the long run.


Coding example of a smart car, object following.
A car detects object of a particular color and turns towards it.

Object Detection (Color detection) module.
Wheel Rotation module.

Main code between them:
1. will ask color detection module to send the location of the colored object.
2. based on that the rotation module will rotate the wheels.

In reality these modules are just files which have scripts of code.
WHen you have modules and you put them together, it becomes a package or library.

We will focus only on modules.
Take Color Detection module for example.
There can be many different functions and variables inside this module, say to find the coloe, then to find xm yposition, then to change the size, etc.
I will just call these functions in the main code.

Once we create a color module, we can use it in many projects. And if we change it, we can call the new version.
This way, it will be very easy to maintain the code, and we can use the same thing in many different projects.


# ----------------------------------------------------------------------------------------------------
Here is a list of all the modules we will be creating in this course.
1. Color Detection             # will allow us to detect any kind of color, will give us image of detected color
2. Face Recognition            # we find, which person is detected in the image, bill gates, elon musk etc
3. Shape Detection             # detect contours and will tell which shape, rectangle, square, circle. Differentiate between different shapes.
4. Arduino Serial              # Communicate with arduino, using simple commands, get sensor values from arduino
5. Object Detection            # find an object and give a bounding box around it
6. RGB LED                     # To control the LED color, using one command
7. Real Time Database          # send our info to a real time database, say a website
'''
