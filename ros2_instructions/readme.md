# Instructions to setup ROS2 on ubuntu 22.04

### Reasons for choosing.
I decided to install ROS2 Humble on Ubuntu 22.04 (Jammy). The reason is ROS2 Humble is an LTS version, which means Long Terms Support. The EOL for ROS2 Humble is in May 2027.

I decided to go with ROS2 because I thought I should work on something new, rather than again going back to ROS1.

Regarding using a dedicated Ubuntu system, I tried WSL and also virtual machine, but I faced problems with both.


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

### Installation instructions & Environment Setup
ROS2 installation docs -> Binary packages -> Ubuntu Linux - Jammy Jellyfish (22.04) -> [Debian packages](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)


**Remember to add following line to ~/.bashrc**
```
source /opt/ros/humble/setup.bash
```
- `source` is a shell built-in command used to read and execute commands from a file in the current shell. When a script is run using source, any variables or functions it defines will remain available within the shell after the script completes.
- `/opt/ros/humble/setup.bash` is the path to the setup script for ROS humble. Sourcing this script sets up the environment variables needed by ROS in that shell.

`~/.bashrc` file is a script that runs every time you open a bash shell. It initializes an interactive shell session.You can put any command in this file that you can type the terminal.

The above line is added to the end of `~/.bashrc` file so that it's run automatically every time you open a new terminal.

### Running your first ROS2 program
Once the environment has been set up, you can run ROS2 programs to check if everything works. This will also familiarize you with how to run ROS2 programs.

For this we use existing example programs which are downloaded when you install ROS2.

```
# In one terminal, run talker node
ros2 run demo_nodes_cpp talker

# In another terminal, run listener node
ros2 run demo_nodes_cpp listener
```

Each terminal runs a ROS2 program (aka node). Both the nodes are from `demo_nodes_cpp` package (a collection of nodes). 

You must have noticed that both the programs run separately, and stopping one does not stop the other. Hence they are independent, even though the output of `listener` console depends on the output of `talker` console. This is because these independently running programs are communicating with each other. But how? We will learn this later.

Syntax of running a ROS2 node is:
```
ros2 run <pkg_name> <node_name>
```


### Create your own ROS2 Node
To create your own ROS2 programs, you will need a build tool specific to ROS2, called `colcon`. This was created specifically for ROS2.

```
# to install the colcon build tool
sudo apt install python3-colcon-common-extensions

# add following line to ~/.bashrc to enable autocomplete
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

### Creating and setting up ROS2 workspace
#### What is a ROS2 workspace?
It is basically a directory where you store all your code for a ROS2 application. It is also where you compile this code.

#### How to create ROS2 workspace?
```
cd ~
mkdir ros2_ws
cd ros2_ws
mkdir src
```
You can name your workspace directory anything (here `ros2_ws`). There is a convention in ROS community to name workspace directories with `_ws` ending.

In the workspace directory, you create an `src` directory. All the code and packages we create will be in this source code folder.

#### How to build your workspace?
To build your workspace, you can run the following from workspace directory.
```
colcon build
```
As there are no packages in the src folder yet, colcon will build with a message `Summary: 0 packages finished [time]`. This will create 3 more directories in the workspace directory: `build`, `install`, `log`.



#### How to use your built packages?
To use your own packages from your ros2 workspace, you need to source the setup scripts from the install directory of the workspace.

### Creating a package

