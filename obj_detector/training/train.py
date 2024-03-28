import argparse
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings
import json


def get_model_settings_dict(json_config):
    training_dict = json_config['training']
    return training_dict


def train_model_json(json_config):
    args_dict = get_model_settings_dict(json_config)

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)

    # Train
    trainer.train()


def train_model(model, device, data, project, name, epochs=1000):
    args_dict = {
        "model": model,
        "epochs": epochs,
        "device": device,
        "data": data,
        "project": project,
        "name": name
    }

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)

    # Train
    trainer.train()