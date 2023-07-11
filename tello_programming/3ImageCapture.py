# boilerplate for tello drone
from djitellopy import tello

me = tello.Tello()
me.connect()              # this takes care of ip connections and communication
print(me.get_battery())


import cv2

# Image capture
me.streamon()

while True:
    img = me.get_frame_read().frame
    # img = cv2.resize(img, (360,240))        # keeping size small for faster computation
    cv2.imshow("Image", img)

    cv2.waitKey(1) 



'''
We can see a delay in frames, this is because of transfer and viewing. 
In reality this delay is not too much. The delay is introduced because
we are viewing it and performing graphical computations on the frames.
'''