import os
import time

global new_modification_time
global modification_time
new_modification_time = 1
modification_time = 1

def check_file_modified(file_path):
    # Get the modification time of the file
    if os.path.exists(file_path):
        modification_time = os.path.getmtime(file_path)
        print("mod time: ",modification_time)
    else:
        print(f"The file '{file_path}' does not exist.")


    # Wait for some time (e.g., 5 seconds)
    time.sleep(5)

    # Get the modification time of the file again
    if os.path.exists(file_path):
        new_modification_time = os.path.getmtime(file_path)
        print("mod time2: ",new_modification_time)
        return new_modification_time > modification_time
    else:
        print(f"The file '{file_path}' does not exist.")
    # Compare the modification times and return the result
   
