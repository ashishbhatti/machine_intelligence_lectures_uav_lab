''' How each detection looks like?
<detectNet.Detection object>
   -- Confidence: 0.820312
   -- ClassID: 62
   -- Left:    88.5938
   -- Top:     142.969
   -- Right:   186.562
   -- Bottom:  278.672
   -- Width:   97.9688
   -- Height:  135.703
   -- Area:    13294.7
   -- Center:  (137.578, 210.82)
'''

import jetson.inference
import jetson.utils
import cv2

''' # opencv is not needed,
You can run the complete detection part using jetson inference and utils.
But to use the opencv functions, we import cv2, and convert image to a format,
opencv understands.
'''

# create a network
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold = 0.5)

# webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    # image that comes from opencv is based on numpy format
    # not recognized by net
    # converting to cuda format
    imgCuda = jetson.utils.cudaFromNumpy(img)

    detections = net.Detect(imgCuda)

    # how to display detections? 2 methods
    # method 1: converting imgCuda to opencv img (easier but inflexible)
    # img = jetson.utils.cudaToNumpy(imgCuda)

    # method 2: overlaying the detections on opencv image
    for d in detections:
        # print(d)
        x1,y1,x2,y2 = int(d.Left), int(d.Top), int(d.Right), int(d.Bottom)
        className = net.GetClassDesc(d.ClassID)
        cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255), 2)
        cv2.putText(img, className, (x1+5, y1+15), cv2.FONT_HERSHEY_DUPLEX, 0.75, (255,0,255),2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
