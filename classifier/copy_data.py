import os
import shutil

def copy_files_starting_with_17388(input_dir, output_dir):
    # Ensure the output directory exists; create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the filename starts with "17388"
        if filename.startswith("17358"):
            # Construct full paths for the source and destination files
            source_path = os.path.join(input_dir, filename)
            destination_path = os.path.join(output_dir, filename)
            
            # Copy the file to the output directory
            shutil.copy(source_path, destination_path)
            print(f"Copied {filename} to {output_dir}")

# Example usage:
input_directory = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\child_positive_frames"
output_directory = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\exp12_child_datasets\\17358_set_aside\\17358\\positive_JA"

# copy_files_starting_with_17388(input_directory, output_directory)
