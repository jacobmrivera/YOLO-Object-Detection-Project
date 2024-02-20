#!/usr/bin/env python
import json
import argparse
import obj_predictor.predicting.predict as predict
import os
'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/03/2024

Description:
    Will predict objects on a video given the info inside a json config file

'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video.")
    parser.add_argument("--model_path", required=True, help="Path to YOLO model .pt file.")
    parser.add_argument("--video_input", required=True, help="Input video name and path.")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions.")
    parser.add_argument("--output_dir", type=str, required=False, default=None, help="Output directory for predicted files.")

    parser.add_argument("--save_annot", type=int, required=False, default=False, help="flag to save text annotations.")
    parser.add_argument("--save_frames", type=int, required=False, default=False, help="flag to save individual frames.")
    parser.add_argument("--save_yolo_vid", type=int, required=False, default=True, help="flag to save predicted video.")
    parser.add_argument("--save_drawn_frames", type=int, required=False, default=False, help="flag to save yolo drawn/annotated frames.")
    parser.add_argument("--normalize_annot", type=int, required=False, default=False, help="flag to save annotations normalized or not.")
    parser.add_argument("--save_conf", type=int, required=False, default=False, help="flag to save annotations normalized or not.")

    args = parser.parse_args()

    model_path = args.model_path
    video_input = args.video_input
    confidence = args.confidence
    output_dir = args.output_dir
    if output_dir is None:
        output_dir = os.path.dirname(video_input)
    # add flag for normalized annot
    save_annot = True if args.save_annot == 1 else False
    save_frames = True if args.save_frames == 1 else False
    save_yolo_vid = True if args.save_yolo_vid == 1 else False
    save_drawn_frames = True if args.save_drawn_frames == 1 else False
    normalize_annot = True if args.normalize_annot == 1 else False
    save_conf = True if args.save_conf == 1 else False

    predict.predict_video(model_path=model_path, input_vid=video_input, output_dir=output_dir, conf=confidence, save_annot=save_annot, save_frames=save_frames, save_yolo_vid=save_yolo_vid, save_drawn_frames=save_drawn_frames, normalize_annot=normalize_annot, save_conf=save_conf)

    return

if __name__ == "__main__":
    main()