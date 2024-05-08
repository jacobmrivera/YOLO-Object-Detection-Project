from pathlib import Path
import os
from ultralytics import YOLO
import random
from tqdm import tqdm
'''
Created by Jacob Rivera
Spring 2024

Last edit: 03/28/2024

Description:
    Predict objects in a directory of images (or frames from a video)

    in a terminal or command prompt, run the following commands from the top level of this project

    ! MAC/LINUX
    $ source venv/bin/activate

    ! WINDOWS   
    $ source venv\\Scripts\\activate

    python examples/predict_frames.py

    deactivate
    ~~~~~~~~~~~~~~
'''

# "C:\Users\multimaster\Desktop\JA_DATASET\csvs\JA_child-view\exp12_obj_17_split_data\first_10%_split\for_testing\negative_JA"
def predict_on_dir(model_path, input_dir:Path, class_name, base_output_name, num_to_pred=None):

    model = YOLO(model_path)  # load a custom model
    random.seed(32)

    class_dir = input_dir.joinpath(class_name)

    to_eval = os.listdir(class_dir)
    random.shuffle(to_eval)

    if num_to_pred is None:
         num_to_pred = len(to_eval)
    num_correct = 0
    num_incorrect = 0

    class_num = None

    with open(f'{input_dir}\\{base_output_name}_{class_name}.txt', 'w') as file:

        for f in tqdm(to_eval[:num_to_pred], desc="Predicting..."):
            if f[-2:] == "db":
                continue
            img = class_dir.joinpath(f)
            results = model(img, verbose=False)
            # print(results[0].probs)
            pred_class = results[0].probs.top1

            if class_num is None:
                 
                model_dict = results[0].names
                for key, val in model_dict.items():
                    if val == class_name:
                        class_num = key  
            # print(f"predicted_class: {pred_class}")
            # print(f"class_num: {class_num}")
            # input()
            if pred_class == class_num:
                file.write(f"{img}: {1:>6} | {results[0].probs.top1conf.item()}\n")
                num_correct += 1
            else:
                file.write(f"{img}: {0:>6} | {results[0].probs.top1conf.item()}\n")
                num_incorrect += 1

            # print(f"{num_correct + num_incorrect} / {num_to_pred}")
            # input()

    with open(f'{input_dir}\\{base_output_name}_{class_name}.txt', 'r') as f:
        existing_content = f.read()



    with open(f'{input_dir}\\{base_output_name}_{class_name}.txt', 'w') as file:
            file.write(f"Total number of images: {num_correct + num_incorrect:>15}\n")
            file.write(f"# of Correct predictions: {num_correct:>15}\n")
            file.write(f"# of Incorrect predictions: {num_incorrect:>15}\n")
            file.write(f"\nAccuracy: {(num_correct)/(num_correct + num_incorrect):>15}")
            file.write(f"")

            file.write('\n\n\n')
            file.write(existing_content)

N = 500
def main():
    model_path = Path(f"obj17\\first_{N}\\weights\\best.pt")
    # input_path = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_validating")
    input_path = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\newer_csvs\\exp12_JA_obj17_data_child-view\\first_{N}_split\\validating_split")
    # input_path = Path("Z:\\elton\\val")
    base_output_name = f"first_{N}_obj17_trained"
    num_to_pred = 5_000

    # class_name = "positive_JA"
    # predict_on_dir(model_path, input_path, class_name, base_output_name, num_to_pred)


    class_name = "negative_JA"
    predict_on_dir(model_path, input_path, class_name, base_output_name, num_to_pred)





if __name__ == "__main__":
    main()