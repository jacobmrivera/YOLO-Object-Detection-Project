from pathlib import Path
import os
from ultralytics import YOLO
import random

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

    with open(f'{input_dir}\\{base_output_name}{class_name}.txt', 'w') as file:
        for f in to_eval[:num_to_pred]:

            img = class_dir.joinpath(f)
            results = model(img)
            pred_class = results[0].probs.top1

            if pred_class == 1:
                file.write(f"{img}: {1} | {results[0].probs.top1conf.item()}\n")
                num_correct += 1
            elif pred_class == 0:
                file.write(f"{img}: {0} | {results[0].probs.top1conf.item()}\n")
                num_incorrect += 1

            print(f"{num_correct + num_incorrect} / {len(to_eval)}")

    with open(f'{input_dir}\\{base_output_name}{class_name}summary.txt', 'w') as file:
            file.write(f"Total number of images: {num_correct + num_incorrect:>15}\n")
            file.write(f"# of Correct predictions: {num_correct:>15}\n")
            file.write(f"# of Incorrect predictions: {num_incorrect:>15}\n")
            file.write(f"\nAccuracy: {(num_correct)/(num_correct+ num_incorrect):>15}")
            file.write('\n\n\n')



def main():
    model_path = Path("obj17\\train2\\weights\\best.pt")
    input_path = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_validating")
    class_name = "positive_JA"
    base_output_name = f"first_10%_"
    num_to_pred = 10_000


    predict_on_dir(model_path, input_path, class_name, base_output_name, num_to_pred)

if __name__ == "__main__":
    main()