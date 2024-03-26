


# from obj_predictor import predictor
from obj_predictor.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_predictor.data import DataMaster
from pathlib import Path
import os
import obj_predictor.util as util

model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
frames_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\frames") # will be different
output_path = Path("C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict")

def main():
    predictor = PredictorModel(model_path)

    # instantiate datamaster class
    dataHandler = DataMaster(model_path)

    # set up the labels and output paths
    labels_path = output_path / "pred_labels"
    pred_frames_path = output_path /  "pred_frames"

    os.makedirs(labels_path, exist_ok=True)
    os.makedirs(pred_frames_path, exist_ok=True)


    predictor.predict_frames(frames_dir=frames_path,annot_output_path=labels_path, drawn_frame_output_path=pred_frames_path)

    # smooth the annotations
    dataHandler.smooth_annotations(input_dir=labels_path)
    
    # draw the annotations onto the frames
    # dataHandler.batch_draw_bb(images_dir=frames_path, labels_dir=labels_path, output_dir=pred_frames_path)
    # # stitch the frames into a video
    # util.frames_to_video(pred_frames_path, frames_path.parent.joinpath("stitched_video.mp4"), fps=30)




if __name__ == "__main__":
    main()