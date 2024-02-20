#!/usr/bin/env python
import json
import argparse
import obj_predictor.predicting.predict as predict
import os
'''
Created by Jacob Rivera
Fall 2023

Last edit: 02/20/2024

Description:
    Predicts objs in a single image.

    Output depends on given flags.
'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video.")
    parser.add_argument("--model_path", required=True, help="Path to YOLO model .pt file.")
    parser.add_argument("--image_input", required=True, help="Input image name and path.")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions.")
    parser.add_argument("--save_yolo_img", type=int, required=False, default=0, help="Flag to save image with yolo drawn bounding box")
    parser.add_argument("--save_conf", type=int, required=False, default=0, help="flag to save conf in txt file with bounding box")

    args = parser.parse_args()

    model_path = args.model_path
    image_input = args.image_input
    confidence = args.confidence
    save_yolo_img = args.save_yolo_img
    save_conf = args.save_conf


    predict.predict_image_save_annot(image_input, model_path, confidence, save_yolo_img, save_conf)

    return

if __name__ == "__main__":
    main()