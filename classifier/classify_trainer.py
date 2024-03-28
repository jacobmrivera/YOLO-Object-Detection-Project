from pathlib import Path
from typing import Dict, Any
from data import DataMaster
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionTrainer

class ClassifyTrainer():
    def __init__(self, args: dict[str, Any], dataset_path, class_dict: dict[int, str] = None):
        self.model_path = args['model'] if 'model' in args else 'yolov8s.pt'
        self.args = args
        self.dataset_path = dataset_path
        self.seed = 32
        self.dataMaster = DataMaster(self.dataset_path, self.seed, class_dict)
        
        # self.model = DetectionTrainer(overrides=self.args)

    def load_model(self):
        # Ensure the model is in the passed aruements
        self.model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)        return     



    def train(self, show_output: bool = True):
        self.save_path = self.dataMaster.split_data_pipe()
        
        print("Beginning training...")
        self.model.train(verbose=show_output)

    def split_data(self):
        positive_path = ""
        all_path = ""


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


dataset_path = "C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored"

trainerClass = Trainer(args_dict, dataset_path, obj_dict)
trainerClass.train()



