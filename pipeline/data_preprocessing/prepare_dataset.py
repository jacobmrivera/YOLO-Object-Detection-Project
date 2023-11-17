from train_test_split_frames  import *
from make_dataset import *


dataset_folder = "test_split_dataset"
labels_folder = "C:\\Users\\multimaster\\Desktop\\formated_data_set_103123\\1\\obj_train_data\\frames"
images_folder =  "C:\\Users\\multimaster\\Desktop\\img_test"
split = 80


train_test_split_frames(dataset_folder, labels_folder, dataset_folder,split)
