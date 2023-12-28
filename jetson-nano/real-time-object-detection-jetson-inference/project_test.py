import cv2
import MobileNetSSDModule as mnSSDm

# webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

myModel = mnSSDm.mnSSD("ssd-mobilenet-v2", 0.5)

while True:
    success, img = cap.read()
    objects = myModel.detect(img, True)
    if len(objects) != 0:
        print(objects[0][0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)