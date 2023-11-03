# import os

# from ultralytics import YOLO
# import cv2


# VIDEOS_DIR = os.path.join('.', 'videos')

# # video_path = os.path.join(VIDEOS_DIR, 'test0_16963.MOV')
# video_path = os.path.join(VIDEOS_DIR, 'test1_16963_cam08.MOV')


# video_path_out = '{}_out_70_conf.mp4'.format(video_path)

# cap = cv2.VideoCapture(video_path)
# ret, frame = cap.read()
# H, W, _ = frame.shape
# W = 720
# H = 480
# out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'best.pt')
# # model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'last.pt')

# # Load a model
# model = YOLO(model_path)  # load a custom model

# threshold = 0.5

# while ret:

#     results = model(frame)[0]

#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result

#         if score > threshold:
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#             cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3, cv2.LINE_AA)

#     out.write(frame)
#     ret, frame = cap.read()

# cap.release()
# out.release()
# cv2.destroyAllWindows()

import cv2
import os
from ultralytics import YOLO

# Load the YOLOv8 model
model_path = os.path.join('.', 'runs', 'detect', 'train33', 'weights', 'best.pt')
model = YOLO(model_path)

# Open the video file
video_path = "intermediate_data\\videos\\orig\\exp351_sub2_child.mp4"
# video_path = "path/to/your/video/file.mp4"

video_path_out = 'intermediate_data\\videos\\predicted\\{}_s_run33.mp4'.format(video_path.split('\\')[-1][:-4])
print(video_path_out)

W = 1280
H = 720

cap = cv2.VideoCapture(video_path)
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, imgsz=1280, conf=0.5,)

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
