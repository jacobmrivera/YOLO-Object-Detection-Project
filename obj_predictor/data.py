import os
import random
import re
import shutil
from pathlib import Path
import datetime
from tqdm import tqdm
import yaml
from PIL import Image, ImageOps
import PIL


SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png']


class DataMaster():
    def __init__(self, dataset_path, seed: int, class_dict, save_path=None) -> None:
        self.dataset_path = Path(dataset_path)
        self.seed = seed
        self.class_dict = class_dict
        self.save_path = save_path if save_path is not None else Path(self.dataset_path / f'{datetime.date.today().isoformat()}_Training-data')

    def split_data_pipe(self, split=0.8):
        # Set a seed for reproducibility
        random.seed(self.seed)

        labels = sorted(self.dataset_path.rglob("*labels/*.txt")) # all data in 'labels'

        # Initialize an empty list to store image file paths
        images = []
            # Loop through supported extensions and gather image files
        for ext in SUPPORTED_EXTENSIONS:
            images.extend(sorted((self.dataset_path / 'images').rglob(f"*{ext}")))

        # save_path = Path(self.dataset_path / f'{datetime.date.today().isoformat()}_Split-data')
        self.save_path.mkdir(parents=True, exist_ok=True)

        (self.save_path / 'train' / 'images').mkdir(parents=True, exist_ok=True)
        (self.save_path / 'train' / 'labels').mkdir(parents=True, exist_ok=True)
        (self.save_path / 'val' / 'images').mkdir(parents=True, exist_ok=True)
        (self.save_path / 'val' / 'labels').mkdir(parents=True, exist_ok=True)


        # Create dataset YAML files
        dataset_yaml = self.save_path / 'dataset.yaml'
        with open(dataset_yaml, 'w') as ds_y:
            yaml.safe_dump({
                'path': self.save_path.as_posix(),
                'train': 'train',
                'val': 'val',
                'names': self.class_dict
            }, ds_y)

        self.yaml = dataset_yaml

        # Randomly shuffle the file names using the seeded random function
        random.shuffle(images)
        # Calculate the split point based on an split/1-split ratio ex: 80/20
        split_point = int(split * len(images))

        img_to_path = self.save_path / 'images'
        lbl_to_path = self.save_path / 'labels'

        # copy train split
        for img in images[:split_point]:
            try:
                shutil.copy(self.dataset_path / 'images' / img, self.save_path / 'train' / 'images' / img)
                shutil.copy(self.dataset_path / 'labels' / img[:-4]+".txt", self.save_path / 'train' / 'labels' / img[:-4]+".txt")
            except:
                print("Could not copy files: " + img)
                continue

        # copy test split
        for img in images[split_point:]:
            try:
                shutil.copy(self.dataset_path / 'images' / img, self.save_path / 'val' / 'images' / img)
                shutil.copy(self.dataset_path / 'labels' / img[:-4]+".txt", self.save_path / 'val' / 'labels' / img[:-4]+".txt")
            except:
                print("Could not copy files: " + img)
                continue


        for image, label in zip(images, labels):
            # Destination directory
            img_to_path = self.save_path / 'images'
            lbl_to_path = self.save_path / 'labels'

            print(f"image: {image}")
            print(f"img_to_path: {img_to_path}")
            print(f"image.name: {image.name}")

            # Copy image and label files to new directory (SamefileError if file already exists)
            try:
                shutil.copy( img_to_path / image.name, image)
            except shutil.SameFileError:
                pass
            
            try:
                shutil.copy(label, lbl_to_path / label.name)
            except shutil.SameFileError:
                pass

        return self.save_path
    

    # Sorting function to handle file names with integers 
    # without, sorts like 1, 10, 100, 1000, 1001
    def natural_sort_key(self, filename):
        # Split the filename into parts of digits and non-digits
        parts = [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', filename)]
        return parts


    # Returns a list of all files with a particular ending from a dir
    def list_files_in_directory(self, directory_path, ending):
        try:
            # Get all files in the directory
            files = os.listdir(directory_path)

            # Filter the list to include only text files (files with a ".txt" extension)
            filtered_files = [file for file in files if file.lower().endswith(ending)]

            # Sort the list of files alphabetically
            sorted_files = sorted(filtered_files, key=self.natural_sort_key)

            return sorted_files
        
        except OSError as e:
            print(f"Error: {e}")
            return []

    
    def generate_mirror_vars(self, put_back:bool = True):
        
        # if user wants mirrored data to not be put with dataset
        if not put_back:
            save_path = self.save_path / 'mirrored'
        else:
            save_path = self.save_path

        os.makedirs(save_path, exist_ok=True)

        save_path_images = save_path / 'images'
        save_path_labels = save_path / 'labels'

        (save_path_images).mkdir(parents=True, exist_ok=True)
        (save_path_labels).mkdir(parents=True, exist_ok=True)

        images = self.list_files_in_directory(self.dataset_path / 'images',)

        for img in tqdm(images, desc="Processing images"):

            img_name = os.path.basename(img)
            text_name = os.path.splitext(img_name)[0] + ".txt"

            lbl = os.path.join(self.dataset_path / 'labels', text_name)

            # Split the filename and extension
            img_name_root, img_ext = os.path.splitext(img_name)
            lbl_name_root, lbl_ext = os.path.splitext(img_name)


            ############### x ################
            img_name_x = Path(img_name_root + "_mirror_acr_x.jpg")
            lbl_name_x = Path(lbl_name_root + "_mirror_acr_x.txt")

            self.mirror_image_x(img, save_path_images / img_name_x)
            self.process_text_file(lbl, save_path_labels / lbl_name_x, 'x')
            

            ############### y ################
            img_name_y = Path(img_name_root + "_mirror_acr_y.jpg")
            lbl_name_y = Path(lbl_name_root + "_mirror_acr_y.txt")
            
            self.mirror_image_y(img, save_path_images / img_name_y)
            self.process_text_file(lbl, save_path_labels / lbl_name_y, 'y')

            ############### xy ###############
            img_name_xy = Path(img_name_root + "_mirror_acr_xy.jpg")
            lbl_name_xy = Path(lbl_name_root + "_mirror_acr_xy.txt")
            
            self.mirror_image_xy(img, save_path_images / img_name_xy)
            self.process_text_file(lbl, save_path_labels / lbl_name_xy, 'xy')


    def mirror_image_x(self, input_image_path, output_image_path):
        try:
            # Open the image file
            with Image.open(input_image_path) as img:
                # Flip the image vertically
                flipped_img = ImageOps.flip(img)

                # Create the output directory if it does not exist
                output_img_dir = os.path.dirname(output_image_path)

                if not os.path.exists(output_img_dir):
                    os.makedirs(output_img_dir)

                # Save the flipped image
                flipped_img.save(output_image_path)
                # if DB: print(f"Flipped image saved as {output_image_path}")
        except IOError:
            print("Unable to load image")

    def mirror_image_y(input_image_path, output_image_path):
        try:
            # Open the image file
            with Image.open(input_image_path) as img:
                # Flip the image horizontally using mirror
                flipped_img = ImageOps.mirror(img)

                # Create the output directory if it does not exist
                output_img_dir = os.path.dirname(output_image_path)

                if not os.path.exists(output_img_dir):
                    os.makedirs(output_img_dir)

                # Save the flipped image
                flipped_img.save(output_image_path)
                # if DB: print(f"Flipped image saved as {output_image_path}")
        except IOError:
            print("Unable to load image")


    def mirror_image_xy(input_image_path, output_image_path):
        try:
            # Open the image file
            with Image.open(input_image_path) as img:
                # Flip the image horizontally using mirror
                # flipped_img = ImageOps.flip(img)
                out = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
                out = out.transpose(PIL.Image.FLIP_TOP_BOTTOM)

                # mirrored_img = ImageOps.mirror(flipped_img)
                
                # Save the flipped image
                out.save(output_image_path)
                # if DB: print(f"Flipped and mirrored image saved as {output_image_path}")
        except IOError:
            print("Unable to load image")

    def mirror_bounding_box_x_axis(bb_array):
        return [bb_array[0], 1 - bb_array[1], bb_array[2], bb_array[3]]
    
    def mirror_bounding_box_y_axis(bb_array):
        return [1 - bb_array[0], bb_array[1], bb_array[2], bb_array[3]]

    def mirror_bounding_box_xy(bb_array):
        return [1 - bb_array[0], 1 - bb_array[1], bb_array[2], bb_array[3]]


    # transform each line of annotation text file
    def process_text_file(self, input_file, output_file, direction):
        # Read content from the input file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # iterate over lines from input text file
        for i in range(len(lines)):
            curr_line = lines[i].rstrip('\n')
            curr_line_arr = curr_line.split(' ')
            curr_line_arr[1:] = [float(x) for x in curr_line_arr[1:]]

            if len(curr_line_arr) < 2: 
                continue

            # might be a problem with indexing to avoid the obj number (first element)
            if direction == 'y':
                bb_array = self.mirror_bounding_box_y_axis(curr_line_arr[1:])
            elif direction == 'x':
                bb_array = self.mirror_bounding_box_x_axis(curr_line_arr[1:])
            elif direction == 'xy':
                bb_array = self.mirror_bounding_box_xy(curr_line_arr[1:])
            # recreate string to write to output file
            lines[i] = f"{curr_line_arr[0]} {bb_array[0]} {bb_array[1]} {bb_array[2]} {bb_array[3]}\n"

            # Create the output directory if it does not exist
            output_txt_dir = os.path.dirname(output_file)

            if not os.path.exists(output_txt_dir):
                os.makedirs(output_txt_dir)

            # Write the modified content to the output file
            # print(f"output txt file: {output_file}")
            with open(output_file, 'w') as outfile:
                outfile.writelines(lines)

        return




    # splits data into multiple folds for cross validation training
    def kfold_data(source_dir, output_dir, k, seed):
        random.seed(seed)

        # Set the source directories
        source_text_dir = source_dir + "\\labels"
        source_image_dir = source_dir + "\\images"

        # Get a list of file names in the text folder (assuming the names match the image files)
        file_names = os.listdir(source_text_dir)

        # Randomly shuffle the file names using the seeded random function
        random.shuffle(file_names)

        # Calculate the split point based on an split/1-split ratio ex: 80/20
        fold_size = len(file_names) // k

        subset_files = []
        for i in range(k):
            if i == k-1:
                subset = file_names[i * fold_size :]
            else:
                subset = file_names[i * fold_size : (i + 1) * fold_size]
            subset_files.append(subset)

        for i in range(k):

            training_files  = subset_files[:i] + subset_files[i+1:] # get all files except fold
            training_files = [element for sublist in training_files for element in sublist] # collapse 2d array into 1d

            testing_files = subset_files[i]

            # Set the destination directories
            out_train_text_dir = output_dir + f"\\{i+1}\\train\\labels"
            out_train_image_dir = output_dir + f"\\{i+1}\\train\\images"
            out_test_text_dir =  output_dir + f"\\{i+1}\\test\\labels"
            out_test_image_dir = output_dir + f"\\{i+1}\\test\\images"

            os.makedirs(out_train_text_dir, exist_ok=True)
            os.makedirs(out_train_image_dir, exist_ok=True)
            os.makedirs(out_test_text_dir, exist_ok=True)
            os.makedirs(out_test_image_dir, exist_ok=True)

            for file_name in training_files:
                    try:
                        shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_train_text_dir, file_name))
                        shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_train_image_dir, file_name[:-4]+".jpg"))
                    except:
                        print("Could not copy files: " + file_name)
                        continue
            
            for file_name in testing_files:
                try:
                    shutil.copy2(os.path.join(source_text_dir, file_name), os.path.join(out_test_text_dir, file_name))
                    shutil.copy2(os.path.join(source_image_dir, file_name[:-4]+".jpg"), os.path.join(out_test_image_dir, file_name[:-4]+".jpg"))
                except:
                    print("Could not copy files: " + file_name)
                    continue

        