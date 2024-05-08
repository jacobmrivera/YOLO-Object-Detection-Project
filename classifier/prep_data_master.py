import os
import random
import re
import shutil
from tqdm import tqdm
from pathlib import Path
import pandas as pd


TRAIN_TEST_SPLIT = 0.8
SEED = 32

sub_class_train_count = {}

def gen_n_split(df, which_class, output_dir, first_n, mins_dict):
    training_split_dir = Path(f"{output_dir}\\first_{first_n}_split\\training_split\\{which_class}")
    validating_split_dir = Path(f"{output_dir}\\first_{first_n}_split\\validating_split\\{which_class}")

    os.makedirs(training_split_dir, exist_ok=True)
    os.makedirs(validating_split_dir, exist_ok=True)

    subs = get_list_subs(df)
    for s in subs:
        subject_df = df[df["subID"] == s]        
        subject_file_paths = subject_df["framePath"]

        # if s in sub_class_train_count.keys():
            
        if mins_dict[s] >= first_n:
        # if len(subject_file_paths) >= first_n and mins_dict[s] >= first_n:

            # Copy files for training model
            for file_name in tqdm(subject_file_paths[:first_n], desc=f"copying training split : {s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
 
                dst = os.path.join(training_split_dir, str(s) + "_" + Path(file_name).name)
                shutil.copy(file_name, dst)

            # Copy files for testing model
            for file_name in tqdm(subject_file_paths[first_n:], desc=f"copying validating split: {s}"):
                # src = os.path.join(directory, file_name)
                dst = os.path.join(validating_split_dir,  str(s) + "_" + Path(file_name).name)
                shutil.copy(file_name, dst)
        else:
             # Copy files to train set
            for file_name in tqdm(subject_file_paths[:mins_dict[s]], desc=f"copying training split, no validation for {s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
                dst = os.path.join(training_split_dir, str(s) + "_" + Path(file_name).name)
                shutil.copy(file_name, dst)
    return Path(f"{output_dir}\\first_{first_n}_split\\training_split")

# returns list of subjects in dataframe
def get_list_subs(df:pd.DataFrame) -> list[str]:
    subs = df["subID"].unique()
    return subs


# will split data into train test split for files 
#   inside given directory
def train_test_split_class(input_dir:Path, class_name:str):

    train_dir = os.path.join(f"{input_dir}", "train", f"{class_name}")
    test_dir = os.path.join(f"{input_dir}", "test", f"{class_name}")

    # Create train and test directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Get the list of files in the directory
    file_names = os.listdir(input_dir)
    random.shuffle(file_names)

    # Calculate the number of files for train and test sets
    total_files = len(file_names)
    train_size = int(0.8 * total_files)
    test_size = total_files - train_size

    # Copy files to train set
    for file_name in tqdm(file_names[:train_size], desc=f"Copying {class_name} train files"):
        src = os.path.join(input_dir, file_name)
        dst = os.path.join(train_dir, file_name)
        shutil.copy(src, dst)

    # Copy files to test set
    for file_name in tqdm(file_names[train_size:], desc=f"Copying {class_name} test files"):
        src = os.path.join(input_dir, file_name)
        dst = os.path.join(test_dir, file_name)
        shutil.copy(src, dst)


def extract_target_df(df, *conditions):

    # Combine all conditions using logical AND operator
    combined_condition = pd.Series(True, index=df.index)
    for condition in conditions:
        combined_condition &= condition

    filtered_df = df[combined_condition]

    return filtered_df

def get_min_each_sub(df, class_dict):
    
    mins_dict = {}
    for c,v in class_dict.items():
        subjects = get_list_subs(df)
        
        for sub in subjects:
            size = len(df[(df["subID"] == sub) & (df["status"] == v)])
            
            if sub in mins_dict.keys():
                mins_dict[sub] = min(size, mins_dict[sub])
            else:
                mins_dict[sub] = size
    return mins_dict

def main():
    random.seed(SEED)

    class_dict = {
        "positive_JA":1,
        "negative_JA":2,
                  }
    
    CSV_PATH = Path("C:\\Users\\multimaster\\Desktop\\JA_DATASET\\newer_csvs\\exp12_JA_obj17_datasheet_child-view.csv")
    DATA_OUT_PATH = Path("C:\\Users\\multimaster\\Desktop\\JA_DATASET\\newer_csvs\\exp12_JA_obj17_data_child-view")
    N = 500

    df = pd.read_csv(CSV_PATH)
    minimums_dict = get_min_each_sub(df, class_dict)
    ### CONDITIONS
    for cl_ss, val in class_dict.items():
        cond = df["status"] == val
        training_split_dir = gen_n_split(df[cond], cl_ss, DATA_OUT_PATH, N, minimums_dict)

        # train_test_split_class(DATA_OUT_PATH.joinpath("training_split"), cl_ss)

    # subs = get_list_subs(df)

    # for s in subs:
    #     print(s)
    #     print(len(df[(df["subID"] == s) & (df["status"] == 1)]))
    #     print(len(df[(df["subID"] == s) & (df["status"] == 2)]))
    #     print()

if __name__ == "__main__":
    main()