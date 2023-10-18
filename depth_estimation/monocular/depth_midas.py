'''
Author: Ashish Kumar
Date: September 19, 2023
Place: UAV Lab, IIT Kanpur
'''
# Import dependencies
import cv2
import torch
import matplotlib.pyplot as plt
import time
import numpy as np

# Select a model type of MiDaS model for depth estimation
# model_type = "DPT_Large"         # MiDaS v3 - Large (highest accuracy, slowest inference speed)
# model_type = "DPT_Hybrid"        # MiDaS v3 - Hybrid (medium accuracy, medium inference speed)
model_type = "MiDaS_small"       # MiDaS v2.1 - Small (lowest accuracy, highest inference speed)


# Download the MiDas
midas = torch.hub.load('intel-isl/MiDaS', model_type)

# Select device, move model to GPU if available
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)             # midas.to('cpu') 
midas.eval()

# Models are trained on a particular image size0
# Load transforms to resize and normalize the image
# Input transformation pipeline
transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')


if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = transforms.dpt_transform
else:
    transform = transforms.small_transform

# Capturing from webcam using opencv
cap = cv2.VideoCapture(0)

# # Define the codec and create a VideoWriter object for MP4
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Codec for MP4 format
out_frame = cv2.VideoWriter('output_frame.mp4', fourcc, 20.0, (640, 480))  # Output file for frame
out_depth = cv2.VideoWriter('output_depth.mp4', fourcc, 20.0, (640, 480))  # Output file for depth map


while cap.isOpened():
    success, frame = cap.read()    # Reading the frame

    start = time.time()

    # Tranform input for midas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Correcting color format
    imgbatch = transform(img).to(device)           # Applying input transform

    # Make a prediction and resize to original resolution
    with torch.no_grad():
        prediction = midas(imgbatch)
        
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size = img.shape[:2],
            mode = 'bicubic',
            align_corners = False
        ).squeeze()
        
        depth_map = prediction.cpu().numpy()
        # print(depth_map)

    end = time.time()
    total_time = end - start
    fps = 1.0 / total_time
    
    # Viewing depth_map with opencv
    depth_map = cv2.normalize(depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_64F)
    depth_map = (depth_map*255).astype(np.uint8)
    depth_map = cv2.applyColorMap(depth_map, cv2.COLORMAP_MAGMA)

    cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
    
    # Write the frame and depth map to separate output video files
    out_frame.write(frame)
    out_depth.write(depth_map)
    
    # Display the frame and depth map
    cv2.imshow('Frame', frame)
    cv2.imshow('Depth Map', depth_map)

    # Viewing with matplot lib
    # plt.imshow(depth_map)
    # plt.pause(0.00001)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        out_frame.release()
        out_depth.release()
        cv2.destroyAllWindows()
        break

plt.show()