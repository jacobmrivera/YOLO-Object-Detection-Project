#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="All_Data_Trainings\\all_data_2_14_mirrored_80_20_split\\weights\\best.pt"
image_input="practice_data\\20230209_10057_cam07_frame_2887.jpg"
confidence=0.5  # Default is 50, 0 == really blurry, 200 == really sharp
save_yolo_img=1
save_conf=1

source venv\\Scripts\\activate

# Run the Python script
python scripts\\py_scripts\\predicting_scripts\\predict_single_image.py --model_path "$model_path" --image_input "$image_input" --confidence "$confidence" --save_yolo_img "$save_yolo_img" --save_conf "$save_conf"

deactivate