import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Input folders for images and YOLO format label files
image_folder = r'C:\Users\HP\Downloads\add_label1_edited\images'
label_folder = r'C:\Users\HP\Downloads\add_label1_edited\labels'
output_folder = r'C:\Users\HP\Downloads\add_label1_edited\labels\plot_output'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)
# Define a list of class names (replace with your own class names)
class_names = ['bike','car']

# Function to parse YOLO format labels
def parse_yolo_label(label_path, image_shape):
    with open(label_path, 'r') as label_file:
        lines = label_file.readlines()

    boxes = []
    for line in lines:
        parts = line.strip().split()
        class_id, x_center, y_center, width, height = map(float, parts)

        # Convert YOLO format to absolute coordinates
        x_center *= image_shape[1]
        y_center *= image_shape[0]
        width *= image_shape[1]
        height *= image_shape[0]

        # Calculate the coordinates of the bounding box
        x1 = int(x_center - width / 2)
        y1 = int(y_center - height / 2)
        x2 = int(x_center + width / 2)
        y2 = int(y_center + height / 2)

        boxes.append((class_id, x1, y1, x2, y2))

    return boxes

# Get a list of image filenames
image_filenames = [filename for filename in os.listdir(image_folder) if filename.endswith('.png')]

# Iterate through image filenames
for image_filename in image_filenames:
    image_path = os.path.join(image_folder, image_filename)
    label_filename = os.path.splitext(image_filename)[0] + '.txt'
    label_path = os.path.join(label_folder, label_filename)

    # Read the image
    image = cv2.imread(image_path)

    # Get image shape (height, width)
    image_shape = image.shape[:2]

    # Parse YOLO format labels
    print(f"hey {label_filename}")
    if os.path.exists(label_path):
        boxes = parse_yolo_label(label_path, image_shape)

        # Draw bounding boxes on the image with class names
        for class_id, x1, y1, x2, y2 in boxes:
            class_name = class_names[int(class_id)]
            color = (0, 255, 0)  # Green color (BGR format)
            thickness = 2
            image = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
            cv2.putText(image, class_name, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Save the image with class names and bounding boxes to the output folder
    output_path = os.path.join(output_folder, image_filename)
    cv2.imwrite(output_path, image)
print("Images with class names and bounding boxes saved to the output folder.")
