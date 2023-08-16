'''
In this project we are going to create a line following drone.
The idea of Line Following Drone, comes from line follower robot.
We will see how line follower robot works and how to implement 
same methodology in the drone. 

First, let us check how line follower robot works:
Let us assume we have an 3 IR sensors, which detect if line is black.
We have 2^3 = 8 possibilities.

0  1  0    # go forward
0  0  1    # go right
0  0  1    # go right
0  1  1    # slight right
1  1  0    # slight left
0  0  0    # stop, because not possible
1  1  1    # stop, because not possible
1  0  1    # stop, because not possible


How to implement it on drone?


'''