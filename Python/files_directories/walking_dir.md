# Traversing Directories and Processing Files
## Walking a directory tree and printing the names of the directories and files
````
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
````
os.walk() returns three values on each iteration of the loop:

The name of the current folder

A list of folders in the current folder

A list of files in the current folder

On each iteration, it prints out the names of the subdirectories and files it finds:
````
Found directory: .
test1.txt
test2.txt
Found directory: ./folder_1
file1.py
file3.py
file2.py
Found directory: ./folder_2
file4.py
file5.py
file6.py
````
To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk():
````
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
````
Passing the topdown=False argument will make os.walk() print out the files it finds in the subdirectories first:
````
Found directory: ./folder_1
file1.py
file3.py
file2.py
Found directory: ./folder_2
file4.py
file5.py
file6.py
Found directory: .
test1.txt
test2.txt
````
___
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- V. Ndlovu, Real Python, Working With Files in Python, https://realpython.com/working-with-files-in-python/