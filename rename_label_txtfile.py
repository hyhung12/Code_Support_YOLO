import os

# Specify the directory you want to iterate through
directory_path = r'C:\Users\HP\Downloads\test_remove\learn2_labels_1436_2'
png_keyword = '_png'

# Iterate through the list of files and print their names
for filename in  os.listdir(directory_path):
    index = filename.find(png_keyword)
    result = filename[:index] + '.txt'
    old_filepath = os.path.join(directory_path, filename)
    new_filepath = os.path.join(directory_path, result)
    # print(new_filepath)
    os.rename(old_filepath, new_filepath)
