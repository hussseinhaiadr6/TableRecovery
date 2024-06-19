import os

def remove_empty_directories(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f'Removed empty directory: {dir_path}')


import os
import shutil
import re


def flatten_and_rename(root_directory):
    for chunk_dir in os.listdir(root_directory):
        chunk_path = os.path.join(root_directory, chunk_dir)

        if os.path.isdir(chunk_path):
            image_counter = {}
            print(f"Processing directory: {chunk_path}")

            for root, dirs, files in os.walk(chunk_path, topdown=False):
                for file in files:
                    if file.endswith(('.jpg', '.jpeg', '.png')):
                        page_dir = os.path.basename(root)
                        match = re.match(r'page(\d+)', page_dir)
                        if match:
                            page_number = match.group(1)
                            table_number = image_counter.get(page_number, 0)
                            new_name = f'{chunk_dir}_Page{page_number}_Table{table_number}.jpg'
                            old_path = os.path.join(root, file)
                            new_path = os.path.join(chunk_path, new_name)
                            shutil.move(old_path, new_path)
                            print(f'Renamed {old_path} to {new_path}')
                            image_counter[page_number] = table_number + 1

                # Remove empty directories
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    if not os.listdir(dir_path):
                        os.rmdir(dir_path)
                        print(f'Removed empty directory: {dir_path}')


# Replace this with your actual path
"""tables_detected_path = "./Tables_Detected"
flatten_and_rename(tables_detected_path)
"""