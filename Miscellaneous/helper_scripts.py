import zipfile
import glob
import os

def zip_dirs_files(dir_list: list, files_list: list, file_name: str):
    """
    """
    with zipfile.Zipfile(file_name, 'w') as f:
        for i in dir_list:
            print(f'[INFO] Ziping directory: {i}')
            for folder, subfolder, files in os.walk(i):
                for sub in subfolder:
                    f.write(os.path.join(folder, sub))
                for file in files:
                    f.write(os.path.join(folder, file))
        for i in files_list:
            print(f'[INFO] Ziping files: {i}')
            f.write(i)
        f.close()
