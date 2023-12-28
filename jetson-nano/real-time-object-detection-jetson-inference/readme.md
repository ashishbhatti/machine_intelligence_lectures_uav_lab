# Real Time (24-FPS) Object Detection on Jetson Nano

This project is based on this video by Murtaza's Workshop youtube channel. The code is based on [`jetson-inference`](https://github.com/dusty-nv/jetson-inference) github repo by [`dusty-nv`](https://github.com/dusty-nv) (Dustin Franklin), who is a Jetson Developer at NVIDIA. 

We will create an Object Detection Module named `MobileNetSSDModule`, so that we can use it with other projects and so that we can switch modules, keeping the rest of the code same.

### Setup the dependencies 

Run the following commands:
```
$ sudo apt-get update
$ sudo apt-get install git cmake libpython3-dev python3-numpy
$ git clone --recursive https://github.com/dusty-nv/jetson-inference.git
$ cd jetson-inference
$ mkdir build
$ cmake ../
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig
```

Download the `SSD-Mobilenet-v2` model by running the following commands and selecting the model.
```
$ cd jetson-inference/tools
$ ./download-models.sh
```

You can skip pytorch installation, it is not required.


### The file structure 
- `bare_min_test.py` : Absolutely bare minimum code required to run object detection.
- `MobileNetSSDModule.py` : Module which can be used in other projects.
- `project_test.py` : File to help us see how we can use this module in a different project.


