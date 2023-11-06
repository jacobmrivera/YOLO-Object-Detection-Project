import json
from training import det_train_json as trainer
from data_preprocessing import make_config as dp

json_path = "pipeline\\config.json"


global json_config
try:
    with open(json_path, 'r') as config_file:
        json_config = json.load(config_file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Error reading config file.")




dp.make_config()

# print("Beginning Training...")
# trainer.train_model()
