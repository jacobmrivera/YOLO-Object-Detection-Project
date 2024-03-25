import cv2
from ultralytics import YOLO
import os
from PIL import Image
from tqdm import tqdm
import torch
from ultralytics.models.yolo.detect import DetectionTrainer
from pathlib import Path
from . import constants

REMOVE_DUPLICATE_OBJ_PREDS = True

class PredictorModel:
    def __init__(self, model_path: str|Path) -> None:
        self.model = YOLO(model_path)


    def set_model(self, model: str|Path):
        self.model = YOLO(model)
        return


    def predict_image(self, img, output_dir= None, save_yolo_img=False, save_conf=False, normalize_annot=True):
        if not self.model:
            raise ValueError("Model not set.")
        
        results = self.model(img, conf=constants.DEFAULT_CONF_VAL, save_conf=True, verbose=False)

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

        predicted_bb = self.predictions_to_arr(results)

        text_name =  img.split("\\")[-1].split('.')[0] + ('_pred_c.txt' if save_conf else '_pred.txt')
        output_path = os.path.join(output_dir, text_name)

        self.predicts_to_txt(predicted_bb, output_path, width, height, save_yolo_img)

        return

    def predict_video(self, 
        input_vid, 
        output_vid_name=None,
        output_dir=None, 
        save_annot=False, 
        save_frames=False, 
        save_yolo_vid=True, 
        save_drawn_frames=False, 
        normalize_annot=True, 
        save_conf=True
        ):
        if not self.model:
            raise ValueError("Model not set.")

        cap = cv2.VideoCapture(str(input_vid))

        device = 0 if torch.cuda.is_available() else None

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        video_pre_path, video_name = os.path.split(input_vid)
        vid_prefix = video_name.split('.')[0]

        if output_dir == None:
            output_path = input_vid.parent
        else:
            output_path = output_dir
        os.makedirs(output_path, exist_ok=True)

        # create out opencv video obj
        if save_yolo_vid:
            if output_vid_name is None:
                output_vid = os.path.join(output_path, "predicted.mp4")
            else:
                output_vid = os.path.join(output_path, output_vid_name)

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

        # if save_annot and save_conf:
        #     text_conf_output = os.path.join(output_path, 'pred_labels_w_conf')
        #     os.makedirs(text_conf_output, exist_ok=True)

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
                results =  self.model(frame, device=device, conf=constants.DEFAULT_CONF_VAL, verbose=False)
                predicted_bb = self.predictions_to_arr(results)

                # generate text files if saving annotations
                if save_annot:
                    txt_path = os.path.join(texts_output, vid_prefix + f"_frame_{count}.txt")
                    self.predicts_to_txt(predicted_bb, txt_path, width, height, save_conf)

                # if save_conf:
                #     txt_path = os.path.join(text_conf_output, vid_prefix + f"_frame_c_{count}.txt")
                #     self.predicts_to_txt(predicted_bb, txt_path, width, height, save_conf)

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




    def predicts_to_txt(self, preds_dict, output_file, width, height, write_conf=False):
        # Write to the file
        with open(output_file, 'w') as file:
            for obj_num in preds_dict.keys():
                if write_conf:
                    file.write(f"{int(obj_num)} {round(preds_dict[obj_num][1][0]/width, 5)} {round(preds_dict[obj_num][1][1]/height, 5)} {round(preds_dict[obj_num][1][2]/width, 5)} {round(preds_dict[obj_num][1][3]/height, 5)} {round(preds_dict[obj_num][2], 5)}\n")
                else:
                    file.write(f"{int(obj_num)} {round(preds_dict[obj_num][1][0]/width, 5)} {round(preds_dict[obj_num][1][1]/height, 5)} {round(preds_dict[obj_num][1][2]/width, 5)} {round(preds_dict[obj_num][1][3]/height, 5)} \n")


    def predictions_to_arr(self, results):
        predicted_dict = {}
        boxes = results[0].boxes

        for i in range(len(boxes.cls)):
            # if the obj num is already a key in the dict and has a greater confidence score, replace 
            if boxes.cls[i].item() in predicted_dict.keys() and boxes.conf[i].item() >  predicted_dict[boxes.cls[i].item()][2]:
                predicted_dict[boxes.cls[i].item()] = [boxes.cls[i].item(), boxes.xywh[i].tolist(), boxes.conf[i].item()]
            # if the obj is not in the dictionary, just add it
            elif  boxes.cls[i].item() not in predicted_dict.keys():
                predicted_dict[boxes.cls[i].item()] = [boxes.cls[i].item(), boxes.xywh[i].tolist(), boxes.conf[i].item()]
            # no else

        return predicted_dict

    def predict_frames(self, img, output_dir= None, save_yolo_img=False, save_conf=False, normalize_annot=True):
        print()

        '''
        given a directory, provide annootations for eac frame in an output dir
        
        '''