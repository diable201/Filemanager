import os
import shutil

from datetime import datetime

path = '/Users/macbookair/Downloads/filemanager-master'  # path to directory
data_file = '/Users/macbookair/Downloads/filemanager-master'

print('_____ _ _        __  __ ')
print('|  ___(_) | ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __')
print('| |_  | | |/ _ \ | |\/| |/ _` |  _ \ / _` |/ _` |/ _ \  __|')
print('|  _| | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   ')
print('|_|   |_|_|\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|')
print('                                           |___/')

print("With what do you want to work?")
select = str(input())
print("[1] Files", select)
print("[2] Directories", select)


def delete():
    pass


if select == 1:
    option = str(input())

    print('which option?')
    print('[1] Delete file', option)
    print('[2] Rename file', option)
    print('[3] Read data', option)
    print('[4] Append data', option)
    print('[5] Return to the parent directory', option)


# If the file exists, delete it
def delete():
    print("write the name of file to delete")
    file = str(input())
    if os.path.isfile(file):
        os.remove(file)
    else:
        print(f'Error: {file} not a valid filename')


# Rename File
def rename():
    original = str(input())
    remaster = str(input())
    os.rename(original, remaster)


# Read Data
def read_data():
    file = open('ex5.txt')
    if file.mode == 'r':
        contents = file.read()
        print(contents)


# or perhaps use this
# with open('ex5.txt', 'r') as file:
#     data = file.readlines()
#     print(data)


# Append Data
def append_data():
    file = str(input())
    with open(file, 'a') as file:
        file.write(str(input()))  # omg this is works


# Return to the parent
def return_to_parent():
    from pathlib import Path
    path_of_file = str(input())
    path.parent = Path(path_of_file)
    print(path.parent)


# The Next Commands for Directory


# Rename Directory
# def rename_dir():
#     path_of_dir = str(input())
#     data_file = Path(path_of_dir)
#     data_file.rename('example_directory_2')


# Print number of files in dir
def number_of_files():
    path = '/Users/macbookair/Downloads/filemanager-master'
    number_of_files = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                number_of_files += 1
                print(entry.name)
    print(number_of_files)


# Print number of directories in dir
def number_of_dir():
    path = '/Users/macbookair/Downloads/filemanager-master'
    with os.scandir(path) as entries:
        number_of_dir = 0
        for entry in entries:
            if entry.is_dir():
                number_of_dir += 1
                print(entry.name)
    print(number_of_dir)


# List content
def list():
    path = '/Users/macbookair/Downloads/filemanager-master'
    with os.scandir(path) as entries:
        number_of_f = 0
        for entry in entries:
            if entry.is_file():
                number_of_f += 1
                print(entry.name, number_of_f)
            if entry.is_dir():
                print(entry.name)


# Move file
def move():
    shutil.move('dir_1/', 'backup/')


# shutil.copy()
# Rename file or dir
# os.rename('first.zip', 'first_01.zip')

# Create file or dir
def create():
    dir_name = str(input())
    os.mkdir(dir_name)
    file_name = str(input())
    file = open(file_name, 'rw')


# Convert Unix Time
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


# Time Modified
def time():
    dir_entries = os.scandir('/Users/macbookair/Downloads/filemanager-master')
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Last Modified: {convert_date(information.st_mtime)}')


# Size Modified
def size():
    dir_entries = os.scandir('/Users/macbookair/Downloads/filemanager-master')
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Size: {information.st_size}')
