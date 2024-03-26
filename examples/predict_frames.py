


# from obj_predictor import predictor
from obj_predictor.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_predictor.data import DataMaster
from pathlib import Path

import obj_predictor.util as util

model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
frames_path = Path("G:\\jacob\\practice_data_yolo\\short.mp4")

def main():
    predictor = PredictorModel(model_path)
    '''
    todo
    MAKE A FUNC THAT WILL TAKE A DIR OF FRAMES, AND RETURN ANNOTS

    THEN SMOOTH
    THEN DRAW
    THEN STITCH

    the full pipeline doesn't need the stitching, just te smoothed annotations
        but I need to test it by drawing and stitching 
    '''
    # predictor.predict_video(input_video, save_annot=True)

    dataHandler = DataMaster(model_path)

    labels_path = frames_path.parent / frames_path.name + "pred_labels"
    output_dir = frames_path.parent / frames_path.name + "pred_frames"

    dataHandler.smooth_annotations(input_dir=labels_path)
    dataHandler.batch_draw_bb( frames_path, labels_path, output_dir)

    util.frames_to_video(frames_path, output_video_path, fps=30):




if __name__ == "__main__":
    main()