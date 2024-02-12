import cv2
from ultralytics import YOLO
import os
from PIL import Image
from tqdm import tqdm



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



def predict_image_save_annot(img, model, confidence= 0.5, save_yolo_img=False):

    model = YOLO(model)
    results = model(img, conf=confidence)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Save the frame as an image
    if save_yolo_img:
        out_img = img.split('.')[0] + "_pred.jpg"
        cv2.imwrite(out_img, annotated_frame)

    predicted_bb = []

    # for result in results:
    boxes = results[0].boxes

    for i in range(len(boxes.cls)):
        predicted_bb.append([boxes.cls[i].item(), boxes.xywh[i].tolist()])

    text_name =  img.split('.')[0] + '_pred.txt'
    predicts_to_txt(predicted_bb, text_name)


def predict_video(model_path, input_vid, conf=0.5, save_annot=False, save_frames=False, save_yolo_vid=True):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(input_vid)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    video_pre_path, video_name = os.path.split(input_vid)
    vid_prefix = video_name.split('.')[0]

    output_path =  os.path.join(video_pre_path, vid_prefix+"_predicted_data")
    os.makedirs(output_path, exist_ok=True)

    if save_yolo_vid:
        output_vid = os.path.join(output_path, "predicted.mp4")
        out = cv2.VideoWriter(output_vid, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

    if save_frames:
        frames_output = os.path.join(output_path, 'frames')
        os.makedirs(frames_output, exist_ok=True)

    if save_annot:
        texts_output = os.path.join(output_path, 'pred_labels')
        os.makedirs(texts_output, exist_ok=True)

    count = 0

    print("Predicting...")
    # Initialize tqdm progress bar
    progress_bar = tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, conf=conf,verbose=False)

            if save_annot:
                predicted_bb = predictions_to_arr(results)
                txt_path = os.path.join(texts_output, vid_prefix + f"_{count}.txt")
                predicts_to_txt(predicted_bb, txt_path)

            if save_frames:
                # Save the frame as an image
                img_path = os.path.join(frames_output, vid_prefix + f"_{count}.jpg")
                cv2.imwrite(img_path, frame)

            if save_yolo_vid:
                results = model(frame, conf=conf, verbose=False)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # write frame to videoWriter
                out.write(annotated_frame)

            count += 1
            progress_bar.update(1)  # Update progress bar
        else:
            # Break the loop if the end of the video is reached
            break

    # Close tqdm progress bar
    progress_bar.close()

    # Release the video capture object and close the display window
    cap.release()
    if save_yolo_vid: out.release()
    cv2.destroyAllWindows()

    return
