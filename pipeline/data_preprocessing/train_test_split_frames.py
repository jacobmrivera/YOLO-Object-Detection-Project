import os
import random
import shutil

from make_dataset import *

def train_test_split_frames(dataset_folder, labels_folder,image_folder,split):
    os.makedirs(dataset_folder, exist_ok=True)

    file_names = os.listdir(labels_folder)
    
    random.shuffle(file_names)
    split_point = int(split * len(file_names))

    train_test_labels = [file_names[:split_point],file_names[split_point:]]


    print(train_test_labels)
    label_type = {0:'train',1:'test'}
    
    for i, labels in enumerate(train_test_labels):
        sub_dataset_folder = f'{dataset_folder}\\{label_type[i]}'
        print(i)
        make_dataset(labels, image_folder, sub_dataset_folder)
