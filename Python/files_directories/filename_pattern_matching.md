# Filename Pattern Matching

These are the methods and functions available to search for
files that match a particular pattern.

| Function | Description |
|----------|-------------|
| startswith() | Tests if a string starts with a specified pattern and returns True or False
| endswith() | Tests if a string ends with a specified pattern and returns True or False
| fnmatch.fnmatch(filename, pattern) | Tests whether the filename matches the pattern and returns True or False
| glob.glob() | Returns a list of filenames that match a pattern
| pathlib.Path.glob() | Finds patterns in path names and returns a generator object
---
## String method .startswith() and .endswith()

To do this, first get a directory listing and then iterate over it:
````python
>>> import os

>>> # Get .txt files
>>> for f_name in os.listdir('some_directory'):
...     if f_name.endswith('.txt'):
...         print(f_name)

# Output:
data_01.txt
data_03.txt
data_03_backup.txt
data_02_backup.txt
data_02.txt
data_01_backup.txt
````
___
## Filename Pattern Matching Using fnmatch
````python
>>> import os
>>> import fnmatch

>>> for file_name in os.listdir('some_directory/'):
...     if fnmatch.fnmatch(file_name, '*.txt'):
...         print(file_name)

# This iterates over the list of files in some_directory and uses .fnmatch() to perform a wildcard search for files that
# have the .txt extension.

>>> for filename in os.listdir('.'):
...     if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
...         print(filename)
````
___
## Filename Pattern Matching Using glob

.glob() treats files beginning with a period (.) as special.
UNIX and related systems translate name patterns with wildcards like ? and * into a list of files. This is called globbing.
For example, typing mv `*`.py python_files/ in a UNIX shell moves (mv) all files with the .py extension from the current
directory to the directory python_files. The * character is a wildcard that means “any number of characters,” and `*`.py
is the glob pattern. This shell capability is not available in the Windows Operating System.  
Asterisk `(*)`: Matches zero or more characters  
Question Mark `(?)` Matches any single character  
Square brackets `[]` Matches any character in the sequence.  
`[!]` Matches any character not in sequence  
The glob module adds this capability in Python, which enables Windows programs to use this feature.

| Function | Description |
|----------|-------------|
| glob.glob(pathname) | Returns a list of files that matches the path specified in the function argument
| glob.iglob(pathname) | Return a generator object that we can iterate over and get the individual file names
| glob.escape(pathname) | Useful especially in the case of the filenames with special characters

Syntax of glob() function
````python
glob.glob(pathname, *, recursive=False)
````
Here’s an example of how to use glob to search for all Python (.py) source files in the current directory:
````python
>>> import glob
# relative path
>>> glob.glob('*.py')
['admin.py', 'tests.py']

# absolute path to search all text files inside a specific folder
path = r'C:/User/cookieMonster/test
print(glob.glob(path))
````
glob.glob('*.py') searches for all files that have the .py extension in the current directory and returns them as a
list. glob also supports shell-style wildcards to match patterns:
````python
>>> import glob
>>> for name in glob.glob('*[0-9]*.txt'):
...     print(name)
````
glob makes it easy to search for files recursively in subdirectories too:
````python
import glob

# path to search file
path = '**/*.txt'
for file in glob.glob(path, recursive=True):
    print(file)
# OR

>>> import glob
>>> for file in glob.iglob('**/*.py', recursive=True):
...     print(file)
````

This example makes use of glob.iglob() to search for .py files in the current directory and subdirectories.
Passing recursive=True as an argument to .iglob() makes it search for .py files in the current directory and any subdirectories.
The difference between glob.iglob() and glob.glob() is that .iglob() returns an iterator instead of a list.
````python
from pathlib import Path
>>> p = Path('.')
>>> for name in p.glob('*.p*'):
...     print(name)

# Output:
admin.py
scraper.py
docs.pdf
````
Calling `p.glob('*.p*')` returns a generator object that points to all files in the current directory that start with the
letter p in their file extension. Path.glob() is similar to os.glob() discussed above.

In addition to the character and numeric ranges, we have the escape() method to enable the pattern inside the glob() 
with special characters
````python
import glob

print("All JPEG's files")
print(glob.glob("*.jpeg"))

print("JPEGs files with special characters in their name")
# set of special characters _, $, #
char_seq = "_$#"
for char in char_seq:
    esc_set = "*" + glob.escape(char) + "*" + ".jpeg"
    for file in (glob.glob(esc_set)):
        print(file)
````
We can search files having different extensions using the glob module
````python
import glob

print("All pdf and txt files")
extensions = ('*.pdf', '*.jpeg')
files_list = []
for ext in extensions:
    files_list.extend(glob.glob(ext))
print(files_list)
````
Using glob() with regex
````python
import glob
import re

num = input('Enter the employee number ')
# [a-z] for any employee name
# {file_name} is the employee number
regex = r'[a-z_]+{file_num}.*'.format(file_num=num)

# search emp jpeg in employees folder
for file in glob.glob("2020/*"):
    if re.search(regex, file):
        print('Employee Photo:', file)
````
glob for finding text in files  
Example: Search word profit in files
````python
import glob

# Look all txt files of current directory and its sub-directories
path = '**/*.txt'
search_word = 'profit'
# list to store files that contain matching word
final_files = []
for file in glob.glob(path, recursive=True):
    try:
        with open(file) as fp:
            # read the file as a string
            data = fp.read()
            if search_word in data:
                final_files.append(file)
    except:
        print('Exception while reading file')
print(final_files)
````
Sorting the glob() output  
````python
import glob
path = "*.txt"
print(sorted(glob.glob(path)))
````
We can sort the files based on the date and time of modification by combining the glob() method with the getmtime() method in the os module.
````python
import glob
import os

# List all files and folders in the current  directory
files = glob.glob(os.path.expanduser("*"))

# Sort by modification time (mtime) ascending and descending

files_ascending = sorted(files, key=lambda t: os.stat(t).st_mtime)
print(files_ascending)
files_descending = sorted(files, key=lambda t: -os.stat(t).st_mtime)
print(files_descending)
````
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/
- Vishal, PYnative Python Programming, Python Glob: Filename Pattern Matching, https://pynative.com/python-glob/