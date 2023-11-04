"""
Author: Ashish Kumar
Place: UAV Lab, IIT Kanpur
Date: November 04, 2023
"""

"""
Run this code to test the following:
1. If OpenCV is functioning
2. If camera is being detected.

This code should produce a warning:

[ WARN:0] global /home/nvidia/host/build_opencv/nv_opencv/modules/videoio/src/cap_gstreamer.cpp (933) 
open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
Gtk-Message: 16:21:29.160: Failed to load module "canberra-gtk-module"

This is not a bug, but very normal.
This indicates that the live stream has no duration, so its current location cannot be computed. 
This is harmless for a live source which is camera.
"""

import cv2

# set the resolution to work with
w, h = 360, 240

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (w,h))

    # display the frame in a window
    cv2.imshow('Resized Camera Feed', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
