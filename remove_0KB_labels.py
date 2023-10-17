import os

folder_path = r"C:\Users\HP\Downloads\test_remove\learn2_labels_1436"  # Replace with the path to your folder
files_count = 0
# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a subdirectory) and if its size is 0 KB
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        print(f"Removing empty file: {filename}")
        files_count += 1
        os.remove(file_path)
print(f"Count : {files_count}")
