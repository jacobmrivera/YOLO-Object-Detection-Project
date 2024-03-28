
from obj_detector.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from pathlib import Path
import os
import obj_detector.util as util

model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
frame_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\frames") # will be different
output_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict")

def main():
    predictor = PredictorModel(model_path)

    predictor.predict_image(img=frame_path, drawn_frame_output_path=output_path)



if __name__ == "__main__":
    main()