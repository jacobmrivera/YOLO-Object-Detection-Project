import glob
import os
import scipy.io
import shutil
from pathlib import Path
from tqdm import tqdm

IMAGES_OUT_PATH = Path(f"data\\demo_data\\images")
LABELS_OUT_PATH = Path(f"data\\demo_data\\labels")

def copy_subject_data(sub_num,):
    cnt = 0

    file_pattern = os.path.join( f"M:\\experiment_12\\included\\{sub_num}\\extra_p", '*_child_boxes.mat')
    matching_files = glob.glob(file_pattern)[0]

    subject_num = matching_files.split('\\')[-3]

    mat = scipy.io.loadmat(matching_files)
    num_rows = len(mat['box_data']['post_boxes'][0])

    for i in tqdm(range(num_rows), desc=f"Processing {subject_num}"):

        path_arr = mat['box_data']['frame_name'][0][i][0].split('/')

        subID = path_arr[-3]
        image_name = path_arr[-1]

        # print(subID, image_name)

        frame_path = f"M:\\experiment_12\\included\\{subject_num}\\cam07_frames_p\\{image_name}"

        new_frame_name = subID + "_" + image_name
        new_frame_path = IMAGES_OUT_PATH.joinpath(new_frame_name)

        shutil.copy(frame_path, new_frame_path)


        frame_data = mat['box_data']['post_boxes'][0][i]

        new_txt_name = subID + "_" + image_name.split('.')[0] + ".txt" # strip off image file ext and add txt
        new_txt_path = LABELS_OUT_PATH.joinpath(new_txt_name)
        
        mat_arr_to_txt(frame_data, new_txt_path)

    return

def mat_arr_to_txt(arr, txt_name):

    with open(txt_name, "w") as f:
        for i in range(len(arr)):
            f.write(f"{i} {arr[i][0]} {arr[i][1]} {arr[i][2]} {arr[i][3]}\n")


top_dir = Path("M:\\experiment_12\\included")
# Get all folders in the directory
folders = [folder for folder in os.listdir(top_dir) if os.path.isdir(os.path.join(top_dir, folder))]

# Filter folders that start with "__"
filtered_folders = [folder for folder in folders if folder.startswith("__")]

# print(filtered_folders[0])
for sub in filtered_folders:
    copy_subject_data(sub)
