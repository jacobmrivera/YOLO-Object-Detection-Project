import os
from PIL import Image, ImageDraw, ImageFont


INPUT_DIR = "C:\\Users\\multimaster\\Desktop\\Final_dataset_11_13_23\\11_13_23\\obj_level_data\\{}"

def draw_bounding_boxes(input_file):
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

# Example usage:
for i in range(28):
    print("Inside Directory: {}".format(i))
    input_txt_file = INPUT_DIR.format(i)
    draw_bounding_boxes(input_txt_file)
