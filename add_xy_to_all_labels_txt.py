import os

# Step 1: Read the content from 'ab.txt'
txt_path = r"C:\Users\HP\Downloads\add_label1\ab.txt"
with open(txt_path, 'r') as ab_file:
    ab_text = ab_file.read()

# Step 2: Get a list of all '.txt' files in the folder
folder_path = r'C:\Users\HP\Downloads\add_label1\labels'  # Replace with the actual folder path

txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    
    # Check if the file is not empty before appending
    if os.path.getsize(file_path) > 0:
        with open(file_path, 'a') as file_to_append:
            file_to_append.write('\n' + ab_text)
    else:
        with open(file_path, 'a') as file_to_append:
            file_to_append.write( ab_text)
