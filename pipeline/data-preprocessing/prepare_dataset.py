from train_test_split_frames  import *
from make_dataset import *


dataset_folder = "test_dataset"
labels_folder = "C:\\Users\\multimaster\\Desktop\\formated_data_set_103123\\1\\obj_train_data\\frames\\1"
images_folder =  "C:\\Users\\multimaster\\Desktop\\1"
split = 80

print(f'why is this not working \n {dataset_folder}')

make_dataset(labels_folder, images_folder, dataset_folder)
