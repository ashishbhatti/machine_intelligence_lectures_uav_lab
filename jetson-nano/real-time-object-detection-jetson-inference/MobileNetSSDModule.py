'''
Steps required to setup the dependencies for the module:

$ sudo apt-get update
$ sudo apt-get install git cmake libpython3-dev python3-numpy
$ git clone --recursive https://github.com/dusty-nv/jetson-inference.git
$ cd jetson-inference
$ mkdir build
$ cmake ../
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig

'''