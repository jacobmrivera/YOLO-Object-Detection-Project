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
