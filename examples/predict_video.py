# from obj_predictor import predictor
from obj_detector.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_detector.data import DataMaster
from pathlib import Path
import obj_detector as op


model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
input_video = Path("G:\\jacob\\practice_data_yolo\\short.mp4")
output_video = "short_predicted.mp4"

def main():
    # instatiate PredictorModel class with model path
    predictor = PredictorModel(model_path)

    # predict objects in input video,
    predictor.predict_video(input_vid=input_video, 
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