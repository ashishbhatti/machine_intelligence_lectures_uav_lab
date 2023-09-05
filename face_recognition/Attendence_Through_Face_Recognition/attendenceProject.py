import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


path = 'ImagesAttendance'

def findEncodings(images):
    """
    Takes a list of images, and returns the encodings of these images.
    :param images: list of images
    :return encodeList: list of encodings of the images
    """
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def findEncodingsFromPath(pathToKnownFaces):
    """
    Function takes the path to the directory with known faces.
    It finds the labels from the file names and creates the
    encodings for the faces.
    :param pathToKnownFaces: The path to the directory with images of known faces
    :return images: a list of the image encodings
    :return classNames: a list of the names of the known faces
    :return encodeListKnown: a list of the image encodings of known faces
    """
    print(f"Known Faces Directory: {pathToKnownFaces}")
    images = []
    classNames = []
    myList = os.listdir(pathToKnownFaces)
    print(f"Detected Files of Faces: {myList}")
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnown = findEncodings(images)
    print(f"Identified Faces: {classNames}")
    print("Encoding Complete!")
    return images, classNames, encodeListKnown


def markAttendence(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        # print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
    return


images, classNames, encodeListKnown = findEncodingsFromPath(path)
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendence(name)

    cv2.imshow("webcam", img)
    cv2.waitKey(1)
