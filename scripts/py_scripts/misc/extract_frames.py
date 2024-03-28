#!/usr/bin/env python

import argparse
import obj_detector.data_processing.frame_extractor as frame_extractor

'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/04/2024

Description:
    Inputs a video, outputs a folder of frames from the video

    If no output directory is specified, then the output directory is the video name + "_frames"

Assumptions:
    - openCV extracts frames at the correct frame rate,
      right now, no fps given, so I assume it extracts frame by frame regardless of fps
    - video is in .mp4 format

'''





def main():
    parser = argparse.ArgumentParser(description="Extract all frames from video and save to folder")
    parser.add_argument("--input_video", required=True, help="Path to video to extract frames from")
    parser.add_argument("--output_dir", required=False, default="", help="Directory to save frames to")
    parser.add_argument("--frames_prefix", required=False, default="frame_", help="Directory to save frames to")
    parser.add_argument("--debug", required=False, type=int, default=0, help="Debug flag for print statements")

    args = parser.parse_args()

    input_video = args.input_video
    output_dir = args.output_dir
    frames_prefix = args.frames_prefix
    debug = args.debug

    frame_extractor.process_video(input_video, output_dir, frames_prefix, debug)

    return

if __name__ == "__main__":
    main()