#!/usr/bin/env python

import json
import argparse

import sys
sys.path.append('..obj_predictor')


import obj_predictor as op
# import obj_predictor.data_processing.train_test_split_frames as tts

# from obj_predictor.training import train
# import obj_predictor.training.train as trainer
# import obj_predictor.data_processing.make_config as make_config
# import obj_predictor.data_processing.train_test_split_frames as tts

'''
Created by Jacob Rivera
Spring 2024

Last edit: 02/02/2024

Description:
    Train YOLO model from passed aruements

    TODO: Make it so that the yaml is made automatically, and checks for train/test split and does it if it isn't
'''





def main():
    parser = argparse.ArgumentParser(description="Train YOLO model from passed arguements")
    # parser.add_argument("--data_dir", required=True, help="Path data to be used for training")
    parser.add_argument("--model", required=False, default="yolov8s.pt", help="model to train with")
    parser.add_argument("--epochs", required=False, type=int, default=1000, help="max number of epochs to train")
    parser.add_argument("--device", required=True, help="int for GPU device")
    parser.add_argument("--yaml_path", required=True, help="Path data yaml used by YOLO. Defines obj nums and train/test path")
    parser.add_argument("--project_name", required=True, help="String for project containing training sessions")
    parser.add_argument("--run_name", required=True, help="String for current training session")
    
    args = parser.parse_args()

    model = args.model
    epochs = args.epochs
    device = args.device
    yaml_path = args.yaml_path
    project_name = args.project_name
    run_name = args.run_name

    
    op.training.train_model(model, device, yaml_path, project_name, run_name, epochs)

    return



if __name__ == "__main__":
    main()