# Face Recognition Attendance Real Time Database

This project is based on [this tutorial](https://youtu.be/iBomaK2ARyI?si=MYhYFiHieqHx_lOr) by Murtaza's Workshop Youtube Channel.

The project uses the `face_recognition` library, and the algorithm is explained in [this article](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78). The library uses HOG descriptors.


### Instruction to run
- Add the known faces to `Images` directory. Give them an id, and make sure these are 216x216 images.
- Make a firebase project and activate the Realtime Database and Storage. Download and save the service account key as `serviceAccountKey.json` in the parent directory.
- Run the `EncodeGenerator.py` file. This will create the encodings of the known faces and will store this information in `EncodeFile.p` pickle file. This will also store the images to the firebase storage.
- Run the `AddDataToDatabase.py` file to add the id information of the people in the images folder.
- Run the `main.py` file.


\
This project requires the following dependencies: \
`cmake`
`dlib`
`face_recognition`
`cvzone`
`numpy`
`opencv-python`
`firebase-admin`


