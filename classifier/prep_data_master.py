import os
import random
import re
import shutil
from tqdm import tqdm
from pathlib import Path
import pandas as pd



subject_col_name = "subID"
filepath_col_name = "path"

random.seed(32)

def gen_n_split(df, which_class, output_dir, first_n):
    training_split_dir = Path(f"{output_dir}\\first_{first_n}_split\\training_split\\{which_class}")
    validating_split_dir = Path(f"{output_dir}\\first_{first_n}_split\\validating_split\\{which_class}")

    os.makedirs(training_split_dir, exist_ok=True)
    os.makedirs(validating_split_dir, exist_ok=True)

    subs = get_list_subs(df)
    for s in subs:
        subject_df = df[df[subject_col_name] == s]        
        subject_file_paths = subject_df[filepath_col_name]

        if len(subject_file_paths) >= first_n:
            # # Create train and test directories if they don't exist
            # Copy files for training model
            for file_name in tqdm(subject_file_paths[:first_n], desc=f"copying training split : {s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
                dst = os.path.join(training_split_dir, Path(file_name).name)
                shutil.copy(file_name, dst)

            # Copy files for testing model
            for file_name in tqdm(subject_file_paths[first_n:], desc=f"copying validating split: {s}"):
                # src = os.path.join(directory, file_name)
                dst = os.path.join(validating_split_dir, Path(file_name).name)
                shutil.copy(file_name, dst)
        else:
             # Copy files to train set
            for file_name in tqdm(subject_file_paths, desc=f"copying training split, no validation for {s}"):
                # print(file_name)
                # src = os.path.join(directory, file_name)
                dst = os.path.join(training_split_dir, Path(file_name).name)
                shutil.copy(file_name, dst)


# returns list of subjects in dataframe
def get_list_subs(df:pd.DataFrame) -> list[str]:
    subs = df[subject_col_name].unique()
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


def extract_target_df(df):
    print()
    return df



def main():
    classes = ["positive_JA",
               "negative_JA"]
    
    CSV_PATH = Path(".")
    DATA_OUT_PATH = Path(".")
    N = 1000

    df = pd.read_csv(CSV_PATH)
    target_df = extract_target_df(df)

    for c in classes:
        gen_n_split(target_df, c, DATA_OUT_PATH, N)

if __name__ == "__main__":
    main()