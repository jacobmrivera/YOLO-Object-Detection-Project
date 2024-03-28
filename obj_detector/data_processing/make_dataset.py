import os
import shutil



# given a folder of labels and images, copy data into dataset_path folder
def make_dataset(labels_folder, images_folder, dataset_path):

    os.makedirs(dataset_path, exist_ok=True)
    os.makedirs(f'{dataset_path}\\images',exist_ok=True)
    os.makedirs(f'{dataset_path}\\labels',exist_ok=True)

    subsets = os.listdir(images_folder)

    # assumes that the images folder follow a stucture like this 
    # >images
    #   >1
    #   >n

    for i in subsets:
        image_subset = f'{images_folder}\\{str(i)}\\'
        labels_subset = f'{labels_folder}\\{str(i)}\\'

        copy_images_labels(labels_subset, image_subset, dataset_path)

# change to copy both labels & images 
def copy_images_labels(labels_folder,images_folder,dataset_path):
    
    all_labels = os.listdir(labels_folder)
   
    for file in all_labels:

        label_name = labels_folder + file
        img_name = images_folder + file[:-4] + '.jpg'
       
        try:
            # copy image
            shutil.copy2(img_name, f'{dataset_path}\\images')

        except:
            print("Could not copy image: " + img_name)

        try: 
            # copy label
            shutil.copy2(label_name, f'{dataset_path}\\labels')
        except:
            print("Could not copy txt: " + label_name)


