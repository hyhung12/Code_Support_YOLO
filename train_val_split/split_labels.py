import os
import random
import shutil

# Path to the directory containing the original text files
original_folder = r"C:\Users\HP\Downloads\cam12_merge\merge_labels12"

# List all the text files in the original folder
all_files = os.listdir(original_folder)
text_files = [f for f in all_files if f.endswith(".txt")]

# Shuffle the list of text files randomly
random.shuffle(text_files)

# Split the list into two parts (75% and 25%)
split_point = int(0.8 * len(text_files))
folder1_files = text_files[:split_point]
folder2_files = text_files[split_point:]

# Define the paths for the two destination folders
folder1_path = r"C:\Users\HP\Downloads\cam12_merge\train_labels"
folder2_path = r"C:\Users\HP\Downloads\cam12_merge\val_labels"
os.makedirs(folder1_path , exist_ok=True)
os.makedirs(folder2_path , exist_ok=True)

# Move the files to their respective folders
for file in folder1_files:
    source_path = os.path.join(original_folder, file)
    destination_path = os.path.join(folder1_path, file)
    shutil.copy(source_path, destination_path)

for file in folder2_files:
    source_path = os.path.join(original_folder, file)
    destination_path = os.path.join(folder2_path, file)
    shutil.copy(source_path, destination_path)

print("OK")
