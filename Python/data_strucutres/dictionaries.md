# Dictionaries
Are python's implementation of associative arrays.

| Functions | Explanation |
|-----------|-------------|
| clear() | Removes all the elements from the dictionary `dict.clear()`
| copy() | Returns a copy of the dictionary `dict. copy() `
| fromkeys() | Returns a dictionary with the specified keys and value `dict = dict.fromkeys(keys [, value])`
| get() | Returns the value of the specified key `value_key  = dict.get(key, default=None)`
| items() | Returns a list containing a tuple for each key value pair `list_keys_values = dict.items()`
| keys() | Returns a list containing the dictionary's keys `list_keys = dict.keys()`
| pop() | Removes the element with the specified key `value = dict.pop(key)`
| popitem() | Removes the last inserted key-value pair `dict.popitem()`
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value `value_key  = dict.setdefault(key, default=None)`
| update() | Updates the dictionary with the specified key-value pairs `dict.update(dict)`
| values() | Returns a list of all the values in the dictionary `list_values = dict.values()`
|defaultdict(default_factory)| Defaultdict is a container like dictionaries present in the module collections.Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists `dict = collections.defaultdict(type)` `dict = collections.defaultdict(lambda: 1) # Creates a dict with default value 1.`
___
## Defining a dictionary
```python
# any immutable type can be used as a key, technically must be hashable, which   
# means it can be passed to a hash function. A hash function takes data of arbitrary   
# size and maps it to a relatively simpler fixed-size value called a hash value (or simply hash),   
# which is used for table lookup and comparison.
# from python 3.7 preservation of insertion order is maintained, but they're not considered a sequence  
# a dictionary is like a set of key-value pairs, and sets are unordered.
# duplicate keys are not allowed

d ={<key>: <value>,
    <key>: <value>,
    <key>: <value>
}

d = dict(<key> = <value>,
    <key> = <value>,
    <key> = <value>
)
dict = dict([(<key>, <value>), (<key>, <value>)], <key>=<value>)
dict = dict({<key>: <value>, <key>: "<value>}, <key>=<value>)
dict = dict(collection)   # Creates a dict from coll. of key-value pairs.
dict = dict(zip(keys, values))  # Creates a dict from two collections.
```
___
## Basic operation
```python
# retrieving value
user ={'name': 'Rafal', 'age': 33, 'fav_animal': 'otter'}  # values don't need to be of the same type
user['fav_animal']
'otter'
# adding new entry
user['sport'] = 'muay thai'
user
{'name': 'Rafal', 'age': 33, 'fav_animal': 'otter', 'sport': 'muay thai'}
# updating old entry
user['age'] = 60
user
{'name': 'Rafal', 'age': 60, 'fav_animal': 'otter', 'sport': 'muay thai'}
# delete entry
del user['sport']
user
{'name': 'Rafal', 'age': 60, 'fav_animal': 'otter'}
# if using list or dictionaries as value need to specify index or key
user['pets'] = {'dog':'max', 'cat': 'łatka'}
user['pets']['dog']
'max'

user['languages'] = ['polish', 'english', 'italian']
user['languages'][-1]
'italian'
```
___
## Operators
```python
user = {'name': 'Rafal', 'age': 60, 'fav_animal': 'otter', 'pets': {'dog': 'max', 'cat': 'łatka'}, 'languages': ['polish', 'english', 'italian']}
'name' in user
True
'surname' not in user
True
len(user)
5
```
___
## Sorting
Usually you go from dictionary to list, you sort the list and then cast the sorted list back into dictionary.
```python
# with sorted() = default behavior of sorted() with tuples is to sort lexicographically
# default behaviour is to take the keys of dictionary  
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"} 
sorted(people)
[1, 2, 3, 4]
# OR
# sort by key
dict(sorted(people.items()))  # items creates an iterable of tuples representing the key-value pairs,
# it's actually a dictionary view object, a read only iterable that's linked to   
# the dictionary it was generated from.  
# .values() to get a view of the values only and .keys() to get one with only the keys.
{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

# sort by value 
dict(sorted(people.items(), key=lambda item: item[1]))
{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
# key argument can take a callback function, in this case a lambda
# f you want to sort by value, then you have to specify a sort key.   
# A sort key is a way to extract a comparable value.
# Here the lambda is the smame as:
def value_getter(item):
    return item[1]

# Selecting a Nested Value With a Sort Key
data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}

def get_relevant_skills(item): # e.g tuple (109, {'name': 'Jill', 'age': 83, 'skills': {'java': 10}})
    """Get the sum of Python and JavaScript skill"""
    skills = item[1]["skills"]  # selecting skills key

    # Return default value that is equivalent to no skill
    return skills.get("python", 0) + skills.get("js", 0)  # if elected skill is missing 0 ivalue is defoult

skill_sorted = sorted(data.items(), key=get_relevant_skills, reverse=True)
print(skill_sorted)  # reverse argument because you want the top Python skills to appear first
# skill_sorted is a list of tuples, you need to convert it into dict
# you can use a simple dictionary constructor:
dict(skill_sorted)
# you can use a for loop
skill_sorted_dict = {}
for key, value in skill_sorted:
    skill_sorted_dict[key] = value

from pprint import pprint
pprint(skill_sorted_dict)
{109: {'age': 83, 'name': 'Jill', 'skills': {'java': 10}},
 193: {'age': 30, 'name': 'John', 'skills': {'js': 7, 'python': 8}},
 209: {'age': 15, 'name': 'Bill', 'skills': {'python': 6}},
 277: {'age': 26, 'name': 'Beatriz', 'skills': {'js': 4, 'python': 2}},
 483: {'age': 24, 'name': 'Anna', 'skills': {'js': 10}},
 598: {'age': 62, 'name': 'Sylvia', 'skills': {'bash': 8, 'java': 7}},
 746: {'age': 58, 'name': 'Jane', 'skills': {'js': 2, 'python': 5}},
 765: {'age': 76, 'name': 'Penelope', 'skills': {'go': 5, 'python': 8}},
 984: {'age': 28, 'name': 'Jack', 'skills': {'assembly': 7, 'c': 8}}}

# or use dictionary comprehension if want to change the shape of dictionary or swap  
# the keys and values.
```
___
## Special getter function
```python
from operator import itemgetter
# using itemgetter is much mor efficient on performance
person = ('name', "Rafal")
getter = itemgetter(0)
getter(person)
'name'

getter = itemgetter(1)
getter(person)
'Rafal'

from operator import itemgetter

fruit_inventory = [("banana", 5), ("orange", 15), ("apple", 3), ("kiwi", 0)]

# Sort by key
sorted(fruit_inventory, key=itemgetter(0))
[('apple', 3), ('banana', 5), ('kiwi', 0), ('orange', 15)]

# Sort by value
sorted(fruit_inventory, key=itemgetter(1))
[('kiwi', 0), ('apple', 3), ('banana', 5), ('orange', 15)]
```
___
## Sorted dictionary yes or not?
If you’re going to be adding data to a dictionary, and you want it to stay sorted, is better to use list of tuples or a list of dictionaries:
```python
# Dictionary
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# List of tuples are much faster for sorting than sort a a dictionary view and   
# then create a new sorted dictionary
people = [
    (3, "Jim"),
    (2, "Jack"),
    (4, "Jane"),
    (1, "Jill")
]

# List of dictionaries s the most widespread pattern because of its cross-language   
# compatibility - language interoperability
people = [
    {"id": 3, "name": "Jim"},
    {"id": 2, "name": "Jack"},
    {"id": 4, "name": "Jane"},
    {"id": 1, "name": "Jill"}
]
# there is also from collections import OrderedDict !!!
# Eventually just go with an attribute that clearly specifies the order,  
# like an id, priority, position etc.
people = {
    3: {"priority": 2, "name": "Jim"},
    2: {"priority": 4, "name": "Jack"},
    4: {"priority": 1, "name": "Jane"},
    1: {"priority": 2, "name": "Jill"}
}
# Lookups for dictionaries are much faster!!!
```
___
## Other
````python
{k for k, v in dict.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in dict.items() if k in keys}  # Returns a dictionary, filtered by keys.
# If you decide to go for an ordered collection, check out the Sorted Containers package,   
# which includes a SortedDict.
````
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- J. Sturtz, Real Python, Dictionaries in Python, https://realpython.com/python-dicts/
- I. Currie, Real Python, Sorting a Python Dictionary: Values, Keys, and More, https://realpython.com/sort-python-dictionary/


# DO ZROBIENIA
https://realpython.com/iterate-through-dictionary-python/#using-comprehensions
