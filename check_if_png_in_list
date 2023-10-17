import os

folder_path = r"C:\Users\HP\Downloads\test_remove\learn2_labels_1390"  # Replace with the path to your folder
file_list = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(file_path):
        # Use os.path.splitext to split the filename and extension
        name_without_extension, _ = os.path.splitext(filename)
        file_list.append(name_without_extension )
print(file_list[:2])

folder_path = r"C:\Users\HP\Downloads\test_remove\images_1390"  # Replace with the path to your folder
number_of_files = 0
# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(file_path):
        # Extract the filename (without extension) from the full path
        name_without_extension, _ = os.path.splitext(filename)
        
        # Check if the filename (without extension) is in the file_list list
        if name_without_extension not in file_list:
            number_of_files += 1
            print(f"File not in: {filename}")
            os.remove(file_path)
print(number_of_files)
# Removing file: video_frame_7084.png
