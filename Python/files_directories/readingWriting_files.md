## File methods 

| Method | Description |
|--------|-------------|
|close() | Closes an opened file. It has no effect if the file is already closed.
|detach()| Separates the underlying binary buffer from the TextIOBase and returns it.
|fileno()| Returns an integer number (file descriptor) of the file.
|flush() | Flushes the write buffer of the file stream.
|isatty()| Returns True if the file stream is interactive.
|read(n) | Reads at most n characters from the file. Reads till end of file if it is negative or None.
|readable()| Returns True if the file stream can be read from.
|readline(n=-1)| Reads and returns one line from the file. Reads in at most n bytes if specified.
|readlines(n=-1)| Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
|seek(offset,from=SEEK_SET) | Changes the file position to offset bytes, in reference to from (start, current, end).
|seekable() | Returns True if the file stream supports random access.
|tell() | Returns an integer that represents the current position of the file's object.
|truncate(size=None) | Resizes the file stream to size bytes. If size is not specified, resizes to current location.
|writable() | Returns True if the file stream can be written to.
|write(s) | Writes the string s to the file and returns the number of characters written.
|writelines(lines) | Writes a list of lines to the file
___
## Opening Files in Python
Python has a built-in open() function to open a file. This function returns a file object, also called a handle,
as it is used to read or modify the file accordingly.
````python
f = open("test.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path
````
We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to
the file. We can also specify if we want to open the file in text mode or binary mode.

|Mode | Description|
|-----|------------|
|r | Opens a file for reading. (default)
|w | Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
|x | Opens a file for exclusive creation. If the file already exists, the operation fails.
|a | Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
|t | Opens in text mode. (default)
|b | Opens in binary mode.
|+ | Opens a file for updating (reading and writing)
|"r+" | Opens a file for both reading and writing.
|"rb" | Opens a file for reading only in binary format.
|"rb+" | Opens a file for both reading and writing in binary format.
|"a+" | Open for reading and writing.  The file is created if it does not exist.

when working with files in text mode, it is highly recommended to specify the encoding type.
````python
f = open("test.txt", mode='r', encoding='utf-8')
````
## Closing file
Closing a file will free up the resources that were tied with the file. It is done using the close() method.
Python has a garbage collector to clean up unreferenced objects but is better to not rely on it to close the file.
````python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
````
The best solution is to use contex manager:
````python
with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations
   # No need to use close() the contex manager will do it for you!
````
___
## Writing to a file
In order to write into a file in Python, open it in write w, append a or exclusive creation x mode.
!!! w mode overwrites the file if it already exists.
````python
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
````
This program will create a new file named test.txt in the current directory if it does not exist. If it does exist, it is overwritten.
!!! include the newline characters to distinguish the different lines.

```python
txt_data = "I like pizza!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
```
```python
import json

employee = { "name": "Spong",
            "age": 30,
            "job": "cook"}   

file_path = "output.txt"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
```

```python
import csv

employee = [["Name", "age", "job"],
            ["Spong", 30, "Cook"],
            ["Pat", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]] 

file_path = "output.txt"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
for row in employee:
    writer.writerow(row)
```
___
## Reading a file
To read a file in Python use r mode.
````python
test.txt = "This morning I ate 4 cookies.
God i love cookies!
I need more cookies!

f = open("test.txt",'r',encoding = 'utf-8')
f.read(4)    # read the first 4 data
# Output:
'This'
f.read(4)    # read the next 4 data
' mor'
````
If 'n' in read(n) is not specified the method returns up to the end of the file. 
Use a for loop to read the file:
````python
with open("test.txt", "r") as f:
    file = f.read()
    for line in file:
    print(line, end = '') # end ='' to delete \n
````

Alternatively, the readline() method creates a list of items == individual lines of the file including the newline character.
````python
['This morning I ate 4 cookies.\n', 'God i love cookies!\n', 'I need more cookies!\n']
````
```python
file_path = "C/path/to/file.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission!")
```

```python
import json

file_path = "C/path/to/file.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content) or print(content["age"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission!")
```

```python
import csv

file_path = "C/path/to/file.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission!")
```
___
## Reading Multiple Files
Python supports reading data from multiple input streams or from a list of files through the fileinput module.
This module allows to loop over the contents of one or more text files quickly and easily.
````python
import fileinput
for line in fileinput.input()
    process(line)
# fileinput gets its input from command line arguments passed to sys.argv by default.
````
Crude version of UNIX "cat" with fileinput
````python
# File: fileinput-example.py
import fileinput
import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()
````
___
## Reading and writing files with pathlib
We can call .open() on a Path object:
````python
with path.open(mode='r') as f:
    # do something
````
Path.open() is calling the built-in open() behind the scenes.

For simple reading and writing of files, there are a couple of convenience methods in the pathlib library:

|Method | Desc. |
|-------|-------|
|.read_text(): | open the path in text mode and return the contents as a string.
|.read_bytes(): | open the path in binary/bytes mode and return the contents as a bytestring.
|.write_text(): | open the path and write string data to it.
|.write_bytes(): | open the path in binary/bytes mode and write data to it.

Each of these methods handles the opening and closing of the file.
````python
recipe = "C:/Users/raf88/Desktop/cookieRecipie.txt"
Path(recipe).read_text()
'Combine brown sugar, butter, white sugar, and salt in a large bowl; beat with an electric mixer until a creamy...
````
## Sources used for the creation of this cheat sheet
- Programiz, Python File I/O, https://www.programiz.com/python-programming/file-operation
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
