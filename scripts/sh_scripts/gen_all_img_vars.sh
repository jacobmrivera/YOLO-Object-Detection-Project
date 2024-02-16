#!/bin/bash



# parser.add_argument("--images_dir", required=True, help="directory containing all images")
# parser.add_argument("--labels_dir", required=True, help="directory containing all labels")
# parser.add_argument("--output_dir", required=False, help="top level directory to place output image and label dirs")
# parser.add_argument("--add_directly", type=bool, required=False, default=False, help="Flag if image variations should be placed in input directory, could create something messy")
    
INPUT_DIR="C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored\\images"
LABELS_DIR="C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored\\labels"
OUTPUT_DIR=''


source venv\\Scripts\\activate

python scripts\\py_scripts\\gen_image_vars\\gen_all_mirrors.py --images_dir "$INPUT_DIR" --labels_dir "$LABELS_DIR"

deactivate