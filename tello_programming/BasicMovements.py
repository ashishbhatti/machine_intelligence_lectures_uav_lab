from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()              # this takes care of ip connections and communication

print(me.get_battery())

me.takeoff()

# controlling our drone through speed
me.send_rc_control(0, 50, 0, 0)                   # forward 50
sleep(2)
me.send_rc_control(0, 0, 0, 0)                    # stop forward movement
me.land()