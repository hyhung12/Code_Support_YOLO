## Count number of files

import os

folder_path = r'C:\Users\HP\Downloads\avi_to_mp4' # Replace with the actual folder path
files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
file_count = len(files)
print(f"Total files in folder: {file_count}")

## Convert JPG to PNG

from PIL import Image
import os

# Define the input and output directories
input_dir = r'C:\Users\HP\Downloads\0928_1622_1744.v2i.yolov8_after_label\train\images'
output_dir = r'C:\Users\HP\Downloads\new_png'

# Ensure the output directory exists; create it if it doesn't
os.makedirs(output_dir, exist_ok=True)

# Loop through the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        # Open the image using Pillow
        img = Image.open(os.path.join(input_dir, filename))

        # Change the file extension to .png and save the image
        png_filename = os.path.splitext(filename)[0] + '.png'
        img.save(os.path.join(output_dir, png_filename), 'PNG')

print("Conversion complete.")  


  
