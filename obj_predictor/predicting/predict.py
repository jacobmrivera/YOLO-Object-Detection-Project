import cv2
from ultralytics import YOLO
import os




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



# def write_annot_to_text():

# calls yolo on every frame, and saves predictions to txt file
# a frames and labels folder are made, so that a video can be made from them
def predict_every_frame(model_path, video_input, output_dir='', width=1280, height=720, confidence=0.5):

    model = YOLO(model_path)

    cap = cv2.VideoCapture(video_input)
    # out = cv2.VideoWriter(video_output, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

    prefix = video_input.split('\\')[-1].split('.')[0]

    frames_output = os.path.join(output_dir, 'frames')
    txts_output = os.path.join(output_dir, 'labels')

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(frames_output, exist_ok=True)
    os.makedirs(txts_output, exist_ok=True)

    count = 0

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, imgsz=width, conf=confidence,)

            predicted_bb = predictions_to_arr(results)
            # txt = "C:\\Users\\jacob\\Desktop\\practice\\preds.txt"

            txt_path = os.path.join(txts_output, prefix + f"_{count}")
            predicts_to_txt(predicted_bb, txt_path)

            # Save the frame as an image
            img_path = os.path.join(txts_output, prefix + f"_{count}")
            cv2.imwrite(img_path, frame)

            count += 1

        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    # out.release()
    cv2.destroyAllWindows()

    return



def predictions_to_arr(results):
    predicted_bb = []
    boxes = results[0].boxes 

    for i in range(len(boxes.cls)):
        # print(boxes.cls[i].item(), boxes.xywh[i].tolist())
        predicted_bb.append([boxes.cls[i].item(), boxes.xywh[i].tolist()])

    return predicted_bb

def predicts_to_txt(preds, output_file):
    # Write to the file
    with open(output_file, 'w') as file:
        for pred in preds:
            file.write(f"{int(pred[0])} {round(pred[1][0], 5)} {round(pred[1][1], 5)} {round(pred[1][2], 5)} {round(pred[1][3], 5)}\n")



# def predict_frame(frame, model, img_size, confidence):
#     # frame = "C:\\Users\\jacob\\Desktop\\practice\\apples.jpg"

#     # model = YOLO("yolov8s.pt")
#     # results = model(frame)
#     results = model(frame, imgsz=img_size, conf=confidence,)
#     # print(results.boxes)

#     predicted_bb = []

#     # for result in results:
#     boxes = results[0].boxes 

#     for i in range(len(boxes.cls)):

#         # print(boxes.cls[i].item(), boxes.xywh[i].tolist())
#         predicted_bb.append([boxes.cls[i].item(), boxes.xywh[i].tolist()])
            
#     txt_name = frame.split('\\')[-1].split('.')[0]
#     # print(txt_name)
#     txt = "C:\\Users\\jacob\\Desktop\\practice\\preds.txt"
#     predicts_to_txt(predicted_bb, txt)




# predict_frame("tet")