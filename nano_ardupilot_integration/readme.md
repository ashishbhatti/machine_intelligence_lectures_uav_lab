# ArduPilot and Jetson Nano integration for GPS-denied UAV applications

This blog documents my journey of learning how to control my UAV using my own vision algorithms.

I will fill in the topics as I progress. The main purpose of this blog is to learn how to send command from companion computer, in our case Jetson Nano, to the ardupilot stack on pixhawk. For this, both ROS-based and non-ROS methods will be tested.

The blog follows the following outline.
#### Outline

1. Introduction
2. Hardware Setup
    - The hardware used, including the drone, the Pixhawk flight controller, and the Jetson Nano.
    - A step-by-step guide on how to connect the Pixhawk to the Jetson Nano.
3. Software Setup
   - Set up the Jetson Nano and the necessary software packages.
   - A guide on how to configure the Pixhawk for MAVLink communication.
4. Code Explanation
   - The Python code used for MAVLink communication.
   - The code explained in detail, including how it interacts with the Pixhawk and controls the drone.
5. Testing and Results
   - How to test your setup?
   - Test results.
6. Conclusion
   - Summary the blog post.
   - My final thoughts, future plans, or any other concluding remarks.
7. References
8. Progress Tracker
   - My progress documented as part of milestones and labs.
   - Project: An implementation exercise.


## 1. Introduction
As part of my work in Machine Intelligence Team at UAV Lab IIT Kanpur, I realised that there are very few tutorials available which one can follow to integrate Jetson Nano, and Flight Controllers. The documentation available is also scattered, which made it difficult for me to develop and test my applications. So, I decided to write a series of blog posts as instruction for the same. 

Disclaimer: This blog post has methods which I have tested to be working in my system, and also other systems in the lab. But I DO NOT gaurantee that they will work on yours.

The main area of my work in the lab involves developing programs for fixed wing UAVs, but the major part of this blog post is written for multirotors. I hope the skills and techniques will translate. Nonetheless, I try to run the program on a fixed wing UAV in AirSim as a project.

Flying a UAV in unfamiliar outdoor environments is important for many applications. The challenge is this case is the localization of the UAV and navigation through the unknown environment. Ofcourse sensors like inertial navigation sensors and GPS become extremely useful in this scenario. But there are scenarios where the GPS sensor might not be available, or jammed. One such scenario of my own interest is when a UAV is flying on a different planet, say Mars. Another application is indoor flying. In these cases, when GPS cannot be used, we can use cameras. This opens up UAVs to the entire field of computer vision technologies. One such technology, that has the capability to provide accurate, robust GPS-denied localization and navigation is Visual Inertial Odometery (VIO). This combines information from a camera and an interial sensor to tell the UAV where it is in relation to ists environment.

In this blog post I will provide documentation with step-by-step instructions, so that anybody can follow and develop their own computer-vision based UAV applications in the future.


## 2. Hardware Setup


## 3. Software Setup


## 4. Code Explanation


## 5. Testing and Results


## 6. Conclusion


## 7. References
1. This blog post is inspired from [GSoC 2019: Integration of ArduPilot and VIO tracking camera for GPS-less localization and navigation](https://discuss.ardupilot.org/t/gsoc-2019-integration-of-ardupilot-and-vio-tracking-camera-for-gps-less-localization-and-navigation/42394).


## 8. Progress Tracker

#### Labs
As part of my journey, I will write a series of labs in the form of blog posts. These serve as the milestones and as the step-by-step guideline for anyone who wishes to learn. Many of the labs are directly inspired from the references.


The labs include:

| # | Lab | Description |
| - | --- | --- | 
| 1 | Lab 1 | Indoor non-GPS flight using AprilTags (ROS-based) |
| 2 |     |     |
| 3 |     |     |
| 4 | Lab 4 | Flying your UAV in AirSim |
| 5 |     |     |
| 6 |     |     |
| 7 |     |     |


#### Project: An implementation exercise.
1. Fixed-Wing UAV in AirSim: Control through companion computer.
