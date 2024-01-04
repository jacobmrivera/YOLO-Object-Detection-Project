import cv2
import os
from ultralytics import YOLO
import json
# import constants
# import runner

# W = 1280
# H = 720
# CONFIDENCE = 0.5

def predict_vid_from_json(json_config):

    # Load the YOLOv8 model
    model_path = json_config["predict"]["model_path"]
    # model_path = "C:\\Users\\multimaster\\Desktop\\YOLO-github-11_6_23\\1000_frames_obj_3_4_data_added\\run2\\weights\\best.pt"
    model = YOLO(model_path)

    # model size letter for name of output video
    model_letter = json_config["training"]["model"][-4]
    # model_letter = 's'
    # path to original video
    video_path = json_config["predict"]["video_path"]
#  video_path = "C:\\Users\\multimaster\\Desktop\\YOLO-github-11_6_23\\data\\videos\\orig\\exp351_sub2_parent.mp4"
    # path and name of output file -- currently uses old name and appends run info
    video_path_out = json_config["predict"]["video_path_name_out"]
    # video_path_out = "C:\\Users\\multimaster\\Desktop\\YOLO-github-11_6_23\\data\\videos\\predicted\\{}_{}_supp_1_run2.mp4" #runner.json_config["predict"]["video_path_name_out"]

    # video_path_out = video_path_out.format(video_path.split('\\')[-1][:-4],model_letter)

    width = json_config["constants"]["W"]
    height = json_config["constants"]["H"]
    confidence = json_config["constants"]["CONFIDENCE"]


    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))


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


def predict_video(model_path, video_input, video_output='', width=1280, height=720, confidence=0.5):

    model = YOLO(model_path)

    cap = cv2.VideoCapture(video_input)
    out = cv2.VideoWriter(video_output, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

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