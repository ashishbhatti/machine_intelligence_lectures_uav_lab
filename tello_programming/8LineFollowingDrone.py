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
ROTATION
1. Camera need to face downwards 
    A mirror infront of camera to make it look downwards.
    A clip is available on thingiverse, to attach mirror. Or you can 3D print it. Or just 
    glue it with a glue gun.
    But a cleaner way is to use a thingiverse file by Works-Of-Claye (Tello Mirror Clip).

2. Algorithm (black line following)
    Split the image from camera into three sections: Left, center and right
    This is same method as line follower. 3 regions where we will detect black line.

    If black line in the middle region: go forward
    if black line in right region: rotate right
    if black line in left region : rotate left

    Because we are splitting our image into virtual IR sensors, we can
    split them into as many as we want, say 5.
    But then 2^5 = 32, are too many combinations to handle for a simple problem.

TRANSLATION
Note in the case of line follower robot, the robot could translate in one direction, 
and rotation in one. So, to change the position of robot over the line, the robot can only 
rotate and move forward.

But a drone can translate side to side as well. 
Imagine a situtation, when the line falls in the right region of the drone camera, 
and maybe the drone should translate to the side to keep it centered, rather than rotation.
We have to make sure that the drone is always over the line, that is the line shoulf be in ceter region.
Then only it will be able to tell, when to rotate.

How to solve this?
At every step we will try to find the center of the black line. And check where the drone is wrt this center.
It the drone center is away from line center, we will try to add translation to the drone to match them.


'''