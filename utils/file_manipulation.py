import sys
import os

def create_file(file_path):
    file_name = file_path.split('/')[-1]
    dir_path = file_path.replace(file_name, '')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    if os.path.exists(file_path):
        open(file_path, 'w').close()
    else:
        open(file_path, 'x').close()


def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        print('File does not exist: {}'.format(file_path))
        sys.exit(1)


