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

import jetson_inference
import jetson_utils
import cv2


class mnSSD():
    # intializing instance variables
    def __init__(self, path, threshold):
        self.path = path
        self.threshold = threshold
        self.net = jetson_inference.detectNet(self.path, self.threshold)

    # method to detect
    def detect(self, img, display=False):
        imgCuda = jetson_utils.cudaFromNumpy(img)
        detections = self.net.Detect(imgCuda, overlay="OVERLAY_NONE")   # don't overlay bboxes on the image

        objects = []
        for d in detections:
            className = self.net.GetClassDesc(d.ClassID)
            objects.append([className, d])
            
            if display == True:
                x1,y1,x2,y2 = int(d.Left), int(d.Top), int(d.Right), int(d.Bottom)
                cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255), 2)
                cv2.putText(img, className, (x1+5, y1+15), cv2.FONT_HERSHEY_DUPLEX, 0.75, (255,0,255),2) 
                cv2.putText(img, f'FPS: {int(self.net.GetNetworkFPS())}', (30, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0),2) 
            else: 
                print((self.net.GetNetworkFPS()))
        return objects

def main():
    """
    Implements object detection based on MobilenetSSD-v2
    """
    # webcam
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    myModel = mnSSD("ssd-mobilenet-v2", 0.5)

    while True:
        success, img = cap.read()
        objects = myModel.detect(img, False)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()