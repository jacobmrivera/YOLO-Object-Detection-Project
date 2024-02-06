#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="Mirrored_Images_Training\\all_image_variants\\weights\\best.pt"
video_input=""C:\\Users\\multimaster\\Desktop\\YOLO-DATASETS\\videos\\exp351_sub2_child\\short.mp4""
annot_output="practice_data"
confidence=0.5  # Default is 50, 0 == really blurry, 200 == really sharp
save_frames=False


source venv\\Scripts\\activate

# Run the Python script
python scripts/py_scripts/predicting_scripts/predict_video_save_annot.py --model_path "$model_path" --video_input "$video_input" --annot_output "$annot_output" --confidence "$confidence" --save_frames "$save_frames"

deactivate