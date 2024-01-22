import os
from PIL import Image, ImageDraw, ImageFont



rgb_dict = {
    0: 'rgb(236, 3, 252)',
    1: 'rgb(192, 32, 64)',
    2: 'rgb(12, 200, 100)',
    3: 'rgb(255, 0, 0)',
    4: 'rgb(0, 255, 0)',
    5: 'rgb(0, 0, 255)',
    6: 'rgb(255, 255, 0)',
    7: 'rgb(255, 0, 255)',
    8: 'rgb(0, 255, 255)',
    9: 'rgb(128, 128, 128)',
    10: 'rgb(255, 128, 0)',
    11: 'rgb(0, 128, 255)',
    12: 'rgb(128, 0, 255)',
    13: 'rgb(255, 128, 128)',
    14: 'rgb(128, 255, 128)',
    15: 'rgb(128, 128, 255)',
    16: 'rgb(255, 192, 192)',
    17: 'rgb(192, 255, 192)',
    18: 'rgb(192, 192, 255)',
    19: 'rgb(0, 128, 128)',
    20: 'rgb(128, 0, 128)',
    21: 'rgb(128, 128, 0)',
    22: 'rgb(255, 255, 255)',
    23: 'rgb(0, 0, 0)',
    24: 'rgb(255, 255, 128)',
    25: 'rgb(255, 128, 255)',
    26: 'rgb(128, 255, 255)',
    27: 'rgb(192, 192, 192)'
}


# INPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\obj_level_data\\{}"

def draw_bounding_boxes(input_file, output_dir=''):
    # Create 'drawn' subdirectory if it doesn't exist
    drawn_dir = os.path.join(input_file, "drawn")  
    os.makedirs(drawn_dir, exist_ok=True)


    all_labels_path = os.path.join(input_file, 'all_labels.txt')
    # Read the input file line by line
    with open(all_labels_path, 'r') as file:
        lines = file.readlines()

    line_width = 3
    # Define font and size
    font = ImageFont.truetype("arial.ttf", 12)  # Adjust font and size as needed

    # RGB: (236, 3, 252)
    # Draw text with outline
    text_color = 'black'
    outline_color = 'rgb(236, 3, 252)'
    outline_width = 3 

    for line in lines:
        # Split the line into components
        components = line.strip().split()
        image_name = components[0].replace('.txt', '.jpg')
        label = int(components[1])
        bbox_info = list(map(float, components[2:]))

        # Open the image
        image_path = os.path.join(os.path.dirname(all_labels_path), image_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)

            # Get image width and height
            img_width, img_height = img.size

            # Convert bounding box coordinates to YOLO format
            x_center = bbox_info[0] * img_width
            y_center = bbox_info[1] * img_height
            box_width = bbox_info[2] * img_width
            box_height = bbox_info[3] * img_height

            # Calculate box coordinates
            x_min = x_center - (box_width / 2)
            y_min = y_center - (box_height / 2)
            x_max = x_center + (box_width / 2)
            y_max = y_center + (box_height / 2)

            # Draw bounding box
            draw.rectangle([x_min, y_min, x_max, y_max], outline='rgb(236, 3, 252)', width=line_width)
            # draw.text((x_min, y_min), str(label), fill='red')
            draw.text((x_min, y_min), "obj#:" + str(label), font=font, fill=text_color, stroke_width=outline_width, stroke_fill=outline_color)


            # Save the modified image to the 'drawn' directory
            drawn_image_path = os.path.join(drawn_dir, image_name)
            img.save(drawn_image_path)
        else:
            print(f"Image {image_name} not found.")

# # Example usage:
# for i in range(28):
#     print("Inside Directory: {}".format(i))
#     input_txt_file = INPUT_DIR.format(i)
#     draw_bounding_boxes(input_txt_file)
