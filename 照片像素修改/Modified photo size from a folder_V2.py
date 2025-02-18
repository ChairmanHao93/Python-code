from PIL import Image
import io
import os

# Define the source and destination directories
source_directory = r'C:\Users\h.zhang.2\Desktop\freeesh-kalasatama'
destination_directory = r'C:\Users\h.zhang.2\Desktop\Photo modified'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# List all files in the source directory
file_list = os.listdir(source_directory)

# Create a list to store the filenames of processed images
processed_images = []

# Process each file in the source directory
for filename in file_list:
    # Construct the full path of the original image
    original_image_path = os.path.join(source_directory, filename)

    # Extract the original image's filename without the extension
    original_filename = os.path.splitext(os.path.basename(original_image_path))[0]

    # Check if the processed image already exists in the destination directory
    if f'{original_filename}_modified.jpg' in processed_images:
        print(f'{original_filename} has already been processed.')
        continue  # Skip processing if the image has already been processed

    # Load the original image
    original_image = Image.open(original_image_path)

    # Define the target dimensions (1000x735 pixels)
    target_width, target_height = 1000, 735

    # Calculate the scaling factor to fit the target dimensions while maintaining aspect ratio
    width_scale = target_width / original_image.width
    height_scale = target_height / original_image.height
    scale = max(width_scale, height_scale)

    # Calculate the new dimensions based on the scaling factor
    new_width = int(original_image.width * scale)
    new_height = int(original_image.height * scale)

    # Resize the image while maintaining aspect ratio
    original_image = original_image.resize((new_width, new_height))

    # Initialize the compression quality
    compression_quality = 97

    while True:
        # Create a buffer to store the image data
        output_buffer = io.BytesIO()

        # Save the modified image with the current compression quality
        original_image.save(output_buffer, format='JPEG', quality=compression_quality)

        # Calculate the current file size
        current_file_size = len(output_buffer.getvalue()) / 1024  # Size in KB

        # Check if the current file size is at least 200 KB
        if current_file_size >= 200:
            break  # Stop adjusting quality once the target size is reached

        # Increase the compression quality
        compression_quality += 5

    # Construct the output filename for the modified image
    output_filename = f'{original_filename}_modified.jpg'

    # Add the processed image filename to the list
    processed_images.append(output_filename)

    # Construct the full path of the destination image
    destination_image_path = os.path.join(destination_directory, output_filename)

    # Save the modified image with the original filename to the destination directory
    with open(destination_image_path, 'wb') as output_file:
        output_file.write(output_buffer.getvalue())

# Check for unprocessed images
unprocessed_images = [filename for filename in file_list if f'{os.path.splitext(filename)[0]}_modified.jpg' not in processed_images]

if unprocessed_images:
    print('The following images were not processed:')
    for unprocessed_image in unprocessed_images:
        print(unprocessed_image)
else:
    print('All images have been processed.')
