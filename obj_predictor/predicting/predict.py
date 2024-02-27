import cv2
from ultralytics import YOLO
import os
from PIL import Image
from tqdm import tqdm
import torch



def predictions_to_arr(results):
    predicted_bb = []
    boxes = results[0].boxes

    for i in range(len(boxes.cls)):
        # print(boxes.cls[i].item(), boxes.xywh[i].tolist())
        predicted_bb.append([boxes.cls[i].item(), boxes.xywh[i].tolist(), boxes.conf[i].item()])

    return predicted_bb



def predicts_to_txt(preds, output_file, width, height, write_conf=False):
    # Write to the file
    with open(output_file, 'w') as file:
        for pred in preds:
            if write_conf:
                file.write(f"{int(pred[0])} {round(pred[1][0]/width, 5)} {round(pred[1][1]/height, 5)} {round(pred[1][2]/width, 5)} {round(pred[1][3]/height, 5)} {round(pred[2], 5)}\n")
            else:
                file.write(f"{int(pred[0])} {round(pred[1][0]/width, 5)} {round(pred[1][1]/height, 5)} {round(pred[1][2]/width, 5)} {round(pred[1][3]/height, 5)} \n")



def predict_image_save_annot(img, model, output_dir= ".", confidence= 0.5, save_yolo_img=False, save_conf=False, normalize_annot=True):

    model = YOLO(model)
    results = model(img, conf=confidence, save_conf=True, verbose=False)

    img_PIL = Image.open(img)

    # Get image width and height
    width, height = img_PIL.size

    # set denominator for normalization
    if not normalize_annot:
        width = 1
        height = 1

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Save the frame as an image
    if save_yolo_img:
        out_img = img.split('.')[0] + "_pred.jpg"
        cv2.imwrite(out_img, annotated_frame)

    predicted_bb = predictions_to_arr(results)
    print(f"output path pre: {output_dir}")

    text_name =  img.split("/")[-1].split('.')[0] + ('_pred_c.txt' if save_conf else '_pred.txt')

    print(f"test_name: {text_name}")

    output_path = os.path.join(output_dir, text_name)

    print(f"output path: {output_path}")
    input()
    predicts_to_txt(predicted_bb, output_path, width, height, save_yolo_img)




def predict_video(model_path, input_vid, output_dir, conf=0.5, save_annot=False, save_frames=False, save_yolo_vid=True, save_drawn_frames=False, normalize_annot=True, save_conf=False):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(input_vid)

    device = 0 if torch.cuda.is_available() else None

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    video_pre_path, video_name = os.path.split(input_vid)
    vid_prefix = video_name.split('.')[0]

    output_path =  os.path.join(output_dir, vid_prefix+"_predicted_data")
    os.makedirs(output_path, exist_ok=True)

    # create out opencv video obj
    if save_yolo_vid:
        output_vid = os.path.join(output_path, "predicted.mp4")
        out = cv2.VideoWriter(output_vid, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

    # create dir for frames
    if save_frames:
        frames_output = os.path.join(output_path, 'frames')
        os.makedirs(frames_output, exist_ok=True)

    # create dir for annotations
    if save_annot:
        texts_output = os.path.join(output_path, 'pred_labels')
        os.makedirs(texts_output, exist_ok=True)

    # create dir for yolo drawn frames
    if save_drawn_frames:
        drawn_frames_output = os.path.join(output_path, 'drawn_frames')
        os.makedirs(drawn_frames_output, exist_ok=True)

    if save_conf:
        text_conf_output = os.path.join(output_path, 'pred_labels_w_conf')
        os.makedirs(text_conf_output, exist_ok=True)

    # set denominator for normalization
    if not normalize_annot:
        width = 1
        height = 1

    count = 0

    print("Predicting...")
    # Initialize tqdm progress bar
    progress_bar = tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:

            results =  model(frame, device=device, conf=conf, verbose=False)
            predicted_bb = predictions_to_arr(results)

            # generate text files if saving annotations
            if save_annot:
                txt_path = os.path.join(texts_output, vid_prefix + f"_frame_{count}.txt")
                predicts_to_txt(predicted_bb, txt_path, width, height, False)

            if save_conf:
                txt_path = os.path.join(text_conf_output, vid_prefix + f"_frame_c_{count}.txt")
                predicts_to_txt(predicted_bb, txt_path, width, height, save_conf)

            # save frame if supposed to
            if save_frames:
                # Save the frame as an image
                img_path = os.path.join(frames_output, vid_prefix + f"_frame_{count}.jpg")
                cv2.imwrite(img_path, frame)

            # add frame to out video if saving yolo vid
            if save_yolo_vid:
                # Visualize the results on the frame
                annotated_frame = results[0].plot()
                # write frame to videoWriter
                out.write(annotated_frame)

            # save individual yolo predicted frame
            if save_drawn_frames:
                # get image path and image name
                img_path = os.path.join(drawn_frames_output, vid_prefix + f"_drawn_frame_{count}.jpg")

                # Visualize the results on the frame
                annotated_frame = results[0].plot()
                cv2.imwrite(img_path, annotated_frame)

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