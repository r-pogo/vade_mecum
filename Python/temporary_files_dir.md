# Temporary Files and Directories
Module tempfile.

tempfile can be used to open and store data temporarily in a file or directory while your program is running.
tempfile handles the deletion of the temporary files when your program is done with them.
````
from tempfile import TemporaryFile

# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')
fp.write('Hello universe!')

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()

# Close the file, after which it will be removed
fp.close()
````
In the example above, the mode is 'w+t', which makes tempfile create a temporary text file in write mode.
There is no need to give the temporary file a filename since it will be destroyed after the script is done running.
After writing to the file, you can read from it and close it when you’re done processing it. Once the file is closed,
it will be deleted from the filesystem. If you need to name the temporary files produced using tempfile, use 
tempfile.NamedTemporaryFile().
The temporary files and directories created using tempfile are stored in a special system directory for 
storing temporary files.
Python searches a standard list of directories to find one that the user can create files in.
On Windows, the directories are C:\TEMP, C:\TMP, \TEMP, and \TMP, in that order. On all other platforms, the
directories are /tmp, /var/tmp, and /usr/tmp, in that order. As a last resort, tempfile will save temporary files and
directories in the current directory.
.TemporaryFile() is also a context manager so it can be used in conjunction with the with statement. 
````
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    fp.read()
````
tempfile can also be used to create temporary directories. 
````

>>> import tempfile
>>> with tempfile.TemporaryDirectory() as tmpdir:
...     print('Created temporary directory ', tmpdir)
...     os.path.exists(tmpdir)
...
Created temporary directory  /tmp/tmpoxbkrm6c
True

>>> # Directory contents have been removed
...
>>> tmpdir
'/tmp/tmpoxbkrm6c'
>>> os.path.exists(tmpdir)
False
````
___
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/