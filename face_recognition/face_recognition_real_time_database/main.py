import cv2
import os
import pickle

import face_recognition
import numpy as np
import cvzone
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# firebase credentials based on serviceAccountKey file
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-271223-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-271223.appspot.com"
})

bucket = storage.bucket()

# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# importing the mode images into a list for easy retrieval
imgBackground = cv2.imread('Resources/background.png')
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# load the encodings file
print("Loading Encode File ...")
file = open("EncodeFile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded.")

# initialization
modeType = 0                                                         # active
counter = 0                                                          # frame counter
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # face recognition
    facesCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

    # overlay images on top of background
    imgBackground[162:162+480, 55:55+640] = img                      # overlay webcam image over background image
    imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]    # overlay active on background image

    if facesCurrFrame:

        # for all the faces detected in the frame
        for encodeFace, faceLoc in zip(encodeCurrFrame, facesCurrFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)                              # face with least face distance

            # if face with least face distance is a match
            if matches[matchIndex]:
                # print("Known Face Detected")
                # print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]

                # if match found, set the counter to 1 and modeType to details
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275,400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1                                         # details

        # if match was found in frame
        if counter != 0:

            # if a new match
            if counter == 1:
                # get the data from realtime database
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                # get the image from storage
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                # update data of attendance
                datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                  "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)

                # update attendance only if more than 30 seconds passed from last attendance
                if secondsElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    studentInfo["total_attendance"] += 1
                    ref.child("total_attendance").set(studentInfo["total_attendance"])
                    ref.child("last_attendance_time").set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3                                         # already marked
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            # if already marked
            if modeType != 3:

                # if a very old match
                if 10 < counter < 20:
                    modeType = 2                                             # marked

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]  # overlay details/marked on background image

                # if relatively recent match
                if counter <= 10:
                    # put details of the student on the image
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']),
                                (861, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['major']),
                                (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id),
                                (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['standing']),
                                (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['year']),
                                (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['starting_year']),
                                (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    # centering the name
                    (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w)//2
                    cv2.putText(imgBackground, str(studentInfo['name']),
                                (808+offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    # putting image of student on the main image
                    imgBackground[175:175+216, 909:909+216] = imgStudent

                counter += 1

                # if a very very old match
                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]  # overlay mode image on background image
    else:
        modeType = 0
        counter = 0

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
