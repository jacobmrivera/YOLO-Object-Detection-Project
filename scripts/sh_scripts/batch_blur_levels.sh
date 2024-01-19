#!/bin/bash

# Define the paths
input_dir="/Users/jacobrivera/Desktop/blur_practice"
output_dir="/Users/jacobrivera/Desktop/blur_practice"
threshold=50  # Default is 50, 0 == really blurry, 200 == really sharp



# Run the Python script
python scripts/py_scripts/blur_scripts/detect_blur_levels_dir.py --input_dir "$input_dir" --output_dir "$output_dir" --threshold "$threshold"
