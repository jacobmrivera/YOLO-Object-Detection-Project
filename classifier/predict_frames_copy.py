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
model_path = Path("obj17\\train2\\weights\\best.pt")
# frames_path = Path("C:\\Users\\multimaster\\Desktop\\JA_DATASET\\exp12_child_datasets\\17358_set_aside\\17358\\positive_JA") # will be different


N = "10%"
# "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_testing"
output_path = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_validating")

base_output_name = f"first_{N}_"

positive_dir = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_validating\\positive_JA") # will be different

negative_dir = Path(f"C:\\Users\\multimaster\\Desktop\\JA_DATASET\\csvs\\JA_child-view\\exp12_obj_17_split_data\\first_10%_split\\for_validating\\negative_JA") # will be different

num_to_pred = 10_000

def main():
    model = YOLO(model_path)  # load a custom model
    random.seed(32)

    # all_positive_frames = os.listdir(positive_dir)
    # positive_trained = os.listdir(postitive_train) + os.listdir(postitive_test)
    
    # positive_to_eval = list(set(all_positive_frames) - set(positive_trained))
    positive_to_eval = os.listdir(positive_dir)
    random.shuffle(positive_to_eval)
    pos_correct_cnt = 0
    pos_incorrect_cnt = 0
    # results = model(positive_dir.joinpath(positive_to_eval[0]))
    # print(results[0].probs.top1)
    # print(results[0].probs.top1conf.item())
    with open(f'{output_path}\\{base_output_name}positive_predictions.txt', 'w') as file:
        # for f in positive_to_eval[:num_to_pred]:
        for f in positive_to_eval:

            img = positive_dir.joinpath(f)
            results = model(img)
            pred_class = results[0].probs.top1

            if pred_class == 1:
                file.write(f"{img}: {1} | {results[0].probs.top1conf.item()}\n")
                pos_correct_cnt += 1
            elif pred_class == 0:
                file.write(f"{img}: {0} | {results[0].probs.top1conf.item()}\n")
                pos_incorrect_cnt += 1

            print(f"{pos_correct_cnt + pos_incorrect_cnt} / {len(positive_to_eval)}")

#####################################################
    negative_to_eval = os.listdir(negative_dir)
    random.shuffle(negative_to_eval)

    neg_correct_cnt = 0
    neg_incorrect_cnt = 0
    with open(f'{output_path}\\{base_output_name}negative_predictions.txt', 'w') as file:
        # for f in negative_to_eval[:num_to_pred]:
        for f in negative_to_eval:
            img = negative_dir.joinpath(f)
            results = model(img)
            pred_class = results[0].probs.top1

            if pred_class == 0:
                file.write(f"{img}: {1} | {results[0].probs.top1conf.item()}\n")
                neg_correct_cnt += 1
            elif pred_class == 1:
                file.write(f"{img}: {0} | {results[0].probs.top1conf.item()}\n")
                neg_incorrect_cnt += 1

            print(f"{neg_correct_cnt + neg_incorrect_cnt} / {len(negative_to_eval)}")



    with open(f'{output_path}\\{base_output_name}summary.txt', 'w') as file:
        file.write(f"Total number of pos images: {pos_correct_cnt + pos_incorrect_cnt:>10}\n")
        file.write(f"# of Correct positive predictions: {pos_correct_cnt:>10}\n")
        file.write(f"# of Incorrect positive predictions: {pos_incorrect_cnt:>10}\n")
        file.write(f"\nPositive Accuracy: {(pos_correct_cnt)/(pos_correct_cnt+ pos_incorrect_cnt):>10}")
        file.write('\n\n\n')

        file.write(f"Total number of neg images: {neg_correct_cnt + neg_incorrect_cnt:>10}\n")
        file.write(f"# of Correct negative predictions: {neg_correct_cnt:>10}\n")
        file.write(f"# of Incorrect negative predictions: {neg_incorrect_cnt:>10}\n")
        file.write(f"\nNegative Accuracy: {(neg_correct_cnt)/(neg_correct_cnt+ neg_incorrect_cnt):>10}")
        




if __name__ == "__main__":
    main()