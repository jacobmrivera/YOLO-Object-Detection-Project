# "z:\Jacob\YOLO_Predicted\20221112_10041_cam07_predicted_data\pred_labels_w_conf"

import os

from obj_predictor.data_processing import smooth
from tqdm import tqdm


'''
Across all subjects, want data regarding each object. 

First:
    Make a function that will go thorugh an entire subjects predicted frames, and make a text
    file for each object at the subject level. Get bounding box, confidence, and frame name.

Second:
    Go through every subject and concatenate obj text files into either one big one or maybe a csv. -- I like idea of csv
    however, can i just append to a csv?

'''

def create_sub_obj_txts(output_dir, num_objs):
    for i in range(1, num_objs + 1):
        file_name = os.path.join(output_dir, f"{i}.txt")
        with open(file_name, 'w') as file:
            file.write("")


def create_exp_obj_csvs(output_dir, num_objs):
    for i in range(1, num_objs + 1):
        file_name = os.path.join(output_dir, f"{i}.csv")
        with open(file_name, 'w') as file:
            file.write("")


def list_directories(path):
    directories = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
    return directories


def gather_obj_lvl_predictions(input_dir, output_dir, num_objs):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # create a text file for each object in output_dir
    create_sub_obj_txts(output_dir, num_objs)

    # subs = list_directories(input_dir)

    frames_path = os.path.join(input_dir, "pred_labels_w_conf")
    # get list of all frames, order doesn't matter?
    frames_list = smooth.list_files_in_directory(frames_path, '.txt')

    # # loop though all frames,
    # for frame in tqdm(frames_list, desc="Processing frames"):
    #     # loop through lines of file
    #     with open(os.path.join(frames_path, frame), 'r') as file:
    #         for line in file:
    #             # Do something with each line, for example, print it
    #              line = line.strip()
    #              obj_num =  line.split(' ')[0]
    #              new_line = line + f"_{frame}\n"
                
    #             # opens obj_lvl text file and appends
    #              with open(os.path.join(output_dir, obj_num + ".txt"), 'a') as file:
    #                 file.write(new_line)
    #         # append line to its obj file



    
    # Dictionary to store file handles
    file_handles = {}
    try:

        for frame in tqdm(frames_list, desc="Processing frames"):
            with open(os.path.join(frames_path, frame), 'r') as file:
                for line in file:
                    line = line.strip()
                    obj_num = int(line.split(' ')[0]) + 1
                    new_line = line + f" _{frame}\n"
                    
                    # Check if file handle already exists, if not open the file and store the handle
                    if obj_num not in file_handles:
                        file_handles[obj_num] = open(os.path.join(output_dir, f"{obj_num}.txt"), 'a')
                    
                    # Write the line to the file
                    file_handles[obj_num].write(new_line)
    finally:

        # Close all file handles
        for file_handle in file_handles.values():
            file_handle.close()


def concat_obj_lvl_pred_across_subs(input_dir, output_dir, num_objs):
    print()

    # generate output csvs for each 

    # given directory full of subject dirs, loop thoough
        # loop throug all objs
            # for every line in the obj text file, append it to the csv, structing it if needed
    


def main():

    p = "z:\\Jacob\\YOLO_Predicted\\20221112_10041_cam07_predicted_data"
    gather_obj_lvl_predictions(p, p, 27)

if __name__ == "__main__":
    main()