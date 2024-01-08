# Indoor GPS-denied flight using AprilTags (ROS-based)

I have taken the content from the references, but have adapted it for Jetson Nano. Also note, I have written the lab based on my experiences.

### Outline
1. Before we start
2. System setup
3. Development
3. Ground Test
5. Flight Test
6. Conclusion 

## 1. Before we start
In my experience it is very important to have system powerful enough running Linux, as the main OS or dual-boot. This is because both WSL and VM has additional steps you need to follow to make it work, and everything might not be supported. I have a system with Ubuntu 22.04 installed as the main OS in Dell Inspiron 15 7567.

We need to understand a lot of different libraries and software to make it work. These include Linux (OS), Python (programming language), ROS (middleware b/w your applications and hardware).

One thing that I have learned while working with robots is that **details matter**. You need to modify the commands depending on your particular hardware, firmware and software setup. These commands can be to run the code, to install packages, and to configure the parameters. Even the order in which you run commands can give you different results. Hence keep and eye on the details.

I have tried to add major commands here in this document, even though wiki pages might be there. This is because this document also serves as notes for me. Though I will provide the link to the wiki or documentation from where I take the commands.

## 2. System setup

My hardware setup include:
1. A small quadrotor
2. Companion Computer: Jetson Nano, with 128GB micro SD card running Jetpack 4.6.
3. Raspberrypi Cam v2 
4. Laser range finder (TOF) sensor

Software setup on Jetson Nano:
1. install ROS 
2. install MAVROS
3. connect Nano to ArduPilot using MAVLink
4. connect Nano to ArduPilot using MAVROS
5. 

Prepare the tags board:

Camera calibration:

Configure parameters on Mission Planner:



## 3. Development

## 4. Ground test

## 5. Flight test

## 6. Conclusion