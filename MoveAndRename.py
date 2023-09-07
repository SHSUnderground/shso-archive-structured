import os
import shutil

# Define the source directory where your files are located.
source_dir = './Assets'

# List all the files in the source directory.
files = os.listdir(source_dir)

# Iterate through each file in the source directory.
for filename in files:
    # Split the filename by '+' to get folder names.
    folder_names = filename.split('+')
    
    # Extract the last element (filename with extension).
    new_filename = folder_names[-1].replace('unity3d', 'asset')
    
    # Remove the last element from folder_names.
    folder_names.pop()
    
    # Create the full destination directory path.
    destination_dir = os.path.join(source_dir, *folder_names)
    
    # Ensure that the destination directory exists, create it if not.
    os.makedirs(destination_dir, exist_ok=True)
    
    # Construct the full source and destination file paths.
    source_file = os.path.join(source_dir, filename)
    destination_file = os.path.join(destination_dir, new_filename)
    
    # Move the file to the new destination and rename it.
    shutil.move(source_file, destination_file)

print("Files moved and renamed successfully.")
