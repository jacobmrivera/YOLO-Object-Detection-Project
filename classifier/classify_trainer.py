
from multiprocessing import freeze_support
from ultralytics import YOLO
import torch
import gc
# class ClassifyTrainer():
#     def __init__(self, args: dict[str, Any], dataset_path, class_dict: dict[int, str] = None):
#         self.model_path = args['model'] if 'model' in args else 'yolov8s.pt'
#         self.args = args
#         self.dataset_path = dataset_path
#         self.seed = 32
#         self.dataMaster = DataMaster(self.dataset_path, self.seed, class_dict)
        
#         # self.model = DetectionTrainer(overrides=self.args)

#     def load_model(self):
#         # Ensure the model is in the passed aruements
#         self.model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)        return     



#     def train(self, show_output: bool = True):
#         self.save_path = self.dataMaster.split_data_pipe()
        
#         print("Beginning training...")
#         self.model.train(verbose=show_output)

#     def split_data(self):
#         positive_path = ""
#         all_path = ""



args_dict = {
    "model": 'yolov8s.pt',
    "epochs": 100,
    "device": 0,
    "project": "obj17",
    "name": "25k"
}


def main():
    dataset_path = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_model"
    model = YOLO('yolov8s-cls.pt')  # load a pretrained model (recommended for training)
    results = model.train(data=dataset_path, epochs=50, device=0, project="obj17")
    # torch.cuda.empty_cache()
    # gc.collect()

    # dataset_path = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\exp12_child_datasets\\17358_set_aside\\50k"
    # model = YOLO('yolov8s-cls.pt')  # load a pretrained model (recommended for training)
    # results = model.train(data=dataset_path, epochs=100, device=0, project="17358_set_aside")
    # torch.cuda.empty_cache()
    # gc.collect()

    # dataset_path = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\exp12_child_datasets\\17358_set_aside\\100k"
    # model = YOLO('yolov8s-cls.pt')  # load a pretrained model (recommended for training)
    # results = model.train(data=dataset_path, epochs=100, device=0, project="17358_set_aside")
    # torch.cuda.empty_cache()
    # gc.collect()


if __name__ == '__main__':
    
    freeze_support()
    main()