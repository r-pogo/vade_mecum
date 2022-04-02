# import pathlib
# import os
___
## Slashes and path creation
Windows uses ('\')  
macOS and Linux uses (/)  
Path() uses its own separators to generate the path, guarantees that the code will run properly on all operating systems
````
>>> from pathlib import Path
>>> Path('cookies','milk', 'breakfast')
>>> WindowsPath('cookies/milk/breakfast')
# for macOS and Linux Path(0 creates PosixPath object
>>> str(Path('cookies','milk', 'breakfast'))
>>> 'cookies\\milk\\breakfast'
````
(r'cookies\milk') in Windows refer to two directories or milk file inside cookies dir
while in macOS/Linux refer o one directory called cookies\milk.  
NB: this is the reason why is better to avoid '\' in python scripts  

'/' also to join the parts of the path when constructing it:
````
>>> from pathlib import Path
>>> Path('cookies') / 'milk' / 'butter'
>>> WindowsPath('cookies/milk/butter')
>>> Path('cookies')/Path('bacon/eggs')
>>> WindowsPath('cookies/bacon/eggs')
>>> Path('cookies')/Path('more', 'cookies')
>>> WindowsPath('cookies/more/cookies')
````

You can also create a path from it string representation:
````
>>> pathlib.Path(r'C:\Users\cookieMonster\cookiesJar\file.txt')
>>>WindowsPath('C:/Users/cookieMonster/cookiesJar/file.txt')
````
___
## Current and home directory
Current directory
````
>>> from pathlib import Path
>>> import os
>>> Path.cwd()
>>> WindowsPath('C:\Users\user_name\Desktop\cheat_sheets')
# for changing the directory
>>> os.chdir('C:/Windows/System32')
>>> Path.cwd()
>>> WindowsPath('C:/Windows/System32')
````
Home directory
````
>>> Path.home()
>>> WindowsPath('C:/Users/cookieMonster')
````
___
## Absolute and relative path
````
from pathlib import Path
Path.cwd()
WindowsPath('C:/Users/raf88/Desktop/cheat_sheets')
Path.cwd().is_absolute()
True
Path('cookies/bacon/honey').is_absolute()
False
````
Example on how to obtain an absolute path
````
Path('cookies/bacon/honey')
WindowsPath('cookies/bacon/honey')
Path.cwd() / Path('cookies/bacon/honey')
WindowsPath('C:/Users/cookieMonster/Desktop/cheat_sheets/cookies/bacon/honey')

# OR
Path.home() / Path('cookies/bacon/honey')
WindowsPath('C:/Users/raf88/cookieMonster/bacon/honey')
````
Also, os.path contains some useful functions to work with absolute/relative paths:
````
os.path.abspath('cookies/bacon/honey')
'C:\\Users\\raf88\\Desktop\\cheat_sheets\\cookies\\bacon\\honey'
os.path.isabs('cookies/bacon/honey')
False
os.path.relpath('C:/Windows')
'..\\..\\..\\..\\Windows'
os.path.relpath('C:/Windows', 'C:/')
'Windows
````
___
## Checking the correctness of the paths
````
ok_dir = Path("C:/Users/raf88/Desktop/cheat_sheets")
not_ok_dir = Path("C:/Users/cookieMonster/Desktop/cheat_sheets")
not_ok_dir.exists()
False
ok_dir.exists()
True
ok_dir.is_dir()
True
ok_dir.is_file()
````
___
## Fetching fragments of a path
The different parts of a path are conveniently available as properties. Basic examples include:
.name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories
.parents: An immutable sequence providing access to the logical ancestors of the path

from pathlib import path
````
c = Path("C:/Users/cookieMonster/Desktop/cookieRecipie.txt")
c.anchor
'C:\\'
c.parent ---> this is the only one that gives another Path object
WindowsPath('C:/Users/cookieMonster/Desktop')
c.name
'cookieRecipie.txt'
c.suffix
'.txt'
c.drive ---> only for Windows
'C:'
````
"parents" attribute is something completely different from "parent":
````
c = Path("C:/Users/cookieMonster/Desktop/cookieRecipie.txt")
c.parents[0]
WindowsPath('C:/Users/cookieMonster/Desktop')
c.parents[1]
WindowsPath('C:/Users/cookieMonster')
c.parents[2]
WindowsPath('C:/Users')
````
import os
````
c = "C:/Users/cookieMonster/Desktop/cookieRecipie.txt"
os.path.basename(c)
'cookieRecipie.txt'
os.path.dirname(c)
'C:/Users/cookieMonster/Desktop'
os.path.split(c)
('C:/Users/cookieMonster/Desktop', 'cookieRecipie.txt')
(os.path.dirname(c), os.path.basename(c))
('C:/Users/cookieMonster/Desktop', 'cookieRecipie.txt')

# also useful
c.split('/')
['C:', 'Users', 'cookieMonster', 'Desktop', 'cookieRecipie.txt']
````
____
## Making Directories

| Function | Description |
|----------|-------------|
|os.mkdir()|  Creates a single subdirectory
|pathlib.Path.mkdir()| Creates single or multiple directories
|os.makedirs()| Creates multiple directories, including intermediate directories
___
### Creating single directories
````
import os
os.mkdir('C:/delicious/chocolate/cookies')

from pathlib import Path
Path('C:/delicious/chocolate/cookies').mkdir()

# with try and except blok:
from pathlib import Path
p = Path('C:/delicious/chocolate/cookies')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)

