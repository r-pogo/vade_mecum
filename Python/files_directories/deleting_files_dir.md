# Deleting Files and Directories

| Function | Description |
|----------|-------------|
| os.remove() | Deletes a file and does not delete directories
| os.unlink() | Is identical to os.remove() and deletes a single file
| pathlib.Path.unlink() | Deletes a file and cannot delete directories
| os.rmdir() | Deletes an empty directory
| pathlib.Path.rmdir() | Deletes an empty directory
| shutil.rmtree() | Deletes entire directory tree and can be used to delete non-empty directories
___
## Files
To delete a single file: pathlib.Path.unlink(), os.remove(). or os.unlink().

os.remove() and os.unlink() are semantically identical. 
To delete a file using os.remove():
````python
import os
data_file = 'C:\\Users\\cookeMonster\\Desktop\\Test\\data.txt'
os.remove(data_file)

# Deleting a file using os.unlink():

import os
data_file = 'C:\\Users\\cookeMonster\\Desktop\\Test\\data.txt'
os.unlink(data_file)
````
Calling .unlink() or .remove() on a file deletes the file from the filesystem. These two functions will throw an OSError
if the path passed to them points to a directory instead of a file. To avoid this, you can either check that what you’re
trying to delete is actually a file and only delete it if it is, or you can use exception handling to handle the OSError:
````python
import os
data_file = 'home/data.txt'
# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')

# OR

import os
data_file = 'home/data.txt'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}
````
pathlib.Path.unlink() to delete files:
````python
from pathlib import Path
data_file = Path('home/data.txt')

try:
    data_file.unlink()
except IsADirectoryError as e:
    print(f'Error: {data_file} : {e.strerror}')
````
## Deleting Directories
For deleting directories: os.rmdir(), pathlib.Path.rmdir(), shutil.rmtree()  

To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the directory
you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. 
````python
import os

trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
# Here, the trash_dir directory is deleted by passing its path to os.rmdir(). If the directory isn’t empty, an error
# message is printed to the screen:

# Traceback (most recent call last):
#   File '<stdin>', line 1, in <module>
# OSError: [Errno 39] Directory not empty: 'my_documents/bad_dir'


# Alternatively, you can use pathlib to delete directories:

from pathlib import Path

trash_dir = Path('my_documents/bad_dir')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
    
# Here, you create a Path object that points to the directory to be deleted. Calling .rmdir() on the Path object will
# delete it if it is empty.
````
To delete non-empty directories and entire directory trees: shutil.rmtree():
````python
import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
    
# Everything in trash_dir is deleted when shutil.rmtree() is called on it.
# There may be cases where you want to delete empty folders recursively. You can do this using one of the methods
# discussed above in conjunction with os.walk():

import os
for dirpath, dirnames, files in os.walk('.', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError as ex:
        pass
````
These walks down the directory tree and tries to delete each directory it finds. If the directory isn’t empty, an
OSError is raised and that directory is skipped.

Deleting files using glob()
````python
import glob
import os

# delete all pdf files
for pdf in (glob.glob("2020/*.pdf")):
    # Removing the pdf file from the directory
    print("Removing ", pdf)
    os.remove(pdf)
````
___
## Safe deletion of data
````python
import send2trash
baconFile = open("bacon.txt", 'a')
baconFile.write("Bacon is good for your soul")
baconFile.close()
send2trash.send2trash('bacon.txt')
````
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/
