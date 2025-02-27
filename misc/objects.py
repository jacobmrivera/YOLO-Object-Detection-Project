# "z:\Jacob\YOLO_Predicted\20221112_10041_cam07_predicted_data\pred_labels_w_conf"

import os
import shutil
from obj_detector.data_processing import smooth
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
    for i in range(num_objs):
        file_name = os.path.join(output_dir, f"{i}.txt")
        with open(file_name, 'w') as file:
            file.write("")


def create_exp_obj_csvs(output_dir, num_objs):
    for i in range(num_objs):
        file_name = os.path.join(output_dir, f"{i}.csv")
        with open(file_name, 'w') as file:
            file.write("")


def list_directories(path):
    directories = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
    return directories


def append_files_method2(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        with open(file2_path, 'a') as file2:
            shutil.copyfileobj(file1, file2)



def gather_obj_lvl_predictions(input_dir, output_dir, num_objs):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    # create a text file for each object in output_dir
    print("Creating object text files...")
    create_sub_obj_txts(output_dir, num_objs)

    # subs = list_directories(input_dir)

    frames_path = os.path.join(input_dir, "pred_labels_w_conf")
    # get list of all frames, order doesn't matter?
    frames_list = smooth.list_files_in_directory(frames_path, '.txt')
    
    # Dictionary to store file handles
    file_handles = {}
    try:

        for frame in tqdm(frames_list, desc="Processing frames"):
            with open(os.path.join(frames_path, frame), 'r') as file:
                for line in file:
                    line = line.strip()
                    obj_num = int(line.split(' ')[0])
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
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    
    # create a text file for each object in output_dir
    print("Creating object text files...")
    create_sub_obj_txts(output_dir, num_objs)


    dir_list = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]

    for dir in tqdm(dir_list, desc="Processing directories..."):
        print()
        dir_full_path = os.path.join(input_dir, dir)
        if not os.path.isdir(dir_full_path):
            continue

        # put subject's obj lvl data in subject folder
        gather_obj_lvl_predictions(os.path.join(input_dir,dir), os.path.join(input_dir, dir), num_objs)

        # Iterate through every subject's object files
        for i in range(num_objs):

            in_txt_path = os.path.join(input_dir, dir, f"{i}.txt")
            out_txt_path = os.path.join(output_dir, f"{i}.txt")

            append_files_method2(in_txt_path, out_txt_path)

    
    # generate output csvs for each 


def main():

    p = "z:\\Jacob\\YOLO_Predicted"
    concat_obj_lvl_pred_across_subs(p, p, 27)

if __name__ == "__main__":
    main()