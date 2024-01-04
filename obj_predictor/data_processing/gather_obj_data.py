import os
import shutil


INPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data_corrected"
OUTPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\obj_level_data"
NUM_OBJ = 27


os.makedirs(OUTPUT_DIR, exist_ok=True)

obj_labels_dict = {}

# instantiate key for each obj in dict
for i in range(NUM_OBJ):
    obj_labels_dict[str(i)] = []

# make a dir for each obj
for i in range(NUM_OBJ):
    obj_dir = os.path.join(OUTPUT_DIR, str(i))
    os.makedirs(obj_dir, exist_ok=True)


source_labels_dir = os.path.join(INPUT_DIR, "labels")
source_images_dir = os.path.join(INPUT_DIR, "images")

 # Get a list of file names in the text folder (assuming the names match the image files)
file_name_list = os.listdir(source_labels_dir)

########################
# def process_labels_file

file_name = file_name_list[0]

for file_name in file_name_list:
    print(file_name)
    if file_name[-4:] != ".txt":
        continue
    

    # gete full path to be able to copy files later
    full_file_path = os.path.join(source_labels_dir, file_name)

    # Open the file in read mode
    with open(full_file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # print(line)
            if line == " " or line=="":
                continue
            line = line.strip() # remove \n
            line_arr = line.split(' ')

            obj_num = str(line_arr[0])
            
            print(obj_num)
            # add label file and line to obj dict array
            obj_labels_dict[obj_num].append([file_name, line])

            # create path to put image
            out_obj_dir = os.path.join(OUTPUT_DIR, str(obj_num))
            # copy image file over
            shutil.copy2(os.path.join(source_images_dir, file_name[:-4]+".jpg"), os.path.join(out_obj_dir, file_name[:-4]+".jpg"))

            
for i in range(NUM_OBJ):
    obj_dir = os.path.join(OUTPUT_DIR, str(i), 'all_labels.txt')

    obj_dict_entry = obj_labels_dict[str(i)]

    with open(obj_dir, 'w') as file:
        for line in obj_dict_entry:
            file.write(line[0] + " " + line[1] + "\n")

