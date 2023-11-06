import cv2
import time

def capture_image():

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # image appear too bright because the first frame is captured, 
    # to stop this 3 second wait
    time.sleep(3)


    try:
        # Capture a single frame
        success, frame = cap.read()
        if not success:
            print("Error: Could not read a frame.")
            return 
        
        # save the captured frame as an image
        cv2.imwrite('test.png', frame)
        print("Image capture successfull!")
    finally:
        # release the camera
        cap.release()


if __name__ == "__main__":
    capture_image()