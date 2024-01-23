#!/usr/bin/env python
import json
import argparse
import obj_predictor.predicting.predict as predict

'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/03/2024

Description:
    Will predict objects on a video given the info inside a json config file

'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video")
    parser.add_argument("--model_path", required=True, help="Path to YOLO model .pt file")
    parser.add_argument("--video_input", required=True, help="Input video name and path")
    parser.add_argument("--video_output", required=False, help="Output video name and path, if absent, input name plus _predicted will be used")
    parser.add_argument("--width", type=int, required=False, default=1280, help="Width of predicted video")
    parser.add_argument("--height", type=int, required=False, default=720, help="Height of predicted video")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions")

    args = parser.parse_args()

    model_path = args.model_path
    video_input = args.video_input
    video_output = args.video_output
    width = args.width
    height = args.height
    confidence = args.confidence

    json_config_path = args.json_config_path

    try:
        with open(json_config_path, 'r') as config_file:
            json_config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file.")

    predict.predict_video(model_path, video_input, video_output, width, height, confidence)

    return

if __name__ == "__main__":
    main()