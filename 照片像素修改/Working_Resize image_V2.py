from PIL import Image
import io
import os

# Load the original image
original_image_path = r'C:\Users\h.zhang.2\Desktop\Entress\Fried rice with chicken.jpg'
original_image = Image.open(original_image_path)

# Extract the original image's filename without the extension
original_filename = os.path.splitext(os.path.basename(original_image_path))[0]

# Define the target dimensions (1000x731 pixels)
target_width, target_height = 1000, 731

# Check if the image is smaller than the target dimensions
if original_image.width < target_width or original_image.height < target_height:
    # Calculate the scaling factor to fit the target dimensions while maintaining aspect ratio
    width_scale = target_width / original_image.width
    height_scale = target_height / original_image.height
    scale = max(width_scale, height_scale)

    # Calculate the new dimensions based on the scaling factor
    new_width = int(original_image.width * scale)
    new_height = int(original_image.height * scale)

    # Resize the image while maintaining aspect ratio
    original_image = original_image.resize((new_width, new_height))

# Create a buffer to store the image data
output_buffer = io.BytesIO()

# Adjust the compression quality to increase the file size
compression_quality = 95  # You can experiment with this value
original_image.save(output_buffer, format='JPEG', quality=compression_quality)

# Calculate the current file size
current_file_size = len(output_buffer.getvalue()) / 1024  # Size in KB

# If the current size is still less than 200 KB, keep increasing the quality
while current_file_size < 200:
    compression_quality += 5
    output_buffer = io.BytesIO()
    original_image.save(output_buffer, format='JPEG', quality=compression_quality)
    current_file_size = len(output_buffer.getvalue()) / 1024

# Construct the output filename using the original filename
output_filename = f'{original_filename}_modified.jpg'

# Save the modified image with the original filename
with open(output_filename, 'wb') as output_file:
    output_file.write(output_buffer.getvalue())
