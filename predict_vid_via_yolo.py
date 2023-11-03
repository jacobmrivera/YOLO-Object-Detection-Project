import cv2
import os
from ultralytics import YOLO

# Load the YOLOv8 model
model_path = os.path.join('.', 'runs', 'detect', 'train33', 'weights', 'best.pt')
model = YOLO(model_path)

source = 'intermediate_data\\videos\\orig\\exp351_sub2_child.mp4'

# Run inference on 'bus.jpg' with arguments
# model.predict(source, stream=True, save=True, imgsz=1280, conf=0.1, save_dir='.')
results = model(source, stream=True, imgsz=1280, conf=0.1,)

# Open the video file
video_path = "intermediate_data\\videos\\orig\\exp351_sub2_child.mp4"
# video_path = "path/to/your/video/file.mp4"

video_path_out = 'intermediate_data\\videos\\predicted\\{}_s_run33.mp4'.format(video_path.split('\\')[-1][:-4])
print(video_path_out)

W = 1280
H = 720

# cap = cv2.VideoCapture(video_path)
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Loop through the video frames
while results():
    # Read a frame from the video
    # success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        # cv2.imshow("YOLOv8 Inference", annotated_frame)
        out.write(annotated_frame)
        # Break the loop if 'q' is pressed
    #     if cv2.waitKey(1) & 0xFF == ord("q"):
    #         break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()
