#!/usr/bin/env python
import json
import argparse
import obj_predictor.predicting.predict as predict

'''
Created by Jacob Rivera
Spring 2024

Last edit: 01/25/2024

Description:
    Will predict objects on a video given the info inside a json config file

'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video")
    parser.add_argument("--model_path", required=True, help="Path to YOLO model .pt file")
    parser.add_argument("--video_input", required=True, help="Input video name and path")
    parser.add_argument("--annot_output", required=True, help="Path where predicted annotations will be saved, as well as frames if save_frames is True")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions")
    parser.add_argument("--save_frames", type=bool, required=False, default=False, help="Save frames to output directory")

    args = parser.parse_args()

    model_path = args.model_path
    video_input = args.video_input
    annot_output = args.annot_output
    confidence = args.confidence
    save_frames = args.save_frames


    predict.predict_vid_save_annot(model_path, video_input, annot_output, confidence, save_frames)

    return

if __name__ == "__main__":
    main()