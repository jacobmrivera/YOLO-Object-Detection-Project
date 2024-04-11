from PIL import Image

def stitch_images(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Determine the width and height of the stitched image
    width = image1.width + image2.width
    height = max(image1.height, image2.height)

    # Create a new blank image with the calculated dimensions
    stitched_image = Image.new('RGB', (width, height))

    # Paste the first image onto the stitched image at (0,0)
    stitched_image.paste(image1, (0, 0))

    # Paste the second image onto the stitched image at (image1.width, 0)
    stitched_image.paste(image2, (image1.width, 0))

    # Save the stitched image
    stitched_image.save(output_path)

# Example usage
image1_path = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\test\\positive_JA\\1201_img_110.jpg"
image2_path = "C:\\Users\\multimaster\\Desktop\\JA_DATASET\\test\\positive_JA\\1201_img_110.jpg"
output_path = "stitched_image.jpg"

stitch_images(image1_path, image2_path, output_path)