# Dictionaries
Are python's implementation of associative arrays.
## Dictionary Methods
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
Any immutable type can be used as a key, technically must be hashable, which   
means it can be passed to a hash function. A hash function takes data of arbitrary   
size and maps it to a relatively simpler fixed-size value called a hash value (or simply hash),   
which is used for table lookup and comparison.  
From python 3.7 preservation of insertion order is maintained, but they're not considered a sequence  
a dictionary is like a set of key-value pairs, and sets are unordered.  
Duplicate keys are not allowed
```python
d ={<key>: <value>,
    <key>: <value>,
    <key>: <value>
}

d = dict(<key> = <value>,
    <key> = <value>,
    <key> = <value>
)
dict = dict([(<key>, <value>), (<key>, <value>)], <key>=<value>)
dict = dict({<key>: <value>, <key>: <value>}, <key>=<value>)
dict = dict(zip(keys, values))  # creates a dict from two collections.
dict = collections.defaultdict(<type>)  # creates an empty dict with default value of type
dict = dict.fromkeys(keys, value)  # creates a dict from collection of keys
```
___
## Basic operation
### Accessing values
```python
# coll. of keys
user ={'name': 'Rafal', 'age': 33, 'fav_animal': 'otter'}
print(user.keys())
dict_keys(['name', 'age', 'fav_animal'])

# coll. of values
print(user.values())
dict_values(['Rafal', 33, 'otter'])

# coll. of key-value tuples
print(user.items())
dict_items([('name', 'Rafal'), ('age', 33), ('fav_animal', 'otter')])

# Retrieving a particular value
user ={'name': 'Rafal', 'age': 33, 'fav_animal': 'otter'}  # values don't need to be of the same type
user['fav_animal']
'otter'

# if using list or dictionaries as value need to specify index or key
user = {'name': 'Rafal', 'age': 60, 'fav_animal': 'otter', 'pets': {'dog': 'max', 'cat': 'łatka'}, 'languages': ['polish', 'english', 'italian']}
user['pets'] = {'dog':'max', 'cat': 'łatka'}
print(user['pets']['dog'])
'max'

user['languages'] = ['polish', 'english', 'italian']
print(user['languages'][-1])
'italian'
```
### Modifying and adding elements
```python
# Adding new entry
user['sport'] = 'muay thai'
print(user)
{'name': 'Rafal', 'age': 33, 'fav_animal': 'otter', 'sport': 'muay thai'}

# Updating old entry
user['age'] = 60
print(user)
{'name': 'Rafal', 'age': 60, 'fav_animal': 'otter', 'sport': 'muay thai'}

# Delete entry
del user['sport']
user
{'name': 'Rafal', 'age': 60, 'fav_animal': 'otter'}
````
___
## 'in' operator and len()
```python
user = {'name': 'Rafal', 'age': 60, 'fav_animal': 'otter', 'pets': {'dog': 'max', 'cat': 'łatka'}, 'languages': ['polish', 'english', 'italian']}
'name' in user
True
'surname' not in user
True
len(user) # number of keys
5
```
___
## Iterating through a dictionary
```python
# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Iterating through values
for value in my_dict.values():
    print(value)
```
### Iterating with .popitem()
Perfect to iterate through a dictionary in Python and delete its items sequentially.
When you call .popitem() on an empty dictionary, it raises a KeyError.
```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break

