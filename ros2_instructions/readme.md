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

So, 4 folder in the ROS2 workspace (after building) contain:
- `src` : source code folder, the code of all the packages and their nodes.
- `build` : intermediate files, Makefiles, and package-specific directories for and generated a part of the compilation process.
- `install` : shell setup scripts, source inorder to use whatever you have created in workspace.
- `log` : log (a written record) of the build process.

Typically you don’t need to interact with these folders directly, except the `src` folder. You just use colcon commands to build your workspace, and it handles the details of the rest of the process.


#### How to use your built packages?
To use your own packages from your ros2 workspace, you need to source the setup scripts from the install directory of the workspace.

##### Which one to source?
- `local_setup.bash` :  this script simply sets up the environment for only the packages in your own workspace (that we call as an overlay). It **does not** include the environment settings from any underlying global ros2 installation ( underlay).
- `setup.bash` : will set up the environment for both, the packages in this workspace and the packages in the underlay workspace, which is global ros2 installation. This means it includes both your workspace (overlay) and the global ROS2 installation (underlay).

To avoid confusion here we will source `setup.bash`. Add the following line at the end of `~/.bashrc`.
```
source ~/ros2_ws/install/setup.bash
```


### Creating a package

#### Why do we need a package?

To create a ros2 node we need a package first. Packages allow you to separate your code into reusable blocks. Each package is an independent unit, which contains many different nodes.

#### How to create a package?
```
# navigate to the ros2 workspace src directory
cd ~/ros_ws/src

# create a new package
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

In ros2 there is a difference between the python and cpp package. Hence, we need to specify the `--build-type` flag at the time of creating the package. Also our package can depend on other packages, which can be added via the `--dependencies` flag.

Here we create a package with name `my_py_pkg`, with specific properities:
- `--build-type` is `ament_python`. `ament` is the build system, and `ament_python` means that you want a python package.
- `--dependencies` is used to simply specify other packages on which our package relies on. `rclpy` we us in all of the ros2 python programs, because it is ros2 python library. We need this to write ros2 code in python.


The above command creates a directory in the `src` folder with name `my_py_pkg`. This package directory contains the following files and folders:
- `my_py_pkg` folder: This folder has the same name as the package directory, and will always have. In this folder you will put all your python nodes. It already includes an `__init__.py` file, which is required for Python to recognize this directory as a package. You don’t need to touch this file.
- `resource` folder: This folder is used to store resource files that your package might need. These could be things like configuration files, data files, etc. Ignore this for now.
- `test` folder: This folder is where you can put your test files. It already contains three test files as examples.
- `package.xml` file: Every ros2 package, whether it’s written in python or cpp, must have a package.xml file in the root directory of ros2 package. It provides metadata (data about data) about the package, basically 2 things: about the package and package dependencies and build type. If you need to add a new dependency, you can add another depend tag here.

- `setup.cfg` file: The two setup files are useful to install nodes in your environment, which we will see later. For now, this file is used for the configuration of setuptools, which is a library in Python used to distribute Python packages. It can include information about the package version, required packages, scripts, and more. In simple words, this is like a recipe for your Python package. It tells Python what ingredients (or packages) are needed and how to prepare (or configure) them. It also includes details like the version of your package.
- `setup.py`: This is the build script for setuptools. It tells setuptools about your module/package and how to install it. It can define metadata about your package and also custom build commands. In simple words, this is like the cooking instructions for your Python package. It tells Python how to make (or build) your package and get it ready for use. It can also include extra details about your package.


Syntax of creating  a new ROS2 package is:
```
ros2 pkg create <new_pkg_name> --build-type <ament_python/ament_cmake> --dependencies <other_packages>
```
Remember to run this from workspace src directory.

Your package in now ready.

#### How to compile your package?
```
# go to ros2 workspace
cd ~/ros2_ws

# command to build the entire workspace
colcon build

# command to build select packages
colcon build --packages-select my_py_pkg
```
The last command allows you to only compile the packages you made changes in, or the ones you want to test. So development time is much shorter.

Your python package is now ready to house any python node.


### Creating a Node

#### What is a Node?
It is a subpart (subprogram) of your application and it should have a single function. This means it is responsible for only one thing. You can think of it as a single file which contains code which has a single functionality.

Nodes are combined into a graph. They communicate with each other through topics, services and parameters.

#### Why do we need nodes?
Nodes reduce code complexity. If you correctly separate your application in packages and nodes, then it will be much easier later to scale your application. If you write everything in one file, then after a stage you spend more time in debugging than in building new functionality.

Nodes also make your system fault tolerant. If one node crashes, your entire application will not crash.

You can write nodes in cpp and python, and both nodes can communicate with each other. Hence they make ros2 language agnostic. You can also use other languages. This means you can choose to develop your entire app in python, but some nodes in cpp because they need fast execution speed.

Two nodes can't have the same name. Hence, make sure all node names are unique.

#### Writing your own node
```
# go to your package directory
cd ~/ros2_ws/src/my_py_pkg

# go to nodes folder of package (same name as package)
cd ./my_py_pkg

# create your node file
touch my_first_node.py
```

#### How to install your own node?



#### How to run your own node?



#### Improving your node with OOP



#### Node Template





