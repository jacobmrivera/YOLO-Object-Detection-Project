import os
from PIL import Image, ImageDraw, ImageFont
import obj_predictor.data_processing.smooth as smooth
from ultralytics import YOLO
import cv2
'''

need to make functions that can draw bounding boxes, 
    from one frame and one text file,
then a func to batch process the above function
Then a function to stich all the frames together into a video

'''


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
    27: 'rgb(192, 192, 192)',
    47: 'rgb(192, 192, 192)'
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



def draw_single_frame(frame, labels_file, drawn_frame, save_drawn_frame=False):

    with open(labels_file, 'r') as file:
        lines = file.readlines()

    # print(labels_file)
    # print(lines)
    # RGB: (236, 3, 252)
    # Draw text with outline
    # text_color = 'black'
    # outline_color = 'rgb(236, 3, 252)'
    # outline_width = 5

    img = Image.open(frame)
    draw = ImageDraw.Draw(img)


    img_width, img_height = img.size

    # Calculate the font size based on image size
    base_font_size = 15  # Set your base font size here
    font_size = int(base_font_size * min(img_width, img_height) / 800)  # Adjust the divisor as needed

    base_line_width = 3
    line_width = int(base_line_width * min(img_width, img_height) / 800)  # Adjust the divisor as needed

    base_padding = 3
    padding = int(base_padding * min(img_width, img_height) / 800)  # Adjust the divisor as needed

    # Define font and size
    font = ImageFont.truetype("data/fonts/lato/Lato-Bold.ttf", font_size)  # Adjust font and size as needed


    for line in lines:
        # Split the line into components
        components = line.strip().split()
        # image_name = components[0].replace('.txt', '.jpg')
        obj_num = int(components[0])
        bbox_info = list(map(float, components[1:]))

        # Get image width and height

        # Convert bounding box coordinates to YOLO format
        x_center = bbox_info[0] * img_width
        y_center = bbox_info[1] * img_height
        box_width = bbox_info[2] * img_width
        box_height = bbox_info[3] * img_height
        # print(f"Y_CETNER: {y_center}")
        # Calculate box coordinates
        x_min = x_center - (box_width / 2)
        y_min = y_center - (box_height / 2)
        x_max = x_center + (box_width / 2)
        y_max = y_center + (box_height / 2)

        if (y_min > y_max):
            temp = y_min
            y_min = y_max
            y_min = temp
        if (x_min > x_max):
            temp = x_min
            x_min = x_max
            x_min = temp

        color = rgb_dict[obj_num] if obj_num in rgb_dict else 'rgb(236, 3, 252)'

        box_text = f" obj#: {obj_num} "
        # text_bbox = draw.textbbox((0, 0), box_text, font)

        # Draw bounding box
        draw.rectangle([x_min, y_min, x_max, y_max], outline=color, width=line_width)

        # Draw text
        left, top, right, bottom = draw.textbbox((x_min, y_min - font_size), box_text, font=font)
        draw.rectangle((left, top-line_width, right+line_width, bottom), fill=color)
        draw.text((x_min, y_min-font_size), box_text, font=font, fill="white")


    if save_drawn_frame: img.save(drawn_frame)
    return drawn_frame



# draws annotations onto each frame of video
# expects annotations to be saved as text files, one per frame
#
# input_vid: path to input video
# output_vid: path/name of output video
# predictions_dir: path to directory containing annotations
#
# returns: nothing
def draw_annot_on_video(input_vid, output_vid, predictions_dir):
    cap = cv2.VideoCapture(input_vid)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_vid, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (width, height))

    predictions_files_arr = smooth.list_files_in_directory(predictions_dir, '.txt')
    count = 0

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
        if success:
            drawn_frame = draw_single_frame(frame, predictions_files_arr[count], '')
            out.write(drawn_frame)
            count += 1
        # Break the loop if the end of the video is reached
        else:
            break

    # Release the video capture object and close the display window
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# draw_single_frame("C:\\Users\\jacob\\Desktop\\practice\\apples.jpg", "C:\\Users\\jacob\\Desktop\\practice\\preds.txt","C:\\Users\\jacob\\Desktop\\practice\\apples_drawn.jpg" )
# draw_single_frame("practice_data/apples.jpeg", "practice_data/apples_pred.txt","practice_data/apples_hand_drawn.jpeg" )





