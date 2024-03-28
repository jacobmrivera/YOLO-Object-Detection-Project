from obj_detector.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from pathlib import Path

'''
Created by Jacob Rivera
Spring 2024

Last edit: 03/28/2024

Description:
    Predict objects in input video

    There are many flags that can be passed into the predict_video() func,
    all of them besides the input_video have defaults.

    Set the flags to achieve the desired output.

    
    model_path:
        path to .pt file to predict with

    input_video:
        path to video to predict objects in

    output_video:
        if saving the yolo drawn video (yolo puts the bounding boxes for us)
        then provide a name for the output video, otherwise the output name
            will be based off the input video name

'''

model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
input_video = Path("G:\\jacob\\practice_data_yolo\\short.mp4")
output_video = "short_predicted.mp4"

def main():
    # instatiate PredictorModel class with model path
    predictor = PredictorModel(model_path)

    # predict objects in input video,
    predictor.predict_video(
        input_vid=input_video, 
        output_vid_name=None,
        output_dir=output_video, 
        save_annot=False, 
        save_frames=False, 
        save_yolo_vid=True, 
        save_drawn_frames=False, 
        normalize_annot=True, 
        save_conf=True
    )

    

if __name__ == "__main__":
    main()