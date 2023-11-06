import cv2
import os
from ultralytics import YOLO
import constants
import runner

# W = 1280
# H = 720
# CONFIDENCE = 0.5

def predict_vid():

    # Load the YOLOv8 model
    model_path = runner.json_config["predict"]["model_path"]
    model = YOLO(model_path)

    # model size letter for name of output video
    model_letter = runner.json_config["training"]["model"][-4]

    # path to original video
    video_path = runner.json_config["predict"]["video_path"]

    # path and name of output file -- currently uses old name and appends run info
    video_path_out = runner.json_config["predict"]["video_path_name_out"]
    video_path_out = video_path_out.format(video_path.split('\\')[-1][:-4],model_letter)

    width = runner.json_config["constants"]["W"]
    height = runner.json_config["constants"]["H"]
    confidence = runner.json_config["constants"]["CONFIDENCE"]


    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))


    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, imgsz=width, conf=confidence,)

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

    return
