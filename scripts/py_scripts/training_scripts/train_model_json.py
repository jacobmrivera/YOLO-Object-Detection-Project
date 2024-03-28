#!/usr/bin/env python

import json
import argparse

import sys
sys.path.append('..obj_predictor')


import obj_detector as op
# import obj_predictor.data_processing.train_test_split_frames as tts

# from obj_predictor.training import train
# import obj_predictor.training.train as trainer
# import obj_predictor.data_processing.make_config as make_config
# import obj_predictor.data_processing.train_test_split_frames as tts

'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/03/2024

Description:
    Train YOLO model from json config file details. To run, ensure that the json
    file passed in has all important fields filled out.

    TODO: make a list explaining what fields are important and what they do

'''





def main():
    parser = argparse.ArgumentParser(description="Train YOLO model from json config file details")
    parser.add_argument("--json_config_path", required=True, help="Path to json config file")
    args = parser.parse_args()

    json_config_path = args.json_config_path

    try:
        with open(json_config_path, 'r') as config_file:
            json_config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file.")

    op.data_processing.make_config.make_config(json_config)

    op.data_processing.split_data_pipe(source_dir=json_config['dataset_folder'], output_dir=json_config['dataset_folder'], split=json_config['split'], seed=json_config['constants']['SEED'])

    # # predicting_videos.predict_vid_from_json(json_config)
    op.training.train_model_json(json_config)
    # trainer.train_model(json_config)

    return



if __name__ == "__main__":
    main()