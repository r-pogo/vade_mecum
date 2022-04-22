# Shelve
full doc:https://docs.python.org/3/library/shelve.html
It allows you to write variables to database-like binary files
````python
import shelve
shelFile = shelve.open('mydata')
cats = ['Zopkie', 'Pooka', 'Simon']
shelFile['cats'] = cats
shelFile.close()

shelFile = shelve.open('mydata')
shelFile['cats']
['Zopkie', 'Pooka', 'Simon']
shelFile.close()

shelFile = shelve.open('mydata')
list(shelFile.keys())
['cats']
list(shelFile.values())
[['Zopkie', 'Pooka', 'Simon']]
shelFile.close()
````
It may be helpful to use pprint.format() when we work with dictionaries or shelve objects
___
## Sources used for the creation of this cheat sheet
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
