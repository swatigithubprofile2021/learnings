

import os
import shutil
from datetime import datetime, timedelta

downloads_folder = r"C:/Users/HP/Downloads/"
to_delete_folder = r"C:/Users/HP/to_delete/"

# get current date
now = datetime.now()

# loop through all files in downloads folder
for file in os.listdir(downloads_folder):
    # get file path
    file_path = os.path.join(downloads_folder, file)
    print("file_path---->",file_path)
    # get file modification time
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    # check if file is older than 30 days
    if (now - file_mod_time) > timedelta(days=30):
        print("Checking how old the file is?")
        # move file to to_delete folder
        shutil.move(file_path, to_delete_folder)