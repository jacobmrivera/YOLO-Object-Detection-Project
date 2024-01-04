import cv2
import os

# INPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data\\images"
# OUTPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23"

INPUT_DIR_PRE = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\obj_level_data"
OUTPUT_DIR_PRE = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\obj_level_data"
# NUM_OBJ = 27

# THRESHOLD = 50



def detect_blur(image_path, threshold=100):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(img_gray, cv2.CV_64F).var()

    return variance


