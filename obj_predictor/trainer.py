from pathlib import Path
from typing import Dict, Any
from data import DataMaster
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionTrainer

class Trainer():
    def __init__(self, args: dict[str, Any], dataset_path, class_dict: dict[int, str] = None):
        self.model_path = args['model'] if 'model' in args else 'yolov8s.pt'
        self.args = args
        self.dataset_path = dataset_path
        self.seed = 32
        self.dataMaster = DataMaster(self.dataset_path, self.seed, class_dict)
        
        # self.model = DetectionTrainer(overrides=self.args)

    def load_model(self):
        # Ensure the model is in the passed aruements
        self.args["model"] =  self.model_path
        trainer = DetectionTrainer(overrides=self.args)
        return     

    def get_yaml(self):
        self.yaml = self.dataMaster.yaml
        self.args['data'] = self.yaml

    def train(self, show_output: bool = True):
        self.save_path = self.dataMaster.split_data_pipe()
        self.get_yaml(self)
        
        print("Beginning training...")
        self.model.train(verbose=show_output)


    def k_fold_train(self, k: int = 5, show_output: bool = True):
        print(f"Beginning {k}-fold training...")
        self.model.kfold_train(k=k, verbose=show_output)



'''


model = BaseModel()

'''
args_dict = {
    "model": 'yolov8s.pt',
    "epochs": 50,
    "device": 0,
    "project": "testertester",
    "name": "1"
}

obj_dict = {
    0: "kettle",
    1: "cat",
    2: "potato",
    3: "firetruck",
    4: "bulldozer",
    5: "car",
    6: "ostrich",
    7: "frog",
    8: "truck",
    9: "lobster",
    10: "carrot",
    11: "colander",
    12: "motorcycle",
    13: "cup",
    14: "dog",
    15: "elephant",
    16: "spaceship",
    17: "pineapple",
    18: "banana",
    19: "submarine",
    20: "boat",
    21: "cookie",
    22: "stingray",
    23: "fork",
    24: "helicopter",
    25: "duck",
    26: "bee"
}

dataset_path = "C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored"

trainerClass = Trainer(args_dict, dataset_path, obj_dict)
trainerClass.train()



