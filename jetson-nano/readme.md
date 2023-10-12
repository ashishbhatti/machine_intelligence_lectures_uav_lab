# Running your first DL algorithm on Jetson Nano
This repository contains my documentation regarding starting with using jetson nano and running your first algorithm. I have tried to list all the steps, and the roadblocks I encountered and how I solved those, along the way. Hope this helps!


## Outline

- Prerequisites
- Getting started with first boot
- Installing the required packages
- Running your first algorithm

## Prerequisites

1. Where to buy?

If you visit the [Buy the Latest Jetson Products](https://developer.nvidia.com/buy-jetson) webpage, upon entering your required jetson board and location, you can see the Nvidia authorized sellers. 

I tried to contact both the authorized sellers and decided to buy the board from [ThinkRobotics](https://thinkrobotics.com/products/nvidia-jetson-nano-developer-kit-b01-4gb). You can also go with Robu, depending on your order timeline. Both of them offer better communication and quick resolution of complaints, than the Nvidia authorized dealers. This was my experience, though yours can be different.

2. What to buy?

[Nvidia Jetson Nano Developer Kit B01](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) is a great platform to protype and test your Deep Learning models. I began with this because of Lab bought these first. Also if possible try to pick the version with higher RAM, in this case 4GB.

3. Additional items you will need.

    1. Micro-SD card 32 GB or above
    2. Monitor
    3. Keyboard and Mouse
    4. LAN connection or wireless module
    5. Camera (USB-webcam or RPi Camera V2)
    6. Card reader
    7. Power adapter 5V-2A, and a micro-usb cable


## Getting started with first boot

Follow closely this guide [Get Started With Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) from Nvidia. It is extremely detailed and will answer all your questions. 

For my case there was a problem with the Jetpack file I downloaded, from this guide. If you encounter the same issue, go to the [Jetpack Archive](https://developer.nvidia.com/embedded/jetpack-archive) and download an image supported for jetson nano. Rest of the steps are the same.


Note that there is another software called [DeepStream](https://developer.nvidia.com/deepstream-getting-started). We will talk about that once we are done with setting up our first app.



## Installing the required packages

Now Jetpack already comes with most of the required packages pre-installed. These packages include:
- CUDA
- cuDNN
- TensorRT


We will install the required packages along the way, being careful about the supported versions.


## Running your first algorithm

I will chose to run face detection code on Jetson Nano as my first DL algorithm. 














