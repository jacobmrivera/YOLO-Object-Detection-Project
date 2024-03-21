from pathlib import Path
from typing import Dict, Any
from data import DataMaster
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionTrainer

class Trainer():
    def __init__(self, model_path: str|Path, args: dict[str, Any], dataset_path, class_dict: dict[int, str] = None):
        self.model_path = model_path
        self.args = args
        self.dataset_path = dataset_path
        self.model = self.load_model(model_path=self.model_path)

        self.seed = 32

        self.dataMaster = data.DataMaster()

    def load_model(self, model_path: str|Path = None):
        # if path to a pretrained model not provided, uses default size s model
        if model_path == None:
            print("No model path provided, using default model path: ")
            self.model_path = "yolov8s.pt"
        else:
            self.model_path = model_path

        self.args["model"] =  self.model_path
        return DetectionTrainer(overrides=self.args)


    def train(self, show_output: bool = True):
        # Need to check if the data has been split into train/val



        # Need to check if there is a yaml file for the data


        print("Begining training...")
        self.model.train(verbose=show_output)

    def k_fold_train(self, k: int = 5, show_output: bool = True):
        print(f"Begining {k}-fold training...")
        self.model.kfold_train(k=k, verbose=show_output)



'''


model = BaseModel()

'''