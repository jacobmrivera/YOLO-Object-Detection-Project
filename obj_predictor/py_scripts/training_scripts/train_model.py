#!/usr/bin/env python
import json
import argparse
import obj_predictor.training.train as trainer

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

    # predicting_videos.predict_vid_from_json(json_config)
    trainer.train_model(json_config)

    return



if __name__ == "__main__":
    main()