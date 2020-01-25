import os
import fnmatch
from datetime import datetime
import pathlib
import glob
import shutil
from pathlib import Path


# List
path = '/home/sanzhar/Загрузки/filemanager-master'
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
        if entry.is_dir():
            print(entry.name)

# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)


# List all files in a directory using os.listdir
basepath = path
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)


for file_name in os.scandir(path):
    if fnmatch.fnmatch(file_name, '*.py'):
        print(file_name)


# Convert Unix Time
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


# Time Modified
def get_files():
    dir_entries = os.scandir('/home/sanzhar/Загрузки/filemanager-master')
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Last Modified: {convert_date(information.st_mtime)} Size: {information.st_size}')


# Read File
with open('README.md', 'r') as f:
    data = f.read()
    print(data)

get_files()

# TODO create menu (if)

# Create Directory
p = pathlib.Path('example_directory')
p.mkdir(exist_ok=True)

data_file = 'home/data.txt'

for file in glob.iglob('**/*.txt', recursive=True):
    print(file)


# Copy file
src = '/home/sanzhar/Загрузки/filemanager-master/example_directory/ex.txt'
dst = '/home/sanzhar/Загрузки/filemanager-master/'
shutil.copy2(src, dst)
shutil.move('dir_1/', 'backup/')


# Get .txt files
for f_name in os.listdir('some_directory'):
    if f_name.endswith('.txt'):
        print(f_name)


# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')
