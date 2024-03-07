import os
import re
from tqdm import tqdm

'''
Created by Jacob Rivera
Spring 2024
Last edit: 1/22/2024


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




# Given two bounding box annotations and the number of frames to fill in for,
# returns a list of bounding box coordinates arrays
# 
# Averages the annotations across the missed frames
def get_equidistant_points(start, end, num_points, sig_figs=5):
    if num_points < 2:
        raise ValueError("Number of points must be at least 2.")
    # elif start[0] != end[0]:
    #     raise ValueError(f"Bounding box annotations must be for the same object.\nStart: obj {start[0]}\nEnd:   obj {end[0]}")
    
    # Calculate the step size for interpolation
    step_size = 1.0 / (num_points - 1)

    # Perform linear interpolation
    points = [[round(start[0] + i * step_size * (end[0] - start[0]), sig_figs), 
               round(start[1] + i * step_size * (end[1] - start[1]), sig_figs),
               round(start[2] + i * step_size * (end[2] - start[2]), sig_figs),
               round(start[3] + i * step_size * (end[3] - start[3]), sig_figs),
               round(start[4] + i * step_size * (end[4] - start[4]), sig_figs)]

              for i in range(1, num_points - 1)]

    return points



# returns a dictionary version of bb txt file with
# obj num as the key
def txt_to_dict(file_path):

    output_dict = {}
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Process each line as needed
            line = line.strip()
            line_arr = line.split(" ")
            output_dict[int(line_arr[0])] = [float(item) for item in line_arr[1:]]
    return output_dict 



# given a text file, bounding box annotation line will be added
def add_line_to_txt(file_path, key, arr):
    with open(file_path, 'a') as file:
        file.write(f"{key} {arr[0]} {arr[1]} {arr[2]} {arr[3]} {arr[4]}\n")


        
'''
Smooths bounding box coordinates by extrapolating points given the curr file
    has the obj, and one of the next files has the obj. It will fill in the files
    missing the obj between the curr and the file that it is found in. 

Will smooth over as many files in the array that there are, so limit the array size of
    next_files to limit how many extrapolated annotations will be added.
'''
def check_window(curr_file, next_files):
    # num_objs = 26
    curr_dict = txt_to_dict(curr_file)
    '''
    current dict has the items that i want to check if future frames are missing.
    '''
    file_dicts = []

    # create an array of dictionarys of the next n files
    for f in next_files:
        out = txt_to_dict(f)
        # print(f"out: {out}")
        file_dicts.append(out)

    # loop through all objs in curr_dict
    for i in curr_dict.keys():

        count = 0

        # loop through next n files
        index = 0
        missed = 0

        # loop through forward file dictionaries
        for d in file_dicts:
            count += 1

            # check if obj from curr is in one of the next files,
            # when it is, get the missing points
            if i in d.keys() and missed == 1:
                avg_annot = get_equidistant_points(curr_dict[i], d[i], count + 1, sig_figs=5)
                # add extrapolated points to files missing it
                for fix in range(index):
                    add_line_to_txt(next_files[fix], i, avg_annot[fix])
                missed = 0
                continue
            elif (i not in d.keys() ):
                missed = 1

            index += 1

# input: 
#   input_dir: directory containing text files
#   max_skips: number of frames to fill in missing objects
# output:
#   none
def smooth_annotations(input_dir, max_skip=2):

    text_files = list_files_in_directory(input_dir, '.txt')
    text_files = [os.path.join(input_dir, j) for j in text_files]
    # print(text_files)

    for i in tqdm(range(0, len(text_files) - max_skip- 2), total=len(text_files) - max_skip):
        # gets the next max_skips + 1 files to check for skipping objs
        look_aheads = [text_files[i + j] for j in range(1, max_skip + 2)]

        check_window(text_files[i], look_aheads)

# smooth_annotations("Z:\\Jacob\\lobster_ostrich\\labels")


