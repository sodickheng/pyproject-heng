import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_extension = filename.split('.')[-1]
        print(file_extension)  # png, pdf
        folder_name = file_extension + "_files"    # png_files, pdf_files
        folder_path = os.path.join(directory, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # move # Test_folder inside .png files or .pdf files   to    png_files folder and pdf_files folder
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

# put some png and pdf files in  # Test_folder
organize_files("/Users/heng/Desktop/Test_folder")
