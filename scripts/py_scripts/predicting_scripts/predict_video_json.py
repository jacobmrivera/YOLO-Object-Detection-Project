#!/usr/bin/env python
import json
import argparse
import obj_detector.predicting.predicting_videos as predicting_videos

'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/03/2024

Description:
    Will predict objects on a video given the info inside a json config file
'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video from json config file")
    parser.add_argument("--json_config_path", required=True, help="Path to json config file")
    args = parser.parse_args()

    json_config_path = args.json_config_path

    try:
        with open(json_config_path, 'r') as config_file:
            json_config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file.")

    predicting_videos.predict_vid_from_json(json_config)

    return

if __name__ == "__main__":
    main()