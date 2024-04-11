# Import necessary modules or scripts
from obj_detector.data import DataMaster



'''
Created by Jacob Rivera
Spring 2024

Last edit: 04/10/2024

Description:
    Provide a blur value of a single image by the Laplacian Operator

    Values closer to 0 are considered blurry, while higher values are considered sharper

    The value should be used as a hueristic to gather insight about the images,
    not as a definitive test of blurryness. 
    
    INPUT_IMG:
        path to .pt file to predict with


'''

INPUT_IMG = "C:\\Users\\multimaster\\Desktop\\data_to_train_on\\all_annotations_2_14_24_with_mirrored\\images\\00_20221112_10041_frame27265.jpg"

def main():

    blur_val = DataMaster.get_blur_level(INPUT_IMG)
    print(f"Blur value of {INPUT_IMG}: {blur_val}")
    return

if __name__ == "__main__":
    main()