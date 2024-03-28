import obj_detector.constants as constants
from pathlib import Path
from obj_detector.trainer import Trainer  # Importing the PredictorModel class from your predictor module

'''
Created by Jacob Rivera
Spring 2024

Last edit: 03/28/2024

Description:
    Train YOLO model from passed aruements

    model_path: 
        model to train. 
        if continuing to train a model, path should be to the .pt file
    
    dataset_path:
        path to the top level directory of your dataset
        in the visual below, I would pass the pat to "input_dir"
        
        input_dir/
            ├── images/
            │   ├── file1.jpg
            │   └── file2.jpg
            └── labels/
                ├── file1.txt
                └── file2.txt
'''


model_path = Path("yolov8s.pt")
dataset_path = Path(".")
class_dict = constants.CLASSES_DICT

def main():

    args_dict = {
        "model": model_path,
        "epochs": 1000,
        "device": 0,
        "project_name": "All_Data_Trainings",
        "run_name": "run1",
    }


    trainer = Trainer(args=args_dict, dataset_path=dataset_path, class_dict=class_dict)
    trainer.train(show_output=True)
    
    return



if __name__ == "__main__":
    main()