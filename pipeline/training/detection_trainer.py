import argparse
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics import settings


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Object Detection Script')
    parser.add_argument('--config_path', type=str, help='Path to the config.yaml file')
    parser.add_argument('--model', type=str, help='Name of YOLO model to train', required=True)
    parser.add_argument('--epochs', type=int, help='Max number of epochs to train', required=True)


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








# import argparse
# from ultralytics.models.yolo.detect import DetectionTrainer

# if __name__ == '__main__':
#     # Create an argument parser
#     parser = argparse.ArgumentParser(description='Object Detection Script')

#     # Add an argument for the config_path
#     parser.add_argument('--config_path', type=str, help='Path to the config.yaml file')

#     # Parse the command-line arguments
#     args = parser.parse_args()

#     if args.config_path:
#         # Use the provided config_path
#         config_path = args.config_path
#     else:
#         # If config_path is not provided, use a default value
#         config_path = "C:\\Users\\multimaster\\Documents\\Object_Detection\\yolo_project\\config.yaml"

#     # Define other arguments
#     model = 'yolov8s.pt'
#     epochs = 600
#     device = 0

#     # Create a dictionary with the arguments
#     args_dict = dict(model=model, data=config_path, epochs=epochs, device=device)

#     # Initialize the trainer
#     trainer = DetectionTrainer(overrides=args_dict)

#     # Start training
#     trainer.train()
