#!/usr/bin/env python

import argparse
import datetime
import shutil
from pathlib import Path
from collections import Counter

import yaml
import numpy as np
import pandas as pd
from ultralytics import YOLO
from sklearn.model_selection import KFold

import obj_predictor as op

'''
Created by Jacob Rivera
Adapted from https://docs.ultralytics.com/guides/kfold-cross-validation/

Spring 2024

Last edit: 03/18/2024

Description:

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
    parser.add_argument("--dataset_path", required=True, help="Path data to top lvl directory, containing labels dir and images dir")
    parser.add_argument("--yaml_path", required=True, help="Path data yaml used by YOLO. Defines obj nums and train/test path")
    parser.add_argument("--ksplit", required=False, default=5, type=int, help="number of folds for cross validating training")
    parser.add_argument("--weights_path", required=True, type=str, default="yolov8s.pt", help="model to train, default is s model")
    parser.add_argument("--epochs", required=False, type=int, default=1000, help="max number of epochs to train")
    parser.add_argument("--batch_size", required=False, type=int, default=16, help="max number of epochs to train")
    parser.add_argument("--device", required=True, help="int for GPU device")
    parser.add_argument("--project_name", required=True, help="String for project containing training sessions")

    args = parser.parse_args()

    dataset_path = args.dataset_path
    yaml_path = args.yaml_path
    ksplit = args.ksplit
    weights_path = args.weights_path
    epochs = args.epochs
    batch_size = args.batch_size
    device = args.device
    project_name = args.project_name

 
    op.training.k_fold_train.train(dataset_path, yaml_path, ksplit, weights_path, batch_size, epochs, project_name, device)

    return



if __name__ == "__main__":
    main()