#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="data\\trained_models\\2_14_mirroed_data_80_20.pt"

confidence=0.7  # Default is 50, 0 == really blurry, 200 == really sharp
output_path="Z:\\Jacob\\YOLO_Predicted"

save_yolo_img=0
normalize_annot=1
save_conf=1

# /Volumes/multiwork/experiment_351/included/__20221112_10041/cam07_frames_p/img_1.jpg

source venv\\Scripts\\activate
# source venv/bin/activate

# Directory to search in
directory="M:\\experiment_351\\included"
# directory="/Volumes/multiwork/experiment_351/included"

# Use find command to list directories starting with "__" within the specified directory
directories=$(find "$directory" -mindepth 1 -maxdepth 1 -type d -name "__*")

# Iterate through the list of directories
for dir in $directories; do
    dirname=$(basename "$dir")

    input_dir="$directory\\$dirname\\cam07_frames_p"
    video_output_dir="$output_path\\${dirname#__}_cam07_predicted_data\\stitched_frames.mp4"

    python scripts\\py_scripts\\misc\\frames_to_video.py --input_dir "$input_dir" --output_dir "$output_dir"

    output_dir="$output_path\\${dirname#__}_cam07_predicted_data\\pred_labels_w_conf"




    # python scripts\\py_scripts\\predicting_scripts\\predict_batch_images.py --model_path "$model_path" --input_dir "$input_dir" --output_dir "$output_dir" --confidence "$confidence" --save_yolo_img "$save_yolo_img" --normalize_annot "$normalize_annot" --save_conf "$save_conf"

    # input_dir="$directory\\$dirname\\cam08_frames_p"
    # output_dir="$output_path\\${dirname#__}_cam08_predicted_data\\pred_labels_w_conf"
    # python scripts\\py_scripts\\predicting_scripts\\predict_batch_images.py --model_path "$model_path" --input_dir "$input_dir" --output_dir "$output_dir" --confidence "$confidence" --save_yolo_img "$save_yolo_img" --normalize_annot "$normalize_annot" --save_conf "$save_conf"


done


# # Run the Python script

deactivate