#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="All_Data_Trainings\\all_data_2_14_mirrored_80_20_split\\weights\\best.pt"
video_input="C:\\Users\\multimaster\\Desktop\\dynamic_vids_to_predict\\20230209_10057_cam07.mp4"
confidence=0.7  # Default is 50, 0 == really blurry, 200 == really sharp
output_dir="Z:\\Jacob\\YOLO_Predicted"

save_frames=0
save_annot=0
save_yolo_vid=0
save_drawn_frames=0
normalize_annot=1
save_conf=1



source venv\\Scripts\\activate

# Directory to search in
directory="M:/experiment_351/included"

# Use find command to list directories starting with "__" within the specified directory
directories=$(find "$directory" -mindepth 1 -maxdepth 1 -type d -name "__*")

# Iterate through the list of directories
for dir in $directories; do
    dirname=$(basename "$dir")
    video_input="$directory\\$dirname\\cam07_frames_r\\${dirname#__}_cam07.mp4"
    echo $video_input
    python scripts\\py_scripts\\predicting_scripts\\predict_video.py --model_path "$model_path" --video_input "$video_input" --output_dir "$output_dir" --confidence "$confidence" --save_frames "$save_frames" --save_annot "$save_annot" --save_yolo_vid "$save_yolo_vid" --save_drawn_frames "$save_drawn_frames" --normalize_annot "$normalize_annot" --save_conf "$save_conf"
    
    video_input="$directory\\$dirname\\cam08_video_r\\${dirname#__}_cam08.mp4"
    echo $video_input
    python scripts\\py_scripts\\predicting_scripts\\predict_video.py --model_path "$model_path" --video_input "$video_input" --output_dir "$output_dir" --confidence "$confidence" --save_frames "$save_frames" --save_annot "$save_annot" --save_yolo_vid "$save_yolo_vid" --save_drawn_frames "$save_drawn_frames" --normalize_annot "$normalize_annot" --save_conf "$save_conf"

done

# # Run the Python script

deactivate