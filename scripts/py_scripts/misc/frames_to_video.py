#!/usr/bin/env python

import argparse
import obj_detector as op

'''
Created by Jacob Rivera
Feb 27 2024
'''





def main():
    parser = argparse.ArgumentParser(description="Extract all frames from video and save to folder")
    parser.add_argument("--input_dir", required=True, help="Path to video to extract frames from")
    parser.add_argument("--output_dir", required=False, default="", help="Directory to save frames to")


    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    # input_dir = "M:\\experiment_351\\included\\__20221112_10041\\cam07_frames_p"
    # output_dir = "Z:\\Jacob\\YOLO_Predicted\\20221112_10041_cam07_predicted_data\\test.mp4"

    op.data_processing.util.frames_to_video(input_dir, output_dir)


    return

if __name__ == "__main__":
    main()