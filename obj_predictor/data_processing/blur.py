import cv2
import os





'''
Generates and returns blur value for a single image
'''
def get_blur_level(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(img_gray, cv2.CV_64F).var()

    return variance




'''
Generates blur values for each image in a directory
Outputs a text file containing the blur values and overall blur ratio

Only set to handle .jpg images. If other image types are used, change
the following line: 'if image[-4:] != ".jpg": continue' 
to the appropriate file extension.


'''
def batch_gen_blur_levels(input_dir, output_dir, threshold):
    img_count = 0

    # get list of all files in dir
    file_name_list = os.listdir(input_dir)

    # if no new name given for text file, use default and put it in
    if output_dir.split('\\')[-1][-4:] != ".txt":
        out_path = os.path.join(output_dir,"images_blur_values.txt")

    blurry_count = 0

    with open(out_path, 'w') as file:
        for image in file_name_list:
            # if not an image, skip
            if image[-4:] != ".jpg": continue

            blurry_lvl = get_blur_level( os.path.join(input_dir, image))

            if blurry_lvl < threshold: blurry_count += 1
            img_count += 1

            formatted_string = '{:<30}'.format(image)  # Adjust width as needed for strings
            formatted_float = '{:<10.4f}'.format(blurry_lvl)  # Adjust width and precision for floats

            # Write the formatted string and float to the file
            file.write(f"{formatted_string} {formatted_float}\n")

    # Read the existing content of the file
    with open(out_path, 'r') as file:
        existing_content = file.read()

    to_add = f"\n\n{blurry_count} blurry images out of {img_count}\nRatio: { blurry_count/ img_count}\n"
    all_content = to_add + existing_content

    # Write the combined content back to the file
    with open(out_path, 'w') as file:
        file.write(all_content)

    print(f"\n\n{blurry_count} blurry images out of {img_count}\nRatio: { blurry_count/ img_count}")

    cv2.destroyAllWindows()

    return



###
# get blur levels of object level directories
#
# input_dir: directory containing object level directories
# num_obj: number of object level directories
# threshold: threshold for blurry level
# output_dir: directory to put obj blur levels text files,
#   if none given, will put in src dir for each object
#
# output: none, creates text files in output_dir
###
def get_obj_blur_levels(parent_dir, num_obj, threshold=50, output_dir=''):

    for i in range(num_obj):
        img_count = 0

        # input and output for object dir
        input_dir = os.path.join(parent_dir, str(i))
        output_dir = os.path.join(parent_dir, str(i)) if output_dir == '' else output_dir

        # get list of all files in dir
        file_name_list = os.listdir(input_dir)

        # create obj text file to hold blurry vals
        out_path = os.path.join(output_dir, f"obj{i}_image_blur_values.txt")
        blurry_count = 0

        with open(out_path, 'w') as file:
            for image in file_name_list:
                # if not an image, skip
                if image[-4:] != ".jpg": continue

                blurry_lvl = get_blur_level( os.path.join(input_dir, image))
                if blurry_lvl < threshold: blurry_count += 1
                img_count += 1

                formatted_string = '{:<30}'.format(image)  # Adjust width as needed for strings
                formatted_float = '{:<10.4f}'.format(blurry_lvl)  # Adjust width and precision for floats

                # Write the formatted string and float to the file
                file.write(f"{formatted_string} {formatted_float}\n")

        with open(out_path, 'a') as file:
            file.write("\n\n{} blurry images out of {}\n".format(blurry_count, img_count))
            file.write("Ratio: {}".format( blurry_count/ img_count))
        print("\n\nObject {}  --  {} blurry images out of {}\n".format(i, blurry_count, img_count))
        print("Ratio: {}".format( blurry_count/ img_count))

    cv2.destroyAllWindows()
    return