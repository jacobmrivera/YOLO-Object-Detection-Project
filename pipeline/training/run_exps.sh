 #! /bin/bash

source "yolo_project\\venv\\Scripts\\activate"


SCRIPT="yolo_project\\detection_trainer.py"

CONFIG_PATH="yolo_project\\config_inter_15.yaml"
# CONFIG_PATH_B="yolo_project\\config_b.yaml"

MODEL="yolov8s.pt"
EPOCHS=600


python $SCRIPT --config_path $CONFIG_PATH --model $MODEL --epochs $EPOCHS
# python $SCRIPT --config_path $CONFIG_PATH_B --model $MODEL --epochs $EPOCHS

# MODEL="yolov8m.pt"
# python $SCRIPT --config_path $CONFIG_PATH_A --model $MODEL --epochs $EPOCHS
# python $SCRIPT --config_path $CONFIG_PATH_B --model $MODEL --epochs $EPOCHS


deactivate
#  cd ..\\..\\..

echo "done..."