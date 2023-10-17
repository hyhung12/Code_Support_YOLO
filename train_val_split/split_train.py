import os
import shutil

folder_path = r"C:\Users\HP\Downloads\cam12_merge_upload\train\labels"  # Replace with the path to your folder
file_list = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(file_path):
        # Use os.path.splitext to split the filename and extension
        name_without_extension, _ = os.path.splitext(filename)
        file_list.append(name_without_extension )

print(file_list[:2])
# Source directory (folderA) and destination directory (folderB)
source_folder = r"C:\Users\HP\Downloads\cam12_merge\merge_images12" # images folder
destination_folder = r"C:\Users\HP\Downloads\cam12_merge_upload\train\images"
os.makedirs(destination_folder , exist_ok=True)

for filename in os.listdir(source_folder):
    name_without_extension, _ = os.path.splitext(filename)
    if name_without_extension in file_list:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copy(source_path, destination_path)
    
print("Copy operation complete.")
