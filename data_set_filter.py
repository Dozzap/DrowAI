import os
import shutil

# Define source and destination directories
source_dir = 'mrlEyes_2018_01'
closed_dir = 'closed'
open_dir = 'open'

# Create destination directories if they don't exist
os.makedirs(closed_dir, exist_ok=True)
os.makedirs(open_dir, exist_ok=True)

# Iterate through the folders inside the source directory
for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        # Iterate through the files in the folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file.endswith('.png'):
                # Extract the eye state from the filename
                eye_state = file.split('_')[4]
                
                # Check if the image is a closed eye image
                if eye_state == '0':
                    # Copy the image to the closed folder
                    shutil.copy(file_path, closed_dir)
                else:
                    # Copy the image to the open folder
                    shutil.copy(file_path, open_dir)
