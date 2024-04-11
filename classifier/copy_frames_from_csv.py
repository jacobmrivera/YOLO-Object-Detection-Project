import csv
import os
from pathlib import Path
import pandas as pd
import shutil
from tqdm import tqdm

def copy_images_from_csv(csv_file, destination_path):
    with open(csv_file, 'r') as file:
        row_count = sum(1 for row in file)
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
 
        for row in tqdm(reader,total=row_count, desc="copying!"):
            
            # Assuming each row contains a single path string
            path = row[0]
            if os.path.isfile(path):  # Check if the file exists
                # Extract the filename from the path
                filename = os.path.basename(path)

                sub = path.split("\\")[-3][-5:]
                # name = filename.split("\\")[-1]

                # Construct the destination path
                # destination = os.path.join(destination_path, filename)
                destination = os.path.join(destination_path, f"{sub}_{filename}")
                # print(destination)
                # Copy the file to the destination
                shutil.copyfile(path, destination)
                # print(f"Image copied from {path} to {destination}")
            else:
                print(f"File not found: {path}")






def main():

    # num = 17
    # pos_or_neg = "positive"
    # # Example usage:
    # csv_file = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\{pos_or_neg}_JA_obj_{num}.csv")  # Path to your CSV file
    # destination_folder = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\{pos_or_neg}_JA")  # Specify the destination folder
    # os.makedirs(destination_folder, exist_ok=True)
    
    # copy_images_from_csv(csv_file, destination_folder)

    # pos_or_neg = "negative"
    # # Example usage:
    # csv_file = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\{pos_or_neg}_JA_obj_{num}.csv")  # Path to your CSV file
    # destination_folder = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\{pos_or_neg}_JA")  # Specify the destination folder
    # os.makedirs(destination_folder, exist_ok=True)
    
    # copy_images_from_csv(csv_file, destination_folder)

    num1 = 17
    num2 = 15
    pos_or_neg = "positive"
    # Example usage:
    csv_file = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_obj_{num1}.csv")  # Path to your CSV file
    destination_folder = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_{num1}")  # Specify the destination folder
    os.makedirs(destination_folder, exist_ok=True)
    
    copy_images_from_csv(csv_file, destination_folder)


    # Example usage:
    csv_file = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_obj_{num2}.csv")  # Path to your CSV file
    destination_folder = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_{num2}")  # Specify the destination folder
    os.makedirs(destination_folder, exist_ok=True)
    
    copy_images_from_csv(csv_file, destination_folder)



    pos_or_neg = "negative"
    # Example usage:
    csv_file = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_obj_{num1}_{num2}.csv")  # Path to your CSV file
    destination_folder = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_{num1}_{num2}_split_data\\{pos_or_neg}_JA_{num1}_{num2}")  # Specify the destination folder
    os.makedirs(destination_folder, exist_ok=True)
    
    copy_images_from_csv(csv_file, destination_folder)

if __name__ == "__main__":
    main()