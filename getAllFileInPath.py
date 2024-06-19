import os

def get_all_file_paths(directory):
  file_paths = []
  for filename in os.listdir(directory):
    # Construct the full path by joining the directory path and filename
    full_path = os.path.join(directory, filename)

    # Check if it's a file (not a directory) using os.path.isfile
    if os.path.isfile(full_path):
      file_paths.append(full_path)

  return file_paths




def get_all_dirs_paths(directory):
  dir_paths = []
  for filename in os.listdir(directory):
    # Construct the full path by joining the directory path and filename
    full_path = os.path.join(directory, filename)

    # Check if it's a file (not a directory) using os.path.isfile
    if os.path.isdir(full_path):
      dir_paths.append(full_path)

  return dir_paths


def deep_search_file_type(Source_dir, extension):
  list_of_files=[]
  for root, dirs, files in os.walk(Source_dir):
    for filename in files:
      if filename.endswith(extension):
        list_of_files.append(root+"/"+filename)
  return list_of_files