# if you want to ignore if the directory already exist
#By default python raise an OSError if the target directory already exists.
from pathlib import Path
p = Path('C:/delicious/chocolate/cookies')
p.mkdir(exist_ok=True)
````
___
### Creating Multiple Directories
os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs() create
individual directories, it can also be used to create directory trees. In other words, it can create any necessary
intermediate folders in order to ensure a full path exists.
````
import os
os.makedirs('cookies/butter/milk')
````
This will create a nested directory structure that contains the folders 2018, 10, and 05
````
.  
|  
└── cookies/  
    └── butter/  
        └── milk/  
````
makedirs() uses default permissions, if you want to have directories with different permissions pass the right mode when calling makedirs().
````
import os
os.makedirs('cookies/butter/milk', mode=0o770)
````
````
patlib.Path()
import pathlib
p = pathlib.Path('cookies/butter/milk')
p.mkdir(parents=True)
````
Passing parents=True to Path.mkdir() makes it create the directory milk and any parent directories necessary to make the path valid.
___
## Directory Listing 
| Function | Description |
|----------|-------------|
|os.listdir() | Returns a list of all files and folders in a directory
|os.scandir() | Returns an iterator of all the objects in a directory including file attribute information
|pathlib.Path.iterdir() | Returns an iterator of all the objects in a directory including file attribute information

With os
````
import os
dirs = os.scandir('../cheat_sheets')
for dir in dirs:
    print(dir)
Output:
<DirEntry '.git'>
<DirEntry '.gitignore'>
<DirEntry '.idea'>
<DirEntry 'Python'>
<DirEntry 'README.md'>

with os.scandir('../cheat_sheets') as dirs:
    for dir in dirs:
        print(dir.name)
Output:
.git
.gitignore
.idea
Python
README.md
````
os.scandir() is used in conjunction with the with statement because it supports the context manager protocol.

With pathlib
````
from pathlib import Path
entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)
 ````
pathlib.Path() objects have an .iterdir() method for creating an iterator of all files and folders in a directory.
Each entry yielded by .iterdir() contains information about the file or directory such as its name and file attributes.
___
## Listing Subdirectiories
List all subdirectories using scandir()
````
import os
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
````
Listing Subdirectories with pathlib.Path()
````
from pathlib import Path

basepath = Path('my_directory/')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
````
___
## Listing All Files in a Directory 
List all files in a directory using scandir()
````
import os

basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
````
Listing All Files in a Directory with pathlib.Path()
````
from pathlib import Path

basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
OR

from pathlib import Path

basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)
````
___
## Getting file attributes
with os.scandir()
````
import os
with os.scandir('my_directory/') as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime
````
with pathlib.Path()
````
from pathlib import Path
current_dir = Path('my_directory')
for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)
````
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/
- Python documentation, https://docs.python.org/3/library/pathlib.html