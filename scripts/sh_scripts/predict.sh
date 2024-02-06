#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
model_path="Mirrored_Images_Training\\all_image_variants\\weights\\best.pt"
video_input="G:\\jacob\\practice_data_yolo\\short.mp4"
confidence=0.5  # Default is 50, 0 == really blurry, 200 == really sharp

save_frames=True
save_annot=True
save_yolo_vid=True


source venv\\Scripts\\activate

# Run the Python script
python scripts\\py_scripts\\predicting_scripts\\predict_video.py --model_path "$model_path" --video_input "$video_input" --confidence "$confidence" --save_frames "$save_frames" --save_annot "$save_annot" --save_yolo_vid "$save_yolo_vid"

deactivate