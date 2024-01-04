import os
import random
import shutil

# from make_dataset import *


# # Shuffles labels folder,
# def train_test_split_frames(dataset_folder, labels_folder, image_folder, split):
#     os.makedirs(dataset_folder, exist_ok=True)

#     file_names = os.listdir(labels_folder)
    
#     random.shuffle(file_names)
#     split_point = int(split * len(file_names))

#     train_test_labels = [file_names[:split_point],file_names[split_point:]]


#     print(train_test_labels)
#     label_type = {0:'train', 1:'test'}
    
#     for i, labels in enumerate(train_test_labels):
#         sub_dataset_folder = f'{dataset_folder}\\{label_type[i]}'
#         print(i)
#         make_dataset(labels, image_folder, sub_dataset_folder)




# SPLIT = 0.8
# TOP_PATH = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data"
# OUTPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data"
# # Set a seed for reproducibility
# random.seed(42)

# # Set the source directories
# source_text_dir = TOP_PATH + "\\labels"
# source_image_dir = TOP_PATH + "\\images"

# # Set the destination directories
# out_train_text_dir = OUTPUT_DIR + "\\train\\labels"
# out_train_image_dir = OUTPUT_DIR + "\\train\\images"
# out_test_text_dir =  OUTPUT_DIR + "\\test\\labels"
# out_test_image_dir = OUTPUT_DIR + "\\test\\images"

# # Create the destination directories if they don't exist
# os.makedirs(out_train_text_dir, exist_ok=True)
# os.makedirs(out_train_image_dir, exist_ok=True)
# os.makedirs(out_test_text_dir, exist_ok=True)
# os.makedirs(out_test_image_dir, exist_ok=True)

# # Get a list of file names in the text folder (assuming the names match the image files)
# file_names = os.listdir(source_text_dir)

# # print(file_names)
# # input()
# # Randomly shuffle the file names using the seeded random function
# random.shuffle(file_names)

# # Calculate the split point based on an 80/20 ratio
# split_point = int(SPLIT * len(file_names))

# # Iterate through the file names and move them to train or test
# for file_name in file_names[:split_point]:
#     try:
#         shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_train_text_dir, file_name))
#         shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_train_image_dir, file_name[:-4]+".jpg"))
#     except:
#         print("Could not copy files: " + file_name)
#         continue

# for file_name in file_names[split_point:]:
#     try:
#         shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_test_text_dir, file_name))
#         shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_test_image_dir, file_name[:-4]+".jpg"))
#     except:
#         print("Could not copy files: " + file_name)
#         continue



# could provide top level dir and just append "text" or "image" to have less func parameters
def copy_train_data(source_text_dir, source_image_dir, out_train_text_dir, out_train_image_dir, file_names, split_point):
    # Iterate through the file names and move them to train
    for file_name in file_names[:split_point]:
        try:
            shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_train_text_dir, file_name))
            shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_train_image_dir, file_name[:-4]+".jpg"))
        except:
            print("Could not copy files: " + file_name)
            continue

def copy_test_data(source_text_dir, source_image_dir, out_test_text_dir, out_test_image_dir, file_names, split_point):
    for file_name in file_names[split_point:]:
        try:
            shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_test_text_dir, file_name))
            shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_test_image_dir, file_name[:-4]+".jpg"))
        except:
            print("Could not copy files: " + file_name)
            continue



def split_data_pipe(source_dir, output_dir, split, seed):
    # SPLIT = 0.8
    # TOP_PATH = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data"
    # OUTPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data"
    # Set a seed for reproducibility
    random.seed(seed)

    # Set the source directories
    source_text_dir = source_dir + "\\labels"
    source_image_dir = source_dir + "\\images"


    # Set the destination directories
    out_train_text_dir = output_dir + "\\train\\labels"
    out_train_image_dir = output_dir + "\\train\\images"
    out_test_text_dir =  output_dir + "\\test\\labels"
    out_test_image_dir = output_dir + "\\test\\images"

    os.makedirs(out_train_text_dir,exist_ok=True)
    os.makedirs(out_train_image_dir,exist_ok=True)
    os.makedirs(out_test_text_dir,exist_ok=True)
    os.makedirs(out_test_image_dir,exist_ok=True)


    # Get a list of file names in the text folder (assuming the names match the image files)
    file_names = os.listdir(source_text_dir)

    # Randomly shuffle the file names using the seeded random function
    random.shuffle(file_names)

    # Calculate the split point based on an split/1-split ratio ex: 80/20
    split_point = int(split * len(file_names))

    copy_train_data(source_text_dir, source_image_dir, out_train_text_dir, out_train_image_dir, file_names, split_point)
    copy_test_data(source_text_dir, source_image_dir, out_test_text_dir, out_test_image_dir, file_names, split_point)

    return 1
