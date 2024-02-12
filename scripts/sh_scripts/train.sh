#!/bin/bash

### Created by Jacob Rivera, Feb 2, 2024

# Define the paths
MODEL="yolov8s.pt"
EPOCHS=1000
DEVICE=0
YAML_PATH="data\\config_files\\s_mirrored_vars.yaml"
PROJECT_NAME="Mirrored_Images_Training"
RUN_NAME="all_image_variants"

source venv\\Scripts\\activate

# Run the Python script
python scripts\\py_scripts\\training_scripts\\train_model.py --model $MODEL --epochs $EPOCHS --device $DEVICE --yaml_path $YAML_PATH --project_name $PROJECT_NAME --run_name $RUN_NAME

deactivate

