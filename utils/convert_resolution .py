from PIL import Image
import os

# Set input and output folder paths
input_folder = 'input_images'
output_folder = 'output_images'
os.makedirs(output_folder, exist_ok=True)

# Set target resolution
target_size = (640, 360)

# Iterate over all image files
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image and resize it
        with Image.open(input_path) as img:
            resized_img = img.resize(target_size)
            resized_img.save(output_path)
            print(f'Processed: {filename}')
