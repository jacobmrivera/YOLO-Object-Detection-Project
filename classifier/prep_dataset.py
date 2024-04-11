import os
import random
import shutil
from tqdm import tqdm

pos_or_neg = "positive"

# Define the directory containing the files
# directory = f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\child_{pos_or_neg}_frames"
directory = f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_training\\{pos_or_neg}_JA"
# Define the paths for train and test directories
output_dataset_dir = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_training"
train_dir = os.path.join(f"{output_dataset_dir}", "train", f"{pos_or_neg}_JA")
test_dir = os.path.join(f"{output_dataset_dir}", "test", f"{pos_or_neg}_JA")


# Get the list of files in the directory
file_names = os.listdir(directory)

# Shuffle the list of files
random.seed(32)
random.shuffle(file_names)
# file_names = file_names[:100_000]
# Calculate the number of files for train and test sets
total_files = len(file_names)
train_size = int(0.8 * total_files)
test_size = total_files - train_size



# Create train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Copy files to train set
for file_name in tqdm(file_names[:train_size], desc="Copying train files"):
    src = os.path.join(directory, file_name)
    dst = os.path.join(train_dir, file_name)
    shutil.copy(src, dst)

# Copy files to test set
for file_name in tqdm(file_names[train_size:], desc="Copying test files"):
    src = os.path.join(directory, file_name)
    dst = os.path.join(test_dir, file_name)
    shutil.copy(src, dst)

print("Dataset split into train and test sets successfully.")





