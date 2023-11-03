 #! /bin/bash


VIRTUAL_ENV_PATH=""


SCRIPT="yolo_project\\detection_trainer.py"
CONFIG_PATH="yolo_project\\config_inter_15.yaml"
MODEL="yolov8s.pt"
EPOCHS=600

source $VIRTUAL_ENV_PATH

python $SCRIPT --config_path $CONFIG_PATH --model $MODEL --epochs $EPOCHS

deactivate
echo "done..."