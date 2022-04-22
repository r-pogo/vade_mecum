# Zip and Tar
## Reading ZIP Files
The zipfile module has functions that make it easy to open and extract ZIP files. 
To read the contents of a ZIP file, the first thing to do is to create a ZipFile object. 
ZipFile objects are similar to file objects created using open(). ZipFile is also a context manager and
therefore supports the with statement:
````python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    zipobj.namelist()
# This produces a list:

['file1.py', 'file2.py', 'file3.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
````
.namelist() returns a list of names of the files and directories in the archive. To retrieve information about the
files in the archive, use .getinfo():
````python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('sub_dir/bar.py')
    bar_info.file_size
````
___
## Extracting ZIP Archives
The zipfile module allows you to extract one or more files from ZIP archives through .extract() and .extractall().
````python
>>> import zipfile
>>> import os

>>> os.listdir('.')
['data.zip']

>>> data_zip = zipfile.ZipFile('data.zip', 'r')

>>> # Extract a single file to current directory
>>> data_zip.extract('file1.py')
'/home/terra/test/dir1/zip_extract/file1.py'

>>> os.listdir('.')
['file1.py', 'data.zip']

>>> # Extract all files into a different directory
>>> data_zip.extractall(path='extract_dir/')

>>> os.listdir('.')
['file1.py', 'extract_dir', 'data.zip']

>>> os.listdir('extract_dir')
['file1.py', 'file3.py', 'file2.py', 'sub_dir']

>>> data_zip.close()
````
The third line of code is a call to os.listdir(), which shows that the current directory has only one file, data.zip.
Next, you open data.zip in read mode and call .extract() to extract file1.py from it. .extract() returns the full file
path of the extracted file. Since there’s no path specified, .extract() extracts file1.py to the current directory.
The next line prints a directory listing showing that the current directory now includes the extracted file in addition
 to the original archive. The line after that shows how to extract the entire archive into the zip_extract directory.
 .extractall() creates the extract_dir and extracts the contents of data.zip into it. The last line closes the ZIP archive.
___
## Extracting Data From Password-Protected Archives
zipfile supports extracting password-protected ZIPs. To extract password-protected ZIP files, pass in the password to
the .extract() or .extractall() method as an argument:
````python
>>> import zipfile

>>> with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
...     # Extract from a password protected archive
...     pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')
````
___
## Creating New ZIP Archives
````python
>>> import zipfile

>>> file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
>>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
...     for name in file_list:
...         new_zip.write(name)
````
In the example, new_zip is opened in write mode and each file in file_list is added to the archive.
Opening a ZIP file in write mode erases the contents of  the archive and creates a new archive.
````python
>>> # Open a ZipFile object in append mode
>>> with zipfile.ZipFile('new.zip', 'a') as new_zip:
...     new_zip.write('data.txt')
...     new_zip.write('latin.txt')
````
___
## Opening TAR Archives
TAR files are uncompressed file archives like ZIP. They can be compressed using gzip, bzip2, and lzma compression methods.
The TarFile class allows reading and writing of TAR archives.
````python
import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames())
````
tarfile objects open like most file-like objects. They have an open() function that takes a mode that determines how the file is to be opened.

| Mode | Action |
|------|--------|
| r    |   Opens archive for reading with transparent compression
| r:gz |   Opens archive for reading with gzip compression
| r:bz2|   Opens archive for reading with bzip2 compression
| r:xz |   Opens archive for reading with lzma compression
| w    |   Opens archive for uncompressed writing
| w:gz |   Opens archive for gzip compressed writing
| w:xz |   Opens archive for lzma compressed writing
| a    |   Opens archive for appending with no compression

.open() defaults to 'r' mode. To read an uncompressed TAR file and retrieve the names of the files in it, use .getnames():
````python
>>> import tarfile

>>> tar = tarfile.open('example.tar', mode='r')
>>> tar.getnames()
['CONTRIBUTING.rst', 'README.md', 'app.py']
# This returns a list with the names of the archive contents.
````
The metadata of each entry in the archive can be accessed using special attributes:
````python
>>> for entry in tar.getmembers():
...     print(entry.name)
...     print(' Modified:', time.ctime(entry.mtime))
...     print(' Size    :', entry.size, 'bytes')
...     print()
CONTRIBUTING.rst
 Modified: Sat Nov  1 09:09:51 2018
 Size    : 402 bytes

