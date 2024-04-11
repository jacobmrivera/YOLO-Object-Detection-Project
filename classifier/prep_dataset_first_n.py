import os
import random
import re
import shutil
from tqdm import tqdm
from pathlib import Path


# Sorting function to handle file names with integers
# without, sorts like 1, 10, 100, 1000, 1001
def natural_sort_key(filename):
    # Split the filename into parts of digits and non-digits
    parts = [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', filename)]
    return parts


# Returns a list of all files with a particular ending from a dir
def list_files_in_directory(directory_path:str|Path, ending:str=None) -> list[str]:
    try:
        # Get all files in the directory
        files = os.listdir(directory_path)

        if ending:
            # Filter the list to include only text files (files with a ".txt" extension)
            files_list = [file for file in files if file.lower().endswith(ending)]
        else:
            files_list = [file for file in files if file.lower()]

        # Sort the list of files alphabetically
        sorted_files = sorted(files_list, key=natural_sort_key)

        for i in range(len(sorted_files)):
            sorted_files[i] = os.path.join(directory_path, sorted_files[i])
        return sorted_files

    except OSError as e:
        print(f"Error: {e}")
        return []

fraction = 0.1

first_percent = f"{int(fraction*100)}%"

subs = ['18796', '17608', '18419', '16963', '19954', '17848', '17757', '18431', '18742', 
'17782', '18996', '19615', '19859', '17843', '17878', '17527', '17874', '19812', '20510', '17718', 
'18625', '19544', '19505', '18068', '21015', '17662', '17275', 
'18100', '18459', '17933', '17402', '17592', '17919', '17565', '19357', '19536']

def get_list_subs(input_dir, which_class, output_dir):
    for_output_dir = Path(f"{output_dir}\\first_{first_percent}_split\\for_model\\{which_class}_JA")
    to_output_dir = Path(f"{output_dir}\\first_{first_percent}_split\\for_testing\\{which_class}_JA")

    files = list_files_in_directory(input_dir)
    os.makedirs(for_output_dir, exist_ok=True)
    os.makedirs(to_output_dir, exist_ok=True)

    for s in subs:
        subset = [item for item in files if Path(item).name[:5]==s]
        N = int(len(subset)*fraction)
        if len(subset) >= N:
            # # Create train and test directories if they don't exist
            # Copy files for training model
            for file_name in tqdm(subset[:N], desc=f"{s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
                dst = os.path.join(for_output_dir, Path(file_name).name)
                shutil.copy(file_name, dst)

            # Copy files for testing model
            for file_name in tqdm(subset[N:], desc=f"{s}"):
                # src = os.path.join(directory, file_name)
                dst = os.path.join(to_output_dir, Path(file_name).name)
                shutil.copy(file_name, dst)
        else:
             # Copy files to train set
            for file_name in tqdm(subset, desc=f"{s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
                dst = os.path.join(for_output_dir, Path(file_name).name)
                shutil.copy(file_name, dst)


output_dir = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data"
get_list_subs(Path("C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\negative_JA"), "negative", output_dir)

get_list_subs(Path("C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\positive_JA"), "positive", output_dir)