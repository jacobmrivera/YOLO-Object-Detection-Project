import json
from training import det_train_json
from data_preprocessing import make_config as dp

from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings


json_path = "pipeline\\config.json"


def get_model_settings_dict():
    training_dict = json_config['training']
    # training_dict['imgsize'] = json_config["constants"]["W"]
    return training_dict


def train_model():
    args_dict = get_model_settings_dict()

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)

    # Train
    trainer.train()

if __name__ == '__main__':
    global json_config
    try:
        with open(json_path, 'r') as config_file:
            json_config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file.")



    dp.make_config(json_config)

    train_model()

    # print("Beginning Training...")
    # trainer.train_model()
