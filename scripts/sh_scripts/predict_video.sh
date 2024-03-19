#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="All_Data_Trainings\\all_data_2_14_mirrored_v8n_\\weights\\best.pt"
video_input="C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\20230209_10057_cam07.mp4"
confidence=0.8  # Default is 50, 0 == really blurry, 200 == really sharp
save_frames=0
save_annot=0
normalize_annot=1
save_yolo_vid=1
save_drawn_frames=0
save_conf=1

output_dir="C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\model_n"

source venv\\Scripts\\activate

# Run the Python script
python scripts\\py_scripts\\predicting_scripts\\predict_video.py --model_path "$model_path" --video_input "$video_input" --output_dir "$output_dir" --confidence "$confidence" --save_frames "$save_frames" --save_annot "$save_annot" --save_yolo_vid "$save_yolo_vid" --save_drawn_frames "$save_drawn_frames" --normalize_annot "$normalize_annot" --save_conf "$save_conf"

deactivate