Dictionary length: 3
('pet', 'dog') removed
Dictionary length: 2
('fruit', 'apple') removed
Dictionary length: 1
('color', 'blue') removed
Dictionary length: 0
The dictionary has no item now...
```
Here .popitem() sequentially removed the items of a_dict.  
The loop broke when the dictionary became empty, and .popitem() raised a KeyError exception.
___
## Sorting
Usually you go from dictionary to list, you sort the list and then cast the sorted list back into dictionary.
If you decide to go for an ordered collection, check out the Sorted Containers package, which includes a SortedDict.

`sorted()` doesn't really modify the order of the underlying dictionary.  
What really happen is that sorted() creates an independent list with its element in sorted order
### sorted()
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

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
     print(key, '->', incomes[key])

apple -> 5600.0
banana -> 5000.0
orange -> 3500.0
```
### Sort by value
```python
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
dict(sorted(people.items(), key=lambda item: item[1]))
{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
# If you want to sort by value, then you have to specify a sort key.   
# A sort key is a way to extract a comparable value.
# The key keyword argument specifies a function of one argument that 
# is used to extract a comparison key from each element you’re processing
# key argument can take a callback function, in this case a lambda
# Here the lambda is the same as:
def value_getter(item):
    return item[1]

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
def value_getter(item):
    return item[1]

for k, v in sorted(people.items(), key=value_getter):
    print(k, '->', v)
2 -> Jack
4 -> Jane
1 -> Jill
3 -> Jim

# Also for only values
for v in sorted(people.values()):
    print(v)
```
### Reversed sorting
```python
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes, reverse=True):
     print(key, '->', incomes[key])

orange -> 3500.0
banana -> 5000.0
apple -> 5600.0
```
### Selecting a Nested Value With a Sort Key
```python
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
    return skills.get("python", 0) + skills.get("js", 0)  # if selected skill is missing 0 value is default

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
## Sorted dictionary good idea?
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
## Dictionary comprehensions
````python
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
a_dict
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

{k for k, v in dict.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in dict.items() if k in keys}  # Returns a dictionary, filtered by keys.
````
### Removing specific items
Key-view objects also support common set operations
```python
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
non_citric
{'apple': 5600.0, 'banana': 5000.0}
```
### Sorting
```python
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
sorted_income
{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}
```
___
## collections.ChainMap
`collections` is a module from the Python Standard Library that provides specialized container data types.  
One of these data types is ChainMap, which is a dictionary-like class for creating a single view of  
multiple mappings (like dictionaries). With ChainMap, you can group multiple dictionaries together  
to create a single, updatable view.
```python
from collections import ChainMap
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)
chained_dict  # A ChainMap object
ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})
for key in chained_dict:
     print(key, '->', chained_dict[key])

pepper -> 0.2
orange -> 0.35
onion -> 0.55
apple -> 0.4
```
ChainMap objects also implement .keys(), values(), and .items() as a standard dictionary does,  
so you can use these methods to iterate through the dictionary-like object generated by ChainMap,  
just like you would do with a regular dictionary:
```python
for key, value in chained_dict.items():
     print(key, '->', value)

apple -> 0.4
pepper -> 0.2
orange -> 0.35
onion -> 0.55
```
___
## itertools
### cycle()
Perfect for iterate through a dictionary repeatedly in a single loop
```python
from itertools import cycle
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 3  # Define how many times you need to iterate through prices
total_items = times * len(prices)
print(total_items)
for item in cycle(prices.items()):
     if not total_items:
         break
     total_items -= 1
     print(item)

('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
```
The preceding code allowed you to iterate through prices a given number of times  
(3 in this case). This cycle could be as long as you need, but you are responsible for stopping it.  
The if condition breaks the cycle when total_items counts down to zero
### chain()
itertools also provides chain(*iterables), which gets some iterables as arguments  
and makes an iterator that yields elements from the first iterable until it’s exhausted,  
then iterates over the next iterable and so on, until all of them are exhausted.
This allows you to iterate through multiple dictionaries in a chain.
```python
from itertools import chain
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}
for item in chain(fruit_prices.items(), vegetable_prices.items()):
     print(item)

('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('pepper', 0.2)
('onion', 0.55)
('tomato', 0.42)
```
___
## Dictionary Unpacking Operator (**)
Suppose you have two (or more) dictionaries, and you need to iterate through them together,  
you can use the dictionary unpacking operator (**) to merge the two dictionaries into a  
new one and then iterate through it.
```python
>>> fruit_prices = {'apple': 0.40, 'orange': 0.35}
>>> vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
>>> # How to use the unpacking operator **
>>> {**vegetable_prices, **fruit_prices}
{'pepper': 0.2, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
>>> # You can use this feature to iterate through multiple dictionaries
>>> for k, v in {**vegetable_prices, **fruit_prices}.items():
...     print(k, '->', v)
...
pepper -> 0.2
onion -> 0.55
apple -> 0.4
orange -> 0.35
```
It’s important to note that if the dictionaries you’re trying to merge have repeated or common keys,  
then the values of the right-most dictionary will prevail:
```python
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': .25}
{**vegetable_prices, **fruit_prices}
{'pepper': 0.25, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
```
The pepper key is present in both dictionaries. After you merge them,  
the fruit_prices value for pepper (0.25) prevailed, because fruit_prices is the right-most dictionary.
## Sources
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- J. Sturtz, Real Python, Dictionaries in Python, https://realpython.com/python-dicts/
- I. Currie, Real Python, Sorting a Python Dictionary: Values, Keys, and More, https://realpython.com/sort-python-dictionary/
- L. P. Ramos, Real Python, How to Iterate Through a Dictionary in Python, https://realpython.com/iterate-through-dictionary-python/#using-comprehensions

