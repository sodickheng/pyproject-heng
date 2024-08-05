import os
import shutil

# Define the path to the directory you want to organize
directory = "path_to_your_directory"

# Define the file type categories and their corresponding folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}

# Create folders for each file type category
for folder in file_types:
    os.makedirs(os.path.join(directory, folder), exist_ok=True)

# Move files into their corresponding folders
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(directory, folder, file_name))
                moved = True
                break
        if not moved:
            # Move unknown file types to a general folder
            os.makedirs(os.path.join(directory, "Others"), exist_ok=True)
            shutil.move(file_path, os.path.join(directory, "Others", file_name))

print("Files have been organized.")
