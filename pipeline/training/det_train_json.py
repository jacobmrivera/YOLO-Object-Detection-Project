import argparse
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings
import json



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Object Detection Script')
    parser.add_argument('--jsonConfigPath', type=str, help='Path to the config.json file', required=True)

    global config
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading config file. Using default settings.")

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.config_path:
        # Use the provided config_path
        config_path = args.config_path
    else:
        # If config_path is not provided, use a default value
        config_path = "C:\\Users\\multimaster\\Documents\\Object_Detection\\yolo_project\\config.yaml"

    model = args.model
    epochs = args.epochs
    # Define other arguments
    device = 0

    # Create a dictionary with the arguments
    args_dict = dict(model=model, data=config_path, epochs=epochs, device=device)

    # Initialize the trainer
    trainer = DetectionTrainer(overrides=args_dict)
    trainer.train()

