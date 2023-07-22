'''
Odometry Problem: How to localize the drone in the surroundings?

We will take the velocity information, to find the distance.
We will also use angular speed, to find the angle of drone,
or where it is headed. Based on this we will find the x,y coordinates
of the drone.

So, we will take the distance and angle and we will convert it into
cartesian coordinates, and plot it into a graph.

# Translation
Distance = Speed x Time

# Rotation
Angle (Heading) = AngularSpeed x Time

# How to calculate when both are pressed? forward and rotation
We will find coordinates after every unit of time, so we will
have intermediate positions.

'''