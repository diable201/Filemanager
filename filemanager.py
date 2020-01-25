import os
import fnmatch

path = '/Users/macbookair/Desktop'
for (path, dirs, files) in os.walk(path):
    print(path)
    print(dirs)
    print(files)
s = input("Enter your number")
if s == 0:
    exit(0)
elif s == 1:
    handle = open("can.cpp", "r")
    for line in handle:
        print(line)
    handle.close()
