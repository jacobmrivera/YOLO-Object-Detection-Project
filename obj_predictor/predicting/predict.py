import cv2
from ultralytics import YOLO
import os
from PIL import Image
from tqdm import tqdm


WINDOWS = False

def predict_video_yolo_drawn(model_path, video_input, video_output='', confidence=0.5):

    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_input)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(video_output, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame, conf=confidence,)

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
def predict_vid_save_annot(model_path, video_input, output_dir, confidence=0.5, save_frames=False):

    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_input)

    if WINDOWS:
        prefix = video_input.split('\\')[-1].split('.')[0]
    else:
        prefix = video_input.split('/')[-1].split('.')[0]

    # if output_dir is None: output_dir = os.path.dirname(video_input)
    texts_output = os.path.join(output_dir, 'pred_labels')

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(texts_output, exist_ok=True)

    if save_frames:
        frames_output = os.path.join(output_dir, 'frames')
        os.makedirs(frames_output, exist_ok=True)

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
            results = model(frame, conf=confidence,verbose=False)

            predicted_bb = predictions_to_arr(results)
            # txt = "C:\\Users\\jacob\\Desktop\\practice\\preds.txt"

            txt_path = os.path.join(texts_output, prefix + f"_{count}")
            predicts_to_txt(predicted_bb, txt_path)

            if save_frames:
                # Save the frame as an image
                img_path = os.path.join(frames_output, prefix + f"_{count}.jpg")
                cv2.imwrite(img_path, frame)

            count += 1
            progress_bar.update(1)  # Update progress bar
        else:
            # Break the loop if the end of the video is reached
            break

    # Close tqdm progress bar
    progress_bar.close()

    # Release the video capture object and close the display window
    cap.release()
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



def predict_image_save_annot(img, model, confidence= 0.5, yolo_draw=False):

    model = YOLO(model)

    results = model(img, conf=confidence)

     # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Save the frame as an image
    if yolo_draw:
        out_img = img.split('.')[0] + "_pred.jpg"
        cv2.imwrite(out_img, annotated_frame)

    predicted_bb = []

    # for result in results:
    boxes = results[0].boxes

    for i in range(len(boxes.cls)):
        predicted_bb.append([boxes.cls[i].item(), boxes.xywh[i].tolist()])

    text_name =  img.split('.')[0] + '_pred.txt'
    predicts_to_txt(predicted_bb, text_name)


# predict_frame("tet")
# predict_image_save_annot("practice_data/apples.jpeg", model='yolov8s.pt', yolo_draw=True)