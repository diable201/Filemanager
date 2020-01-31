import os
import shutil
import fnmatch

from zipfile import ZipFile
from datetime import datetime
from pathlib import Path

path = os.getcwd()  # Path to directory

print(' _____ _ _        __  __ ')
print('|  ___(_) | ___  |  \\/  | __ _ _ __   __ _  __ _  ___ _ __')
print('| |_  | | |/ _ \\ | |\\/| |/ _` |  _ \\ / _` |/ _` |/ _ \\  __|')
print('|  _| | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   ')
print('|_|   |_|_|\\___| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|')
print('                                           |___/')


# Delete File
def delete():
    print('Write the name of file to delete')
    try:
        file = str(input())
        if os.path.isfile(file):
            os.remove(file)
            print('File deleted successfully')
        else:
            print(f'Error: {file} not a valid filename')
    except FileNotFoundError:
        print('File doesnt exist')


# Rename File
def rename():
    print('Enter the name of file')
    try:
        original = str(input())
        remaster = str(input())
        os.rename(original, remaster)
    except FileNotFoundError:
        print('File doesnt exist')


# Read Data
def read_data():
    print('Enter the name of file to read')
    try:
        path_to_file = str(input())
        file = open(path_to_file)
        if file.mode == 'r' or 'rw':
            contents = file.read()
            print(contents)
            file.close()
        else:
            print(f'Error: {file} not a valid')
    except FileNotFoundError:
        print('File doesnt exist')


# Append Data
def append_data():
    print('Enter the name of file to append data')
    try:
        file = str(input())
        with open(file, 'a') as file:
            file.write(str(input()))
        print('Data appended successfully')
    except FileNotFoundError:
        print('File doesnt exist')


# Return to the parent
def return_to_parent():
    print('Enter the name of file')
    try:
        file = str(input())
        path_of_file = Path(file)
        print(path_of_file.parent)
    except FileNotFoundError:
        print('File doesnt exist')


# Overwrite File
def overwrite():
    print('Write the name of file to overwrite')
    try:
        file = str(input())
        with open(file, 'w') as file_overwrite:
            print('Write the content')
            content = str(input())
            file_overwrite.write(content)
        print('File overwritten successfully')
    except FileNotFoundError:
        print('File doesnt exist')


# Copy File
def copy():
    try:
        print('Write the name of file to copy')
        name_of_file = str(input())
        print('Write the name of directory')
        name_of_dir = str(input())
        shutil.copy2(name_of_file, name_of_dir)
        print('File copied successfully')
    except FileNotFoundError:
        print('File doesnt exist')


# Move File
def move():
    try:
        print('Enter the name of file to move')
        old_way = str(input())
        print('Write the name of directory')
        new_way = str(input())
        shutil.move(old_way, new_way)
        print('File moved successfully')
    except FileNotFoundError:
        print('File doesnt exist')


# Extension of files
def file_extension():
    try:
        print('Enter the extension of file. For Example: *.py')
        pattern = str(input())
        print('Pattern:', pattern)
        files = os.listdir('.')
        print('Files:', files)
        print('Matches:', fnmatch.filter(files, pattern))
    except FileNotFoundError:
        print('Extension doesnt exist')


# The Next Commands for Directory


# Rename Directory
def rename_dir():
    print('Enter the name of directory')
    name_of_dir = str(input())
    print('Enter the new name of directory')
    new_name_of_dir = str(input())
    os.rename(name_of_dir, new_name_of_dir)
    print('Directory renamed successfully')


# Print number of files in dir
def number_of_files():
    quantity_of_files = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                quantity_of_files += 1
    print(f'Number of files in directory = {quantity_of_files}')


# Print number of directories in dir
def number_of_dir():
    with os.scandir(path) as entries:
        quantity_of_dir = 0
        for entry in entries:
            if entry.is_dir():
                quantity_of_dir += 1
    print(f'Number of directories in directory = {quantity_of_dir}')


# List content
def list_of_files():
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
            if entry.is_dir():
                print(entry.name)


# Create directory
def create_dir():
    print('Enter the name of new directory')
    dir_name = str(input())
    os.mkdir(dir_name)
    print('Directory created successfully')


