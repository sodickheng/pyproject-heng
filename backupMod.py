import os
import shutil
import datetime
import schedule
import time

# Define the source and destination directories
source_dir = "source path"
destination_dir = "destination path"

def copy_folder_to_directory(source, dest):
    # Get today's date
    today = datetime.date.today()
    # Create the destination directory path with today's date
    dest_dir = os.path.join(dest, str(today))

    try:
        # Copy the source directory to the destination directory
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        # If the directory already exists, print a message
        print(f"Folder already exists in: {dest}")

# Schedule the task to run every day at 08:25 AM
schedule.every().day.at("08:25").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
