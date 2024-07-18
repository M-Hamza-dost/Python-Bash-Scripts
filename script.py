import os
import time
import sys
import platform
if len(sys.argv) !=2:
    print(f"Script need 1 aurgument\neg. python {sys.argv[0]} filename")
else:
    file_name=sys.argv[1]
    print(file_name)
    from datetime import datetime as dt
    found=False
    if platform.system()=='Windows':
        dir_path = "C:\\Users\\sc\\Desktop\\python\\day3"
    else:
        dir_path = "/home/hamza/bash"
    for root, directories, files in os.walk(dir_path):
        for file in files:
            if file == file_name:
                creation_time=dt.fromtimestamp(os.path.getctime(os.path.join(root, file))).strftime('%I:%M %p  %d/%m/%Y')
                modified_time=dt.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime('%I:%M %p  %d/%m/%Y')
                print(f"Here is your file with complete path : {os.path.join(root, file)}")
                print(f"{file} was created at {creation_time} and last modified at {modified_time}")   
                found=True
                break
    else:
        if not found:
            print('file not found')