# Create file
def create_file():
    print('Enter the name of new file')
    name = str(input())
    with open(name, "w") as file:
        print('File created successfully')
        print('Do you want to write data?')
        print('[1] Yes')
        print('[2] No')
        choice = int(input())
        if choice == 1:
            print('Write your data')
            data = str(input())
            file.write(data)
            print('Data written successfully')
        elif choice == 2:
            file.close()
            print('File closed')


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
            if information.st_size / 1024 / 1024 >= 1:
                print(f'{ENTRY.name}\t Size: {round(information.st_size / 1024 / 1024)}  MB')
            if information.st_size / 1024 >= 1:
                print(f'{ENTRY.name}\t Size: {round(information.st_size / 1024)}  KB')
            else:
                print(f'{ENTRY.name}\t Size: {information.st_size}  Bytes')


# Next commands for Zip archives


# Extract zip
def extract_zip():
    try:
        print('Enter the name of zip. Example: myzip.zip')
        zip_name = str(input())
        with ZipFile(zip_name, 'r') as zip:
            zip.printdir()
            print('Extract files?')
            print('[1] Yes')
            print('[2] No')
            answer = int(input())
            if answer == 1:
                print('Extracting files...')
                zip.extractall()
                print('Files extracted successfully')
            elif answer == 2:
                print('Operation terminated by user')
                return
    except FileNotFoundError:
        print('Zip doesnt exist')


# Get the files from directory for zipping
def get_all_file_paths(directory):
    file_paths = []
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full file_path.
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)
    return file_paths


# Write zip
def write_zip():
    print('Enter the name of directory. Example: Folder')
    directory = str(input())
    file_paths = get_all_file_paths(directory)
    print('The next files will be zipped:')
    for file_name in file_paths:
        print(file_name)
    print('Are you sure to zip this files?')
    print('[1] Yes')
    print('[2] No')
    answer = int(input())
    if answer == 1:
        print('Enter the zip name')
        zip_name = str(input())
        with ZipFile(zip_name, 'w') as zip:
            for file in file_paths:
                zip.write(file)
        print('All files zipped successfully')
    elif answer == 2:
        print('Operation terminated by user')
        return


# Get information about zip
def zip_info():
    print('Enter the zip name. Example: myzip.zip')
    try:
        zip_name = str(input())
        with ZipFile(zip_name, 'r') as zip:
            for info in zip.infolist():
                print(info.filename)
                print('\tSystem:\t\t' + str(info.create_system) + '(0 = WindowsSystem, 3 = UnixSystem)')
                print('\tZIP version:\t' + str(info.create_version))
                print('\tCompressed:\t' + str(info.compress_size) + 'Bytes')
                print('\tUncompressed:\t' + str(info.file_size) + 'Bytes')
    except FileNotFoundError:
        print('Zip doesnt exist')


# Menu
def main():
    while True:
        print(f'Current working directory is: {os.getcwd()}')
        print('With what do you want to work?')
        print('[1] Files')
        print('[2] Directories')
        print('[3] Zip')
        print('[4] Exit')
        select = int(input())
        if select == 1:
            print('Which option ?')
            print('[1] Delete file')
            print('[2] Rename file')
            print('[3] Read data')
            print('[4] Append data')
            print('[5] Return to the parent directory')
            print('[6] Copy file')
            print('[7] Move file')
            print('[8] Overwrite file')
            print('[9] Find extension of files')
            print('Another number to quit')
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
            elif option == 6:
                copy()
            elif option == 7:
                move()
            elif option == 8:
                overwrite()
            elif option == 9:
                file_extension()
            else:
                continue
        if select == 2:
            print('Which option ?')
            print('[1] Rename Directory')
            print('[2] Number of files in Directory')
            print('[3] Number of Directories')
            print('[4] List Content')
            print('[5] Time Modified')
            print('[6] Size of files')
            print('[7] Create directory')
            print('[8] Create file')
            print('Another number to quit')
            option = int(input())
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
                create_dir()
            elif option == 8:
                create_file()
            else:
                continue
        if select == 3:
            print('Which option ?')
            print('[1] Extract Zip')
            print('[2] Create Zip')
            print('[3] Get info about Zip')
            option = int(input())
            if option == 1:
                extract_zip()
            elif option == 2:
                write_zip()
            elif option == 3:
                zip_info()
            else:
                continue
        if select == 4:
            print('  _             ____   ____ ')
            print(' | |__  _   _  / ___| / ___| ')
            print(' |  _ \\| | | | \\___ \\ \\___\\ ')
            print(' | |_)^| |_| |  ___)| ___)|')
            print(' |_.__/ \\__, | |____(_)____/')
            print('        |___/        ')
            exit()
        else:
            continue


if __name__ == '__main__':
    main()