#!/usr/bin/env python
import json
import argparse
import obj_predictor.data_processing.smooth as smooth

'''
Created by Jacob Rivera
Spring 2024

Last edit: 01/22/2024

Description:


'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video")
    parser.add_argument("--input_dir", required=True, help="Path to text file annotations")
    parser.add_argument("--max_skips", required=False, type=int, default=2, help="Number of frames to extrapolate over")


    args = parser.parse_args()

    input_dir = args.input_dir
    max_skips = args.max_skips

    smooth.smooth_annotations(input_dir, max_skips)

    return

if __name__ == "__main__":
    main()