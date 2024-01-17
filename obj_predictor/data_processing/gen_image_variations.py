from PIL import Image

# def flip_image_vertically(input_image_path, output_image_path):
#     try:
#         # Open the image file
#         with Image.open(input_image_path) as img:
#             # Flip the image vertically
#             flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            
#             # Save the flipped image
#             flipped_img.save(output_image_path)
#             print(f"Flipped image saved as {output_image_path}")
#     except IOError:
#         print("Unable to load image")

# Usage example:
input_image = "input_image.jpg"  # Replace with your input image file path
output_image = "flipped_image.jpg"  # Replace with your desired output image file path
# flip_image_vertically(input_image, output_image)






from PIL import Image, ImageOps, ImageDraw, ImageFont
import cv2
import os

def flip_image_vertically(input_image_path, output_image_path):
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
            print(f"Flipped image saved as {output_image_path}")
    except IOError:
        print("Unable to load image")





def mirror_image_horizontally(input_image_path, output_image_path):
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
            print(f"Flipped image saved as {output_image_path}")
    except IOError:
        print("Unable to load image")


def flip_and_mirror_image(input_image_path, output_image_path):
    try:
        # Open the image file
        with Image.open(input_image_path) as img:
            # Flip the image horizontally using mirror
            flipped_img = ImageOps.flip(img)

            mirrored_img = ImageOps.mirror(flipped_img)
            
            # Save the flipped image
            mirrored_img.save(output_image_path)
            print(f"Flipped and mirrored image saved as {output_image_path}")
    except IOError:
        print("Unable to load image")


def rotate_image(input_image_path, output_image_path, angle):
    try:
        # Open the image file
        with Image.open(input_image_path) as img:
            # Rotate the image by a specified angle
            rotated_img = img.rotate(angle, expand=True)
            
            # Save the rotated image
            rotated_img.save(output_image_path)
            print(f"Rotated image saved as {output_image_path}")
    except IOError:
        print("Unable to load image")





