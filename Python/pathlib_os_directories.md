# import pathlib
# import os
___
## Slashes and path creation
Windows uses (\)  
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