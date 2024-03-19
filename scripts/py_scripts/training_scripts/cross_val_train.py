#!/usr/bin/env python

import json
import argparse
import os
import sys
sys.path.append('..obj_predictor')

from sklearn.model_selection import KFold

import obj_predictor as op
# import obj_predictor.data_processing.train_test_split_frames as tts

# from obj_predictor.training import train
# import obj_predictor.training.train as trainer
# import obj_predictor.data_processing.make_config as make_config
# import obj_predictor.data_processing.train_test_split_frames as tts

'''
Created by Jacob Rivera
Spring 2024

Last edit: 03/08/2024

Description:
    Train YOLO model from passed aruements

    TODO: Make it so that the yaml is made automatically, and checks for train/test split and does it if it isn't
'''

obj_dict = {
    0: "kettle",
    1: "cat",
    2: "potato",
    3: "firetruck",
    4: "bulldozer",
    5: "car",
    6: "ostrich",
    7: "frog",
    8: "truck",
    9: "lobster",
    10: "carrot",
    11: "colander",
    12: "motorcycle",
    13: "cup",
    14: "dog",
    15: "elephant",
    16: "spaceship",
    17: "pineapple",
    18: "banana",
    19: "submarine",
    20: "boat",
    21: "cookie",
    22: "stingray",
    23: "fork",
    24: "helicopter",
    25: "duck",
    26: "bee"
}



def main():
    parser = argparse.ArgumentParser(description="Train YOLO model from passed arguements")
    # parser.add_argument("--data_dir", required=True, help="Path data to be used for training")
    # parser.add_argument("--model", required=False, default="yolov8s.pt", help="model to train with")
    # parser.add_argument("--epochs", required=False, type=int, default=1000, help="max number of epochs to train")
    # parser.add_argument("--device", required=True, help="int for GPU device")
    # parser.add_argument("--yaml_path", required=True, help="Path data yaml used by YOLO. Defines obj nums and train/test path")
    # parser.add_argument("--project_name", required=True, help="String for project containing training sessions")
    # parser.add_argument("--run_name", required=True, help="String for current training session")

    # args = parser.parse_args()

    # model = args.model
    # epochs = args.epochs
    # device = args.device
    # yaml_path = args.yaml_path
    # project_name = args.project_name
    # run_name = args.run_name


    model = "yolov8s.pt"
    epochs = 3000
    device = 0
    project_name = "All_Data_Trainings"
    run_name = "all_data_2_14_mirrored_v8m"
    data_src = "C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored"

    k = 5
    split = 0.8
    seed = 42
    obj_num = 27


    yaml_out_name = "config_all.yaml"
    dataset_path = data_src # os.path.join(data_src, str(5))

    op.data_processing.split.split_data_pipe(dataset_path, dataset_path, split, seed)
    op.data_processing.util.make_config(yaml_out_name, dataset_path, obj_num, obj_dict)
    model = "yolov8m.pt" #os.path.join(project_name, run_name+"all", "weights", "best.pt") 
    op.training.train_model(model, device, yaml_out_name, project_name, run_name, epochs)

    
    # op.data_processing.split.kfold_data(data_src, data_src, k, seed)

    # for i in range (1, k+1):
    #     yaml_out_name = f"config_{i}.yaml"
    #     dataset_path = os.path.join(data_src, str(i))
    #     op.data_processing.util.make_config(yaml_out_name, dataset_path, obj_num, obj_dict)

    #     # get previous best model or standard s model to start
    #     model = os.path.join(project_name, run_name+str(i-1), "weights", "best.pt") if i > 1 else "yolov8s.pt"
    #     op.training.train_model(model, device, yaml_out_name, project_name, run_name+str(i), epochs)

    #     # Check if the file exists before attempting to delete it
    #     if os.path.exists(yaml_out_name):
    #         os.remove(yaml_out_name)
    #         print(f"{yaml_out_name} deleted successfully.")
    #     else:
    #         print(f"Could not delete {yaml_out_name}.")
    return



if __name__ == "__main__":
    main()