import cv2
import os
import shutil

# Function to calculate the image blur level
def calculate_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

# Source and destination directories
source_dir = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\original_data_corrected"
destination_dir = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\corrected_not_blurry_subset"

# Threshold for the blur level
threshold = 50  # Adjust this threshold as needed

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)
os.makedirs(os.path.join(destination_dir,'images'), exist_ok=True)
os.makedirs(os.path.join(destination_dir,'labels'), exist_ok=True)


# Iterate through all jpg files in the source directory
for filename in os.listdir(os.path.join(source_dir,'images')):
	# print(filename)
	if filename.endswith('.jpg'):
		img_filepath = os.path.join(source_dir, 'images', filename)
		txt_filepath = os.path.join(source_dir, 'labels', filename[:-4] + '.txt')

		# Read the image using OpenCV
		img = cv2.imread(img_filepath)
		
		# Calculate the blur level
		blur_level = calculate_blur(img)
	
		# If the blur level is above the threshold, copy the image to the destination directory
		if blur_level > threshold:
			img_destination_path = os.path.join(destination_dir, 'images', filename)
			shutil.copyfile(img_filepath, img_destination_path)

			label_destination_path = os.path.join(destination_dir, 'labels', filename[:-4] + '.txt')
			shutil.copyfile(txt_filepath, label_destination_path)

			print(f"Copied {filename} - Blur level: {blur_level}")

print("Done processing images.")
