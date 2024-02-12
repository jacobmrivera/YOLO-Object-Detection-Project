#!/bin/bash


### Single image blur level detection
### Created by Jacob Rivera, Feb 2, 2024


# Define the paths
images_dir="practice_data\\second_batch_supp\\images"
labels_dir="practice_data\\second_batch_supp\\labels"
output_dir="practice_data\\second_batch_supp\\drawn"


source venv\\Scripts\\activate

# Run the Python script
python scripts\\py_scripts\\drawing_scripts\\batch_draw_bb.py --images_dir "$images_dir" --labels_dir "$labels_dir" --output_dir "$output_dir"

deactivate


