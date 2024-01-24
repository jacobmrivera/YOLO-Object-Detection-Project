#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
input_dir="/Users/jacobrivera/Library/CloudStorage/Box-Box/frames"
output_dir="/Users/jacobrivera/Library/CloudStorage/Box-Box/frames"
threshold=100  # Default is 50, 0 == really blurry, 200 == really sharp


source venv/bin/activate

# Run the Python script
python scripts/py_scripts/blur_scripts/detect_blur_levels_dir.py --input_dir "$input_dir" --output_dir "$output_dir" --threshold "$threshold"

deactivate


