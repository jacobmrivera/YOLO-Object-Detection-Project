

from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionTrainer
from pathlib import Path

class PredictorModel(DetectionTrainer):

    def __init__(self,) -> None:
        self.model=None


    def set_model(self, model: str|Path):
        self.model = model
        return
    
    def 
