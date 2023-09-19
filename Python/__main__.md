# __main__

```python
# file1.py

print(dir())
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys']

print(f"file1's __name__ is: {__name__}")
file1's __name__ is: __main__

# file2.py
import file1.py
file1's __name__ is: file1
```

```python
# file1.py

def hello():
    print("Hello world")

hello()

# file2.py

from file1 import hello

hello()
# If I run file2.py the output will be:
# Hello world
# Hello world
# It will run twice because it is running the function one in the import from  
# file1.py, which has a call for hello() function  
# and a second time is calle in file2.py
# The file1.py should be modified as follow:

#file1.py
def hello():
    print("Hello world")


if __name__ == '__main__':
hello()

# so the function hello() is called only if we're running directly from file1.py  
# and not when we are importing it. So now it can be called in file2.py and it will  
# only run once
```