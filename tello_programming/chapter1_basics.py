# This chapter only covers the basic theory

'''
The term drone means 'a continuous low humming sound.'
I prefer the term UAV, that is unmanned aerial vehicles or 
MAV, micro aerial vehicles.

Types of drones:
    1. Quadcopter: 4 rotors / propellers
    2. Hexacoper: 6 rotors
    3. Octocopter: 8 rotors
    Many more:

Components of a drone:
    1. Frame
    2. Motors
    3. Propellers
    4. ESC - Electronic Speed Controllers
    5. PDB - Power Distribution Board
    6. Flight Controller
    7. Battery
    8. Receiver
    9. Camera
    10. VTX - Video Transmitter
    11. Sensors

For description of components check the video: though it
is very basic and you probably know more.

How does a drone fly?
In the video Murtaza says that a quadrotor has 4 degrees
of freedom. This is incorrect. I think he doesn't have a 
background in aerospace that is why he said this.

In reality a quadrotor has 6 degrees of freedom (6DOF). 
But we also know that it is an underactuated system, 
because we can only give 4 inputs, which are rotation speed 
of each of the 4 rotors.

2 props rotate in same direction, while other 2 rotate in opposite.
This balances the angular momentum.

The dynamics of the movements is explained in video simply.

Tello drone is produced by company Ryze. It contains dji and intel
tech for flight control. 
It has a camera attached to it which can shoot upto 720p video at 30fps.

Best part of the drone is that it is programmable.
And using an SDK, the low-level movement control is taken care of
and we can apply high level computer vision techniques without any external wiring.
Everything is done over a wifi, even a router is not required.

Total flight time: 13mins
Total flight distance: 100ms
Top speed: 8m/s


Check the DroneBlocks simulator here: https://pypi.org/project/DroneBlocksTelloSimulator/
For me it is not working as of now.

'''