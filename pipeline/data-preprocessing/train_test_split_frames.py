import os
import random
import shutil

from make_dataset import *

def train_test_split_frames(dataset_folder, labels_folder,image_folder,split):
    os.makedirs(dataset_folder, exist_ok=True)

    file_names = os.listdir(labels_folder)
    
    random.shuffle(file_names)
    split_point = int(split * len(file_names))

    train_test_labels = [split_point[:split_point],split_point[split_point:]]
    label_type = {0:'train',1:'test'}
    
    for i, labels in enumerate(train_test_labels):
        sub_dataset_folder = f'{dataset_folder}\\{label_type[i]}'

        make_dataset(labels, image_folder, sub_dataset_folder)
