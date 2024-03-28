


from obj_detector.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_detector.data import DataMaster
from pathlib import Path
import os
import obj_detector.util as util

'''
Created by Jacob Rivera
Spring 2024

Last edit: 03/28/2024

Description:
    Predict objects in a directory of images (or frames from a video)
        and stitches them into a video

    There are many flags that can be passed into the predict_frames() func,
    all of them besides the img have defaults.

    Set the flags to achieve the desired output.

    model_path:
        path to .pt file to predict with

    frames_path:
        path to directory containing all images/frames to predict objects in

    drawn_frame_output_dir:
        if saving the yolo drawn image (yolo puts the bounding boxes for us)
        then provide a path to a directory for the output image, otherwise the output name
            will be saved in the same location of the input img

    annot_output_dir:
        output directory to place annotation text file containing prediction bounding box info
        if no directory is provided, then the .txt file will be placed in the same dir
            as the input imgage

    ~~~ TO RUN ~~~
    in a terminal or command prompt, run the following commands from the top level of this project

    ! MAC/LINUX
    $ source venv/bin/activate

    ! WINDOWS   
    $ source venv\\Scripts\\activate

    python examples/predict_frames.py

    deactivate
    ~~~~~~~~~~~~~~
'''
model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
frames_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\frames") # will be different
output_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict")

smooth_annotations = True
output_video_name = "stitched.mp4"


def main():
    predictor = PredictorModel(model_path)

    # instantiate datamaster class
    dataHandler = DataMaster(model_path)

    # set up the labels and output paths
    labels_path = output_path / "pred_labels"
    pred_frames_path = output_path /  "pred_frames"

    os.makedirs(labels_path, exist_ok=True)
    os.makedirs(pred_frames_path, exist_ok=True)


    predictor.predict_frames(frames_dir=frames_path, annot_output_path=labels_path, drawn_frame_output_path=pred_frames_path)

    # smooth the annotations
    dataHandler.smooth_annotations(input_dir=labels_path)
    
    # draw the annotations onto the frames
    if smooth_annotations:
        dataHandler.batch_draw_bb(images_dir=frames_path, labels_dir=labels_path, output_dir=pred_frames_path)
    
    # stitch the frames into a video
    util.frames_to_video(pred_frames_path, frames_path.parent.joinpath(output_video_name), fps=30)




if __name__ == "__main__":
    main()