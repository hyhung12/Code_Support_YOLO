from ultralytics.utils.plotting import Annotator
import cv2
from ultralytics import YOLO
import os
import numpy as np

# Input and output directories
input_folder = r"D:\ShipDetection\Image_car_data_28_09_23_2"
output_folder_labels = r'C:\CarDetection\annotation_test'
output_folder_images = r'C:\CarDetection\prediction_test'

# Perform object detection on the image.
model = YOLO(r"C:\CarDetection\model\best.pt")

# Iterate through the images in the input folder
for image_file in os.listdir(input_folder):
    if image_file.endswith(('.jpg')):
        # Load the image
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)
        
        results = model.predict(image)

        # Create a YOLO label file for each image
        label_file = os.path.splitext(image_file)[0] + '.txt'
        label_path = os.path.join(output_folder_labels, label_file)
        
        with open(label_path, 'w') as label_file:
            for r in results:
                annotator = Annotator(image)
                
                boxes = r.boxes
                probs = r.probs
                print(probs)
                for box in boxes:
                    # Create a list to store the values of the tensor elements.
                    values = []

                    b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
                    # Get the shape of the tensor.
                    shape = b.shape

                    # Iterate over the tensor elements and save each value to the list.
                    for i in range(shape[0]):
                        values.append(b[i])
                        # Assign the list to the variables.
                    x1 = values[0]
                    y1 = values[1]
                    x2 = values[2]
                    y2 = values[3]

                    c = box.cls # class

                    center_x, center_y, width, height = convert_to_yolo_format(x1, y1, x2, y2, image)
                    class_id = int(c[0])
                    
                    # Write YOLO format to the label file with class 0
                    label_file.write(f'{class_id} {center_x} {center_y} {width} {height}\n')
                        

                    annotator.box_la3bel(b, model.names[int(c)], color=5)

            output_file = os.path.join(output_folder_images, f'{os.path.basename(image_file)}')
            cv2.imwrite(output_file, image)

        

# image = annotator.result() 
output_file = os.path.join(output_folder_images, f'{os.path.basename(image_file)}')
cv2.imwrite(output_file, image)
# cv2.imshow(image)  
