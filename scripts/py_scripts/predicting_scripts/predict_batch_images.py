#!/usr/bin/env python
import json
import argparse
import obj_detector.predicting.predict as predict
import os
from tqdm import tqdm
import shutil

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
    parser.add_argument("--input_dir", required=True, help="Input image name and path.")
    parser.add_argument("--output_dir", required=False, default=".", help="Output directory for predictions.")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions.")
    parser.add_argument("--save_yolo_img", type=int, required=False, default=0, help="Flag to save image with yolo drawn bounding box")
    parser.add_argument("--save_conf", type=int, required=False, default=0, help="flag to save conf in txt file with bounding box")
    parser.add_argument("--normalize_annot", type=int, required=False, default=1, help="flag to normalize output bounding box values")

    args = parser.parse_args()

    model_path = args.model_path
    input_dir = args.input_dir
    output_dir = args.output_dir
    confidence = args.confidence
    save_yolo_img = args.save_yolo_img
    save_conf = args.save_conf
    normalize_annot = args.normalize_annot

    if (os.path.exists(output_dir)):
        shutil.rmtree(output_dir)
    
    os.makedirs(output_dir, exist_ok=True)

    dir_label = input_dir.split('\\')[-2]

    for img in tqdm(os.listdir(input_dir),f"Processing frames... {dir_label}"):
        if img.endswith(".jpg"):
            img_path = os.path.join(input_dir, img)
        predict.predict_image_save_annot(img_path, model_path, output_dir, confidence, save_yolo_img, save_conf, normalize_annot)

    return

if __name__ == "__main__":
    main()