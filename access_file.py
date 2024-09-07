# specify a path folder, and when new file are
# saved/moved to this path folder at new times
# display the file path name and file modify timing
import os
import time

# Specify the directory you want to monitor for changes
#folder_path = "/path/to/your/folder"
folder_path = "/Users/heng/Desktop/test_folder"

# This dictionary will store the modification times of the files in the folder
file_mod_times = {}


# Function to retrieve the modification times of all files in the folder
def get_file_mod_times(folder):
    # Returns a dictionary where keys are filenames and values are the last modification times
    return {
        # get times of the path folder
        f: os.path.getmtime(os.path.join(folder, f))
        # loop in list directory of the specify folder
        for f in os.listdir(folder)
        # check using if the specify path folder is a file and not a sub directory
        if os.path.isfile(os.path.join(folder, f))
    }

# Infinite loop to continuously monitor the folder
while True:
    # Get the current modification times of the files in the folder
    new_mod_times = get_file_mod_times(folder_path)

    # Check if there are any new or updated files
    # look at each files in the folder
    # This loop goes through each file in the folder and gets its modification time.
    for file_name, mod_time in new_mod_times.items():
        # time has changed (meaning it was updated), the script recognizes it as new or updated.
        if file_name not in file_mod_times or file_mod_times[file_name] != mod_time:

            readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
            print(f"New updated files detected: {file_name} at {readable_time}")

    # Update the stored modification times with the latest data
    file_mod_times = new_mod_times

    # Pause for 1 minute before checking the folder again
    time.sleep(10)