README.md
 Modified: Sat Nov  3 07:29:40 2018
 Size    : 5426 bytes

app.py
 Modified: Sat Nov  3 07:29:13 2018
 Size    : 6218 bytes
````
___
## Extracting Files From a TAR Archive
To extract files from TAR archives:.extract(), .extractfile(), .extractall()
To extract a single file from a TAR archive, use extract(), passing in the filename:
````python
>>> tar.extract('README.md')
>>> os.listdir('.')
['README.md', 'example.tar']
````
The README.md file is extracted from the archive to the file system. Calling os.listdir() confirms that README.md 
file was successfully extracted into the current directory. To unpack or extract everything from the archive, use 
.extractall():
````python
>>> tar.extractall(path="extracted/")
````
.extractall() has an optional path argument to specify where extracted files should go. Here, 
the archive is unpacked into the extracted directory. The following commands show that the archive 
was successfully extracted:
````
$ ls
example.tar  extracted  README.md

$ tree
.
├── example.tar
├── extracted
|   ├── app.py
|   ├── CONTRIBUTING.rst
|   └── README.md
└── README.md

1 directory, 5 files

$ ls extracted/
app.py  CONTRIBUTING.rst  README.md
````
To extract a file object for reading or writing, use .extractfile(), which takes a filename or TarInfo object to extract
as an argument. .extractfile() returns a file-like object that can be read and used:
````python
>>> f = tar.extractfile('app.py')
>>> f.read()
>>> tar.close()
````
___
## Creating New TAR Archives
````python
>>> import tarfile

>>> file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
>>> with tarfile.open('packages.tar', mode='w') as tar:
...     for file in file_list:
...         tar.add(file)

>>> # Read the contents of the newly created archive
>>> with tarfile.open('package.tar', mode='r') as t:
...     for member in t.getmembers():
...         print(member.name)
app.py
config.py
CONTRIBUTORS.md
tests.py
````
To add new files to an existing archive, open the archive in append mode ('a'):
````python
>>> with tarfile.open('package.tar', mode='a') as tar:
...     tar.add('foo.bar')

>>> with tarfile.open('package.tar', mode='r') as tar:
...     for member in tar.getmembers():
...         print(member.name)
app.py
config.py
CONTRIBUTORS.md
tests.py
foo.bar
````
___
## Working With Compressed
tarfile can also read and write TAR archives compressed using gzip, bzip2, and lzma compression. To read or write to a
compressed archive, use tarfile.open(), passing in the appropriate mode for the compression type.

For example, to read or write data to a TAR archive compressed using gzip, use the 'r:gz' or 'w:gz' modes respectively:
````python
>>> files = ['app.py', 'config.py', 'tests.py']
>>> with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
...     tar.add('app.py')
...     tar.add('config.py')
...     tar.add('tests.py')

>>> with tarfile.open('packages.tar.gz', mode='r:gz') as t:
...     for member in t.getmembers():
...         print(member.name)
app.py
config.py
tests.py
````
The 'w:gz' mode opens the archive for gzip compressed writing and 'r:gz' opens the archive for gzip compressed reading.
Opening compressed archives in append mode is not possible. To add files to a compressed archive, you have to create a new archive.
___
## An Easier Way of Creating Archives

The Python Standard Library also supports creating TAR and ZIP archives using the high-level methods in the shutil module.
The archiving utilities in shutil allow you to create, read, and extract ZIP and TAR archives. These utilities 
rely on the lower level tarfile and zipfile modules.

shutil.make_archive() takes at least two arguments: the name of the archive and an archive format.

By default, it compresses all the files in the current directory into the archive format specified in the format argument.
You can pass in an optional root_dir argument to compress files in a different directory. .make_archive()
supports the zip, tar, bztar, and gztar archive formats.
````python
import shutil

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('data/backup', 'tar', 'data/')
# This copies everything in data/ and creates an archive called backup.tar in the filesystem and returns its name.
# To extract the archive, call .unpack_archive():

shutil.unpack_archive('backup.tar', 'extract_dir/')
````
Calling .unpack_archive() and passing in an archive name and destination directory extracts the contents of backup.tar
into extract_dir/. ZIP archives can be created and extracted in the same way.
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/