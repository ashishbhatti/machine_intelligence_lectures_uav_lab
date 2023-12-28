# Real Time (24-FPS) Object Detection on Jetson Nano

This project is based on this video by Murtaza's Workshop youtube channel. The code is based on [`jetson-inference`](https://github.com/dusty-nv/jetson-inference) github repo by [`dusty-nv`](https://github.com/dusty-nv) (Dustin Franklin), who is a Jetson Developer at NVIDIA. 

We will create an Object Detection Module named `MobileNetSSDModule`, so that we can use it with other projects and so that we can switch modules, keeping the rest of the code same.

The file structure is :
- `bare_min_test.py` : Absolutely bare minimum code required to run object detection.
- `MobileNetSSDModule.py` : Module which can be used in other projects.
- `project_test.py` : File to help us see how we can use this module in a different project.
