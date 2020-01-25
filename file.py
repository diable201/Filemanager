import os
import fnmatch
from datetime import datetime
import pathlib

# List
path = '/Users/macbookair/Desktop/Python'
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)


# Convert Unix Time
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


# Time Modified
def get_files():
    dir_entries = os.scandir('/Users/macbookair/Desktop/Python')
    for ENTRY in dir_entries:
        if ENTRY.is_file():
            information = ENTRY.stat()
            print(f'{ENTRY.name}\t Last Modified: {convert_date(information.st_mtime)}')


get_files()

# TODO create menu (if)

# Create Directory
p = pathlib.Path('example_directory')
p.mkdir(exist_ok=True)
