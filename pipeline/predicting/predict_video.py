import cv2
import os
from ultralytics import YOLO


W = 1280
H = 720
CONFIDENCE = 0.5


# Load the YOLOv8 model
model_path = os.path.join('.', 'runs', 'detect', 'train33', 'weights', 'best.pt')
model = YOLO(model_path)

# path to original video
video_path = "intermediate_data\\videos\\orig\\exp351_sub2_child.mp4"

# path and name of output file -- currently uses old name and appends run info
video_path_out = 'intermediate_data\\videos\\predicted\\{}_s_run33.mp4'.format(video_path.split('\\')[-1][:-4])

cap = cv2.VideoCapture(video_path)
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, imgsz=W, conf=CONFIDENCE,)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # write frame to videoWriter
        out.write(annotated_frame)
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()
