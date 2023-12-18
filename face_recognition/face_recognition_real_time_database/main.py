import cv2
import os

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


while True:
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img                    # overlay webcam image over background image
    imgBackground[44:44+633, 808:808+414] = imgModeList[3]         # overlay mode images on background image

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


