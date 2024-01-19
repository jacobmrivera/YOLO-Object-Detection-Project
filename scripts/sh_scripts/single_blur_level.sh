#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Jan 19 2024


# Define the paths
input_img="/Users/jacobrivera/Desktop/blur_practice/blurry.jpg"

source venv/bin/activate

# Run the Python script
python scripts/py_scripts/blur_scripts/single_img_blur_level.py --input_img "$input_img"

deactivate