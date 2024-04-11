#!/usr/bin/env python

import argparse

from tqdm import tqdm
import obj_detector as op
import os
import re
import cv2
'''
Created by Jacob Rivera
Feb 27 2024
'''

# Sorting function to handle file names with integers 
# without, sorts like 1, 10, 100, 1000, 1001
def natural_sort_key(filename):
    # Split the filename into parts of digits and non-digits
    parts = [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', filename)]
    return parts


# Returns a list of all files with a particular ending from a dir
def list_files_in_directory(directory_path, ending):
    try:
        # Get all files in the directory
        files = os.listdir(directory_path)

        # Filter the list to include only text files (files with a ".txt" extension)
        filtered_files = [file for file in files if file.lower().endswith(ending)]

        # Sort the list of files alphabetically
        sorted_files = sorted(filtered_files, key=natural_sort_key)

        return sorted_files
    
    except OSError as e:
        print(f"Error: {e}")
        return []

def frames_to_video(input_dir, output_video_path, fps=30):
    # Get the list of image files in the input directory
    # image_files = [f for f in os.listdir(input_dir) if f.endswith('.png') or f.endswith('.jpg')]
    image_files = op.data_processing.smooth.list_files_in_directory(input_dir, ".jpg")
    if not image_files:
        print("No image files found in the directory.")
        return


    # Get the first image to retrieve dimensions
    first_image = cv2.imread(os.path.join(input_dir,image_files[0]))
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID', 'MJPG', etc.
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each frame to the video
    # for img in tqdm(os.listdir(input_dir),f"Processing frames... {dir_label}"):

    for image_file in tqdm(image_files, desc="Stitching frames into video..."):
        frame = cv2.imread(os.path.join(input_dir,image_file))
        out.write(frame)

    # Release VideoWriter and destroy any OpenCV windows
    out.release()
    cv2.destroyAllWindows()

    print(f"Video saved to: {output_video_path}")


def main():
    # parser = argparse.ArgumentParser(description="Extract all frames from video and save to folder")
    # parser.add_argument("--input_dir", required=True, help="Path to video to extract frames from")
    # parser.add_argument("--output_dir", required=False, default="", help="Directory to save frames to")


    # args = parser.parse_args()

    # input_dir = args.input_dir
    # output_dir = args.output_dir


    input_dir = "C:\\Users\\multimaster\\Desktop\\practice_pipeline\\__20221112_10041_cam07_frames_predicted_data\\not_smoothed_frames"
    output_dir = "C:\\Users\\multimaster\\Desktop\\practice_pipeline\\__20221112_10041_cam07_frames_predicted_data\\not_smoothed.mp4"

    frames_to_video(input_dir, output_dir)


    return

if __name__ == "__main__":
    main()