import argparse
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings
import json
import runner

def get_model_settings_dict():
    training_dict = runner.json_config['training']
    training_dict['imgsize'] = runner.json_config["constants"]["W"]
    return training_dict


def train_model():
    args_dict = get_model_settings_dict()

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)

    # Train
    trainer.train()
    
