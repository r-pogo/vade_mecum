# Copying, Moving, and Renaming Files and Directories

## Copying Files in Python
shutil.copy() and shutil.copy2().
````
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)
````
shutil.copy() is comparable to the cp command in UNIX based systems. shutil.copy(src, dst) will
copy the file src to the location specified in dst. If dst is a file, the contents of that file are replaced with the
contents of src. If dst is a directory, then src will be copied into that directory. shutil.copy() only copies the
file’s contents and the file’s permissions. Other metadata like the file’s creation and modification times are not preserved.

To preserve all file metadata when copying, use shutil.copy2():
````
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy2(src, dst)
````
Using .copy2() preserves details about the file such as last access time, permission bits, last modification time, and flags.
___

## Copying Directories
shutil.copytree() will copy an entire directory and everything contained in it.
shutil.copytree(src, dest) takes two arguments: a source directory and the destination directory where files and folders will be copied to.
````
>>> import shutil
>>> shutil.copytree('data_1', 'data1_backup')
'data1_backup'
````
In this example, .copytree() copies the contents of data_1 to a new location data1_backup and returns the destination
directory. The destination directory must not already exist. It will be created as well as missing parent directories.
___
## Moving Files and Directories
shutil.move(src, dst).
src is the file or directory to be moved and dst is the destination:
````
>>> import shutil
>>> shutil.move('dir_1/', 'backup/')
'backup'
````
shutil.move('dir_1/', 'backup/') moves dir_1/ into backup/ if backup/ exists. If backup/ does not exist, dir_1/ will be renamed to backup.
___
## Renaming Files and Directories
Python includes os.rename(src, dst) for renaming files and directories:
````
>>> os.rename('first.zip', 'first_01.zip')
The line above will rename first.zip to first_01.zip. If the destination path points to a directory, it will raise an OSError.

OR use rename() from the pathlib module:

>>> from pathlib import Path
>>> data_file = Path('data_01.txt')
>>> data_file.rename('data.txt')

To rename files using pathlib, you first create a pathlib.Path() object that contains a path to the file you want to
replace. The next step is to call rename() on the path object and pass a new filename for the file or directory you’re renaming.
````
___
## Moving and Deleting Files with pathlib

To move a file, use .replace(). Note that if the destination already exists, .replace() will overwrite it. Unfortunately,
pathlib does not explicitly support safe moving of files. To avoid possibly overwriting the destination path, the simplest
is to test whether the destination exists before replacing:
````
if not destination.exists():
    source.replace(destination)
````
However, this does leave the door open for a possible race condition. Another process may add a file at the
destination path between the execution of the if statement and the .replace() method. If that is a concern, a safer
way is to open the destination path for exclusive creation and explicitly copy the source data:
````
with destination.open(mode='xb') as fid:
    fid.write(source.read_bytes())
````
The code above will raise a FileExistsError if destination already exists. Technically, this copies a file.
To perform a move, simply delete source after the copy is done (see below). Make sure no exception was raised though.
When you are renaming files, useful methods might be .with_name() and .with_suffix(). They both return the original path
but with the name or the suffix replaced, respectively.

For instance:
````
>>> path
PosixPath('/home/gahjelle/realpython/test001.txt')
>>> path.with_suffix('.py')
PosixPath('/home/gahjelle/realpython/test001.py')
>>> path.replace(path.with_suffix('.py'))
Directories and files can be deleted using .rmdir() and .unlink() respectively. (Again, be careful!)
````
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/