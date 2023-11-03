import os
import shutil

def make_dataset(labels_folder, images_folder, dataset_path):

    os.makedirs(dataset_path, exist_ok=True)
    subsets = os.listdir(images_folder)

    if len(subsets) != 0:
        print(len(subsets))

        for i in subsets:
            image_subset = f'{images_folder}\\{str(i)}\\'
            labels_subset = f'{labels_folder}\\{str(i)}\\'

            copy_images_labels(labels_subset, image_subset, dataset_path)
    else: 
      
        copy_images_labels(labels_folder, images_folder, dataset_path)
    
# change to copy both labels & images 
def copy_images_labels(labels_folder,images_folder,dataset_path):
    print()
    print(labels_folder)
    print()
    
    all_labels = os.listdir(labels_folder)
    for file in all_labels:
        
        label_name = file[:-4] + '.jpg'
        img_name = images_folder + label_name 
        try:
            # copy image
            
            shutil.copy2(img_name, f'{dataset_path}\\images')
            shutil.copy2(label_name, f'{dataset_path}\\labels')

        except:
            print("Could not copy image: " + img_name)



