


# from obj_predictor import predictor
from obj_detector.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_detector.data import DataMaster
from pathlib import Path
import os
import obj_detector.util as util

model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
output_path = Path("Z:\\Jacob\\YOLO_Predicted")

TOP_EXP_DIR = Path("M:/experiment_351/included")


def main():

    subject_directories = list(TOP_EXP_DIR.glob("__*"))

    predictor = PredictorModel(model_path)

    # instantiate datamaster class
    dataHandler = DataMaster(model_path)

    for sub in subject_directories:

        # cam 7
        frames_path = sub / "cam07_frames_p" 
        sub_output = output_path / Path(sub.name + "_cam07_frames_predicted_data")

        # set up the labels and output paths
        labels_path = sub_output / "predicted_labels"
        os.makedirs(labels_path, exist_ok=True)
        print(f"Processing: {frames_path} ...")
        # Predict frames 
        predictor.predict_frames(frames_dir = frames_path,
                                 annot_output_path = labels_path)

        # smooth the annotations
        dataHandler.smooth_annotations(input_dir=labels_path)


        # cam 8
        # frames_path = sub / "cam08_frames_p" 
        # print(f"Processing: {frames_path} ...")

        # sub_output = output_path / Path(sub.name + "_cam08_frames_predicted_data")

        # # set up the labels and output paths
        # labels_path = sub_output / "predicted_labels"
        # os.makedirs(labels_path, exist_ok=True)

        # # Predict frames 
        # predictor.predict_frames(frames_dir = frames_path,
        #                          annot_output_path = labels_path)
        # # smooth the annotations
        # dataHandler.smooth_annotations(input_dir=labels_path)


if __name__ == "__main__":
    main()