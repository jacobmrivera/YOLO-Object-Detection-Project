
import datetime
import shutil
from pathlib import Path
from collections import Counter

import yaml
import numpy as np
import pandas as pd
from ultralytics import YOLO
from sklearn.model_selection import KFold
import torch
import gc

'''
Adapted from https://docs.ultralytics.com/guides/kfold-cross-validation/

'''

DATASET_PATH = "."
YAML_PATH = "."
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png']



def prep_labels_df(dataset_path: str, yaml_path: str, indx, cls_idx) -> pd.DataFrame:
    labels = sorted(dataset_path.rglob("*labels/*.txt")) # all data in 'labels'

    yaml_file = yaml_path  # your data YAML with data directories and names dictionary
    with open(yaml_file, 'r', encoding="utf8") as y:
        classes = yaml.safe_load(y)['names']
    cls_idx = sorted(classes.keys())


    indx = [l.stem for l in labels] # uses base filename as ID (no extension)
    labels_df = pd.DataFrame([], columns=cls_idx, index=indx)

    for label in labels:
        lbl_counter = Counter()

        with open(label,'r') as lf:
            lines = lf.readlines()

        for l in lines:
            # classes for YOLO label uses integer at first position of each line
            lbl_counter[int(l.split(' ')[0])] += 1

        labels_df.loc[label.stem] = lbl_counter.items()

    labels_df = labels_df.fillna(0.0) # replace `nan` values with `0.0`

    return labels_df



def kfold_data(dataset_path, yaml_file, ksplit=5):
    dataset_path = Path(dataset_path) # replace with 'path/to/dataset' for your custom data

    labels = sorted(dataset_path.rglob("*labels/*.txt")) # all data in 'labels'
    indx = [l.stem for l in labels] # uses base filename as ID (no extension)

    with open(yaml_file, 'r', encoding="utf8") as y:
        classes = yaml.safe_load(y)['names']
    cls_idx = sorted(classes.keys())
    
    labels_df = prep_labels_df(dataset_path, yaml_file, indx, cls_idx)


    kf = KFold(n_splits=ksplit, shuffle=True, random_state=20)   # setting random_state for repeatable results

    kfolds = list(kf.split(labels_df))


    folds = [f'split_{n}' for n in range(1, ksplit + 1)]
    folds_df = pd.DataFrame(index=indx, columns=folds)

    for idx, (train, val) in enumerate(kfolds, start=1):
        folds_df[f'split_{idx}'].loc[labels_df.iloc[train].index] = 'train'
        folds_df[f'split_{idx}'].loc[labels_df.iloc[val].index] = 'val'


    fold_lbl_distrb = pd.DataFrame(index=folds, columns=cls_idx)

    for n, (train_indices, val_indices) in enumerate(kfolds, start=1):
        train_totals = labels_df.iloc[train_indices].count()
        val_totals = labels_df.iloc[val_indices].count()

        # To avoid division by zero, we add a small value (1E-7) to the denominator
        ratio = val_totals / (train_totals + 1E-7)
        fold_lbl_distrb.loc[f'split_{n}'] = ratio

    # Initialize an empty list to store image file paths
    images = []

    # Loop through supported extensions and gather image files
    for ext in SUPPORTED_EXTENSIONS:
        images.extend(sorted((dataset_path / 'images').rglob(f"*{ext}")))

    # Create the necessary directories and dataset YAML files (unchanged)
    save_path = Path(dataset_path / f'{datetime.date.today().isoformat()}_{ksplit}-Fold_Cross-val')
    save_path.mkdir(parents=True, exist_ok=True)
    ds_yamls = []

    for split in folds_df.columns:
        # Create directories
        split_dir = save_path / split
        split_dir.mkdir(parents=True, exist_ok=True)
        (split_dir / 'train' / 'images').mkdir(parents=True, exist_ok=True)
        (split_dir / 'train' / 'labels').mkdir(parents=True, exist_ok=True)
        (split_dir / 'val' / 'images').mkdir(parents=True, exist_ok=True)
        (split_dir / 'val' / 'labels').mkdir(parents=True, exist_ok=True)

        # Create dataset YAML files
        dataset_yaml = split_dir / f'{split}_dataset.yaml'
        ds_yamls.append(dataset_yaml)

        with open(dataset_yaml, 'w') as ds_y:
            yaml.safe_dump({
                'path': split_dir.as_posix(),
                'train': 'train',
                'val': 'val',
                'names': classes
            }, ds_y)

    for image, label in zip(images, labels):
        for split, k_split in folds_df.loc[image.stem].items():
            # Destination directory
            img_to_path = save_path / split / k_split / 'images'
            lbl_to_path = save_path / split / k_split / 'labels'

            # Copy image and label files to new directory (SamefileError if file already exists)
            # print(f"img_to_path: {type(img_to_path[0])}")

            shutil.copy(image, img_to_path[0] / image.name)
            shutil.copy(label, lbl_to_path[0] / label.name)


    folds_df.to_csv(save_path / "kfold_datasplit.csv")
    fold_lbl_distrb.to_csv(save_path / "kfold_label_distribution.csv")

    return ds_yamls



def train(dataset_path, yaml_path, ksplit, weights_path, batch_size, epochs, project, device):
    ds_yamls = kfold_data(dataset_path, yaml_path, ksplit)

    # weights_path = 'path/to/weights.pt'
    model = YOLO(weights_path, task='detect')

    results = {}

    for k in range(ksplit):
        dataset_yaml = ds_yamls[k]
        model.train(data=dataset_yaml, epochs=epochs, batch=batch_size, project=project, device=device)  # include any train arguments
        results[k] = model.metrics  # save output metrics for further analysis
        torch.cuda.empty_cache()
        gc.collect()






#####################################
import os
import pandas as pd
from sklearn.model_selection import KFold

def read_yolo_dataset(dataset_path, k=5):
    # Initialize lists to store file paths
    image_paths = []
    label_paths = []
    
    # Iterate through the images directory and store file paths
    images_dir = os.path.join(dataset_path, "images")
    for root, _, files in os.walk(images_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(os.path.join(root, file))
    
    # Iterate through the labels directory and store file paths
    labels_dir = os.path.join(dataset_path, "labels")
    for root, _, files in os.walk(labels_dir):
        for file in files:
            if file.lower().endswith('.txt'):
                label_paths.append(os.path.join(root, file))
    
    # Create a DataFrame to store image and label paths
    df = pd.DataFrame({'image_path': image_paths, 'label_path': label_paths})
    
    # Initialize KFold object
    kf = KFold(n_splits=k, shuffle=True)
    
    # Split data into k folds
    fold_data = []
    for train_index, test_index in kf.split(df):
        train_data = df.iloc[train_index]
        test_data = df.iloc[test_index]
        fold_data.append((train_data, test_data))
    
    return fold_data

# Example usage:
dataset_path = "path/to/your/yolo_dataset"
k = 5
fold_data = read_yolo_dataset(dataset_path, k)

# Access each fold's train and test data
for i, (train_data, test_data) in enumerate(fold_data):
    print(f"Fold {i+1}:")
    print("Train data:")
    print(train_data.head())
    print("Test data:")
    print(test_data.head())
    print("=" * 50)
