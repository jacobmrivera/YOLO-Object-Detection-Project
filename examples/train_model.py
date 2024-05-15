import obj_detector.constants as constants
from pathlib import Path
from obj_detector.trainer import Trainer  # Importing the PredictorModel class from your predictor module

'''
Created by Jacob Rivera
Spring 2024

Last edit: 4/2/2024

Description:
    Train YOLO model from passed aruements

    model_path: 
        model to train. 
        if continuing to train a model, path should be to the .pt file
    
    dataset_path:
        path to the top level directory of your dataset
        in the visual below, I would pass the pat to "input_dir"
        
        dataset_path/
            ├── images/
            │   ├── file1.jpg
            │   ├── file2.jpg
            │   ├── file3.jpg
            │   └── file4.jpg
            └── labels/
                ├── file1.txt
                ├── file2.txt
                ├── file3.txt
                └── file4.txt

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
                |   ├── file3.jpg
                │   └── file4.jpg
                └── labels/
                    ├── file3.txt
                    └── file4.txt

    class_dict:
        a python dictionary containing {int:"class_label"} pairs
        the ints must start from 0 and each label should be unique
        a dict can be passed in or set in the constants file

'''


model_path = Path("yolov8s.pt")
dataset_path = Path("data\\exp12_training_data")
class_dict = constants.CLASSES_DICT

project_name = "exp12_attempt" # name of the project for various trainings, example: "experiment_12"
training_run_name = "run" # name of individual training for a project, example: "train1"

def main():

    args_dict = {
        "model": model_path,
        "epochs": 1000,
        "device": 0, # set to 'cpu' or delete if no GPU
        "project": project_name,
        "name": training_run_name,
    }


    trainer = Trainer(args=args_dict, dataset_path=dataset_path, class_dict=class_dict)
    trainer.train(show_output=True, data_split=True)
    
    return



if __name__ == "__main__":
    main()