'''
## Object detection module
Viola Jhones Method

How to detect objects in an image?
How to use Haar Cascade files to detect different objects?

For a module ensure:
1. It can run by itself
2. It should be accessible by other scripts as well

How to steps:
1. Write code so that it works when you run as script, so write a main() funtion
2. Break it down into functions
3. Write file and function docstrings
'''

import cv2

def findObjects(img, objectCascade, scaleFactor = 1.1, minNeighbors = 4):
    '''
    finds objects using the haarcascade file, draws bboxes over faces,
    and returns the bbox values.

    :param img: Image in which the objects needs to be found
    :param objectCascade: Object Cascade created with Cascade Classifier
    :param scaleFactor: how much the image size is reduced at each image scale
    :param minNeighbors: how many neighbors each rectangle should have to accept as valid
    :return: image with the rectangles drawn and the bounding box info 
    '''
    imgObject = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # optional
    
    # find objects in image
    objects = objectCascade.detectMultiScale(imgGray, scaleFactor, minNeighbors)
    # image, scale factor, min neighbors (changing these speed accuracy tradeoff)

    # drawing bounding box over faces
    for (x,y,w,h) in objects:
        cv2.rectangle(imgObject, (x,y), (x+w, y+h), (255,0,255), 2)

    return imgObject, objects


def main():
    img = cv2.imread("../Resources/test_image.png")

    # import the file which has information of detection, here face cascade but can by anything
    faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml")
    imgObject, objects = findObjects(img, faceCascade)
    cv2.imshow("Output",imgObject)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()