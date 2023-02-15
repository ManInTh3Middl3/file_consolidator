import os
import shutil

# Ask the user for a directory
dir_path = input("Enter the directory path: ")

# Create a new directory to move the files to
new_dir = os.path.join(dir_path, "consolidated_files")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

# Move all files to the new directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_dir, file)
        shutil.move(file_path, new_file_path)

# Remove all old directories
for root, dirs, files in os.walk(dir_path):
    for dir in dirs:
        if os.path.join(root, dir) != new_dir:
            shutil.rmtree(os.path.join(root, dir))
