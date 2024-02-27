#!/bin/bash

### Created by Jacob Rivera, Feb 27, 2024
# Define the parent directory
parent_dir="Z:\Jacob\YOLO_Predicted"

# Find all directories containing "pred_labels_w_conf" and remove them
find "$parent_dir" -type d -name "pred_labels_w_conf" -exec rm -r {} +

