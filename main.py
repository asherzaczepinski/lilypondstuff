from PIL import Image

def crop_top_quartet(input_image_path, output_image_path, crop_proportion=0.25):
    """
    Crops the top portion of an image based on a proportion of its height and saves the result.

    :param input_image_path: Path to the original image (e.g., 'output.png')
    :param output_image_path: Path to save the cropped image (e.g., 'top_quartet.png')
    :param crop_proportion: The fraction of the image's height to retain from the top (default is 0.25 for 25%)
    """
    try:
        # Open the original image
        with Image.open(input_image_path) as img:
            width, height = img.size
            print(f"Original Image Size: {width}x{height} pixels")

            # Calculate crop_height based on the specified proportion
            crop_height = int(height * crop_proportion)
            print(f"Calculated Crop Height: {crop_height} pixels (Proportion: {crop_proportion})")

            # Ensure crop_height does not exceed the image's height
            if crop_height > height:
                crop_height = height
                print(f"Adjusted Crop Height to Image Height: {crop_height} pixels")

            # Define the cropping box: (left, upper, right, lower)
            crop_box = (0, 0, width, crop_height)

            # Perform the crop
            cropped_img = img.crop(crop_box)
            print(f"Cropped Image Size: {cropped_img.size[0]}x{cropped_img.size[1]} pixels")

            # Save the cropped image
            cropped_img.save(output_image_path)
            print(f"Cropped image saved as '{output_image_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define paths
    input_path = "output.png"          # Path to the original image
    output_path = "top_quartet.png"    # Path to save the cropped image

    # Define the proportion to crop (e.g., 0.25 for 25%)
    crop_proportion = 0.25

    # Call the crop function
    crop_top_quartet(input_path, output_path, crop_proportion)
