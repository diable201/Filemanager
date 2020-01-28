import os
import shutil

from datetime import datetime
from pathlib import Path

path = '/home/sanzhar/Загрузки/filemanager-master'  # path to directory

print('_____ _ _        __  __ ')
print('|  ___(_) | ___  |  \\/  | __ _ _ __   __ _  __ _  ___ _ __')
print('| |_  | | |/ _ \\ | |\\/| |/ _` |  _ \\ / _` |/ _` |/ _ \\  __|')
print('|  _| | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   ')
print('|_|   |_|_|\\___| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|')
print('                                           |___/')


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
    path_to_file = str(input())
    file = open(path_to_file)
    if file.mode == 'r' or 'rw':
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
def rename_dir():
    path_of_dir = str(input())
    name_of_dir = Path(path_of_dir)
    name_of_dir.rename('example_directory_2')


# Print number of files in dir
def number_of_files():
    quantity_of_files = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                quantity_of_files += 1
                print(entry.name, quantity_of_files)
    print(quantity_of_files)

   
# Print number of directories in dir
def number_of_dir():
    with os.scandir(path) as entries:
        quantity_of_dir = 0
        for entry in entries:
            if entry.is_dir():
                quantity_of_dir += 1
                print(entry.name, quantity_of_dir)
    print(quantity_of_dir)


# List content
def list_of_files():
    with os.scandir(path) as entries:
        quantity_of_files = 0
        quantity_of_dir = 0
        for entry in entries:
            if entry.is_file():
                quantity_of_files += 1
                print(entry.name, quantity_of_files)
            if entry.is_dir():
                quantity_of_dir += 1
                print(entry.name, quantity_of_dir)


# Move file
def move():
    old_way = str(input())
    new_way = str(input())
    shutil.move(old_way, new_way)


# shutil.copy()
# Rename file or dir
# os.rename('first.zip', 'first_01.zip')

# Create file or dir
def create():
    dir_name = str(input())
    os.mkdir(dir_name)
    file_name = str(input())
    open(file_name, 'rw')


# Convert Unix Time
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


# Time Modified
def time():
    dir_entries = os.scandir(path)
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Last Modified: {convert_date(information.st_mtime)}')


# Size Modified
def size():
    dir_entries = os.scandir(path)
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Size: {information.st_size}')


print("With what do you want to work?")
print("[1] Files")
print("[2] Directories")
select = int(input())


if select == 1:
    print('which option?')
    print('[1] Delete file')
    print('[2] Rename file')
    print('[3] Read data')
    print('[4] Append data')
    print('[5] Return to the parent directory')
    option = int(input())
    if option == 1:
        delete()
    elif option == 2:
        rename()
    elif option == 3:
        read_data()
    elif option == 4:
        append_data()
    elif option == 5:
        return_to_parent()
if select == 2:
    option = str(input())
    print('which option')
    print('[1] Rename Directory', option)
    print('[2] Number of files in Directory', option)
    print('[3] Number of Directories', option)
    print('[4] List Content', option)
    print('[5] Time Modified', option)
    print('[6] Size of files', option)
    print('[7] Create file or directory')
    if option == 1:
        rename_dir()
    elif option == 2:
        number_of_files()
    elif option == 3:
        number_of_dir()
    elif option == 4:
        list_of_files()
    elif option == 5:
        time()
    elif option == 6:
        size()
    elif option == 7:
        create()
