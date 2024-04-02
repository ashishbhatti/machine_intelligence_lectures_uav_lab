# Instructions to setup ROS2 on ubuntu 22.04

I decided to install ROS2 Humble on Ubuntu 22.04 (Jammy). The reason is ROS2 Humble is an LTS version, which means Long Terms Support. The EOL for ROS2 Humble is in May 2027.

I decided to go with ROS2 because I thought I should work on something new, rather than again going back to ROS1.


## Upon fresh Ubuntu install

Run these commands after fresh ubuntu install:

```
sudo apt update
sudo apt upgrade
sudo apt autoremove

sudo apt install build-essential
sudo apt install build-essential gcc make perl dkms
sudo apt install python3-pip

sudo apt install terminator
```


## ROS2

### Installation & Environment Setup
```
```


**add following line to ~/.bashrc**
```
source /opt/ros/humble/setup.bash
```


### Create your own ROS2 Node
To create your own ROS2 programs, you will need a build tool specific to ROS2, called `colcon`. This was created specifically for ROS2.

```
sudo apt install python3-colcon-common-extensions

# add following line to ~/.bashrc
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

### Creating a workspace
```
cd ~
mkdir ros2_ws
cd ros2_ws
mkdir src
```

All the code and packages we create will be in the source code folder.