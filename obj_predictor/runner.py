import json
import training
from data_preprocessing import make_config as dp
from data_preprocessing import train_test_split_frames

from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings
from obj_predictor.predicting import predicting_videos

json_path = "pipeline\\config.json"


'''

input_dir/
    ├── images/
    │   ├── file1.jpg
    │   └── file2.jpg
    └── labels/
        ├── file1.txt
        └── file2.txt

data_output_dir/
    ├── train/
    |   ├── images/
    |   |   ├── file1.jpg
    |   │   └── file2.jpg
    |   └── labels/
    |       ├── file1.txt
    |       └── file2.txt
    └── test/
        ├── images/
        |   ├── file1.jpg
        │   └── file2.jpg
        └── labels/
            ├── file1.txt
            └── file2.txt
├
|
─

'''

def main():
    global json_config
    try:
        with open(json_path, 'r') as config_file:
            json_config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file.")

    # starting from a directory, with two subdirs
    dp.make_config(json_config)

    train_test_split_frames.split_data_pipe(source_dir=json_config['dataset_folder'], output_dir=json_config['dataset_folder'], split=json_config['split'], seed=json_config['constants']['SEED'])

    training.train.train_model(json_config)

    # print("Beginning Training...")
    # train_model()

    predicting_videos.predict_vid(json_config)


if __name__ == '__main__':
    main()