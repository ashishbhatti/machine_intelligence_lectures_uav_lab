import cv2
import numpy as np
import face_recognition

'''
3 steps:
    1. loading the images and converting into RGB
    2. finding the faces in the image and finding their encodings
    3. comparing the faces and finding the distance between them
'''

# -------------------------------------------------------------------
# loading the images
imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.png')
imgElon = cv2.resize(imgElon, (0, 0), None, 0.5, 0.5)
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# imgTest = face_recognition.load_image_file('ImagesBasic/Elon Musk Test.png')
imgTest = face_recognition.load_image_file('ImagesBasic/Bill Gates.jpg')
imgTest = cv2.resize(imgTest, (0, 0), None, 0.5, 0.5)
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# -------------------------------------------------------------------
# finding faces in the image
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
# print(faceLoc)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# -------------------------------------------------------------------
# comparing the faces
results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'Match: {results[0]}. Distance: {round(faceDis[0], 2)}',
            (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Test Image', imgTest)
cv2.waitKey(0)
