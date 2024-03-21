#!/bin/bash


DATASET_PATH="C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored"
YAML_PATH="data\\config_files\\config_all.yaml"
KSPLIT=10
WEIGHTS_PATH="yolov8s.pt"
EPOCHS=1000
BATCH_SIZE=16
DEVICE=0
PROJECT_NAME="k_fold_training_s_10_fold"

source venv\\Scripts\\activate

python scripts\\py_scripts\\training_scripts\\k_fold_train.py --dataset_path $DATASET_PATH --yaml_path $YAML_PATH --ksplit $KSPLIT --weights_path $WEIGHTS_PATH --epochs $EPOCHS --batch_size $BATCH_SIZE --device $DEVICE --project_name $PROJECT_NAME


deactivate