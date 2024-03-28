#!/usr/bin/env python

import json
import argparse

import sys
import os
import obj_detector as op


import obj_detector as op
import obj_detector.data_processing.smooth as smooth
import obj_detector.data_processing.draw as draw
from tqdm import tqdm

'''
Created by Jacob Rivera
Spring 2024

Last edit: 02/02/2024

Description:

'''


def get_text_file(input_img):
    path, img_name = os.path.split(input_img)
    text_name = img_name[:-3] + "txt"
    return text_name



def main():
    parser = argparse.ArgumentParser(description="Train YOLO model from passed arguements")
    parser.add_argument("--images_dir", required=True, help="")
    parser.add_argument("--labels_dir", required=True, help="")
    parser.add_argument("--output_dir", required=True, help="")
    
    args = parser.parse_args()

    images_dir = args.images_dir
    labels_dir = args.labels_dir
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    all_images = smooth.list_files_in_directory(images_dir, '.jpg')

    for img in tqdm(all_images, desc="Drawing annotations on images..."):
        img_path = os.path.join(images_dir, img)

        text_file = os.path.join(labels_dir, get_text_file(img))

        path, img_root = os.path.split(img)
        drawn_img = os.path.join(output_dir, img_root[:-4] + "_drawn.jpg")

        draw.draw_single_frame(img_path, text_file, drawn_img, True )

    return



if __name__ == "__main__":
    main()