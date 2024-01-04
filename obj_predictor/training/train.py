import argparse
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings
import json


def get_model_settings_dict(json_config):
    training_dict = json_config['training']
    return training_dict


def train_model(json_config):
    args_dict = get_model_settings_dict(json_config)

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)

    # Train
    trainer.train()