# x center, y center, wdith, hieght, all normalized
def draw_bounding_box(img_path, output_path, box_vals, box_string):

    # box_vals = [x_center, y_center, width, height]

    # Load your existing image
    existing_image = cv2.imread(img_path)

    # Calculate bounding box coordinates
    image_height, image_width, _ = existing_image.shape
    left = int((box_vals[0] - box_vals[2] / 2) * image_width)
    top = int((box_vals[1] - box_vals[3] / 2) * image_height)
    right = int((box_vals[0] + box_vals[2] / 2) * image_width)
    bottom = int((box_vals[1] + box_vals[3] / 2) * image_height)

    # Draw a purple rectangle on the image
    rectangle_color = (236, 3, 252)  # Purple color in BGR format
    rectangle_thickness = 3  # Change the thickness of the line here

    cv2.rectangle(existing_image, (left, top), (right, bottom), rectangle_color, rectangle_thickness)

    # Define label text and its position (attached to the bounding box)
    label_text = box_string # Replace with your label text
    text_position = (left, top - 10)  # Adjust the offset as needed

    # Add label text to the image
    text_color = (236, 3, 252)  # Blue color in BGR format
    font_scale = 1.5  # Font scale
    font_thickness = 5  # Font thickness

    cv2.putText(existing_image, label_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
    cv2.imwrite(output_path, existing_image)


def mirror_bounding_box_y_axis(box_vals, image_width, image_height):
    # Calculate original bounding box coordinates
    left = box_vals[0] - box_vals[2] / 2
    top = box_vals[1] - box_vals[3] / 2
    right = box_vals[0] + box_vals[2] / 2
    bottom = box_vals[1] + box_vals[3] / 2

    # Mirror the bounding box coordinates across the center of the image
    mirrored_top = 1 - bottom
    mirrored_bottom = 1 - top

    # New mirrored bounding box coordinates
    mirrored_center_y = (mirrored_top + mirrored_bottom) / 2
    mirrored_height = mirrored_bottom - mirrored_top

    # Return the mirrored bounding box coordinates in YOLO format
    return [box_vals[0], mirrored_center_y, box_vals[2], mirrored_height]


def mirror_bounding_box_x_axis(box_vals, image_width, image_height):
    # Calculate original bounding box coordinates
    left = box_vals[0] - box_vals[2] / 2
    top = box_vals[1] - box_vals[3] / 2
    right = box_vals[0] + box_vals[2] / 2
    bottom = box_vals[1] + box_vals[3] / 2

    # Mirror the bounding box coordinates across the center of the image
    mirrored_left = 1 - right
    mirrored_right = 1 - left

    # New mirrored bounding box coordinates
    mirrored_x_center = (mirrored_left + mirrored_right) / 2
    mirrored_width = mirrored_right - mirrored_left

    # Return the mirrored bounding box coordinates
    return [mirrored_x_center, box_vals[1], mirrored_width, box_vals[3]]


def mirror_bounding_box_xy(box_vals, image_width, image_height):
    # Calculate original bounding box coordinates
    left = box_vals[0] - box_vals[2] / 2
    top = box_vals[1] - box_vals[3] / 2
    right = box_vals[0] + box_vals[2] / 2
    bottom = box_vals[1] + box_vals[3] / 2

    # Mirror the bounding box coordinates across the x-axis
    mirrored_left = 1 - right
    mirrored_right = 1 - left

    # Mirror the bounding box coordinates across the y-axis
    mirrored_top = 1 - bottom
    mirrored_bottom = 1 - top

    # New mirrored bounding box coordinates
    mirrored_x_center = (mirrored_left + mirrored_right) / 2
    mirrored_y_center = (mirrored_top + mirrored_bottom) / 2
    mirrored_width = mirrored_right - mirrored_left
    mirrored_height = mirrored_bottom - mirrored_top

    # Return the mirrored bounding box coordinates
    return [mirrored_x_center, mirrored_y_center, mirrored_width, mirrored_height]



def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height



# transform each line of annotation text file
def process_text_file(input_file, output_file, width, height, direction):
    # Read content from the input file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # iterate over lines from input text file
    for i in range(len(lines)):
        curr_line = lines[i].rstrip('\n')
        curr_line_arr = curr_line.split(' ')

        # might be a problem with indexing to avoid the obj number (first element)
        if direction == 'y':
            bb_array = mirror_bounding_box_y_axis(curr_line_arr[1:], width, height)
        elif direction == 'x':
            bb_array = mirror_bounding_box_x_axis(curr_line_arr[1:], width, height)
        elif direction == 'xy':
            bb_array = mirror_bounding_box_xy(curr_line_arr[1:], width, height)
        # recreate string to write to output file
        lines[i] = f"{curr_line_arr[0]} {bb_array[0]} {bb_array[1]} {bb_array[2]} {bb_array[3]}\n"

    # Create the output directory if it does not exist
    output_txt_dir = os.path.dirname(output_file)

    if not os.path.exists(output_txt_dir):
        os.makedirs(output_txt_dir)

    # Write the modified content to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines)

    return


# Usage example:
input_image = "luffy_album.png"  # Replace with your input image file path
output_image = "luffy_album_out.png"  # Replace with your desired output image file path


# Sample bounding box information (normalized)
x_center = 0.25  # x-coordinate of the center
y_center = 0.25  # y-coordinate of the center
width = 0.3  # width of the bounding box
height = 0.1  # height of the bounding box

bounding_box = [x_center, y_center, width, height]

draw_bounding_box(input_image, "luffy_album_bb.png",bounding_box, "LUFFY!!!")

mirrod_bb = mirror_bounding_box_x_axis(bounding_box, 3024, 4032)


mirror_image_horizontally(input_image, "luffy_album_flip_vertical.png")

draw_bounding_box("luffy_album_flip_vertical.png", "luffy_album_flip_vertical.png",mirrod_bb, "LUFFY!!!")




# # Example usage:
# x_center = 0.5  # x-coordinate of the center
# y_center = 0.4  # y-coordinate of the center
# width = 0.3  # width of the bounding box
# height = 0.2  # height of the bounding box
# image_width = 640  # Replace with the actual width of your image
# image_height = 480  # Replace with the actual height of your image

# # Get the mirrored bounding box coordinates
# mirrored_x_center, mirrored_y_center, mirrored_width, mirrored_height = mirror_bounding_box(
#     x_center, y_center, width, height, image_width, image_height
# )






### below WORKS
# flip_image_vertically(input_image, "luffy_album_flip_vertical.png")
# mirror_image_horizontally(input_image, "luffy_album_mirror_horizontal.png")
# flip_and_mirror_image(input_image, "luffy_album_flip_and_mirror.png")










