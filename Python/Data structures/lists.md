# Lists
Table of content:
- [List methods](#list-methods)
- [Basic operation](#basic-operation)  
    1.[List comprehensions](#list-comprehensions)  
    2.[Modifying and adding elements](#modifying-and-adding-elements)  
    3.[Removing values](#removing-values)  
    4.[Reverting a list](#reverting-a-list)  
    5.[Finding index](#finding-index)  
    6.[The in and not in operators](#the-in-and-not-in-operators)  
    7.[Multiple assignment trick](#multiple-assignment-trick)  
    8.[random.choice() and random.shuffle()](#random.choice()-and-random.shuffle())  
- [List concatenation](#list-concatenation)  
- [Sorting](#sorting)  
- [Tips and Tricks](#tips-and-tricks)  
    1.[Enumerate](#enumerate)  
    2.[Difference between two lists](#difference-between-two-lists)  
    3.[Removing duplicate items from list](#removing-duplicate-items-from-list)  
    4.[Find if all items are identical](#find-if-all-items-are-identical)  
    5.[How to efficiently compare two unordered lists](#how-to-check-if-all-elements-in-a-list-are-unique)  
    6.[Convert two lists into a dictionary](#convert-two-lists-into-a-dictionary)  
    7.[Loop multiple list with zip()](#loop-multiple-list-with-zip)  
    8.[Convert list to dictionary with enumerate](#convert-list-to-dictionary-with-enumerate)

Python’s lists are implemented as dynamic arrays behind the scenes.

Lists allow elements to be added or removed, and the list will 
automatically adjust the backing store that holds these elements by allocating or 
releasing memory.

Python lists can hold arbitrary elements, everything is an object in Python, 
including functions. Therefore, you can mix and match different kinds of 
data types and store them all in a single list.

A list stores series of items in a particular order. You access items using an index, 
or with a loop.

Sum up:
- Lists are ordered.
- Zero based
- Heterogeneous: Lists can contain any arbitrary objects.
- List elements can be accessed by index.
- Nestable: Lists can be nested to arbitrary depth.
- Lists are mutable.
- Lists are dynamic.
- Iterable
- Slicable
- Combinable

```python
# List literals:
my_list = [itme_0, itme_1, ..., item_n]

# The list() constructor:
my_list = list([iterable])
# Strings are iterable so the constructor will break them down
list("Pythonista")
['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a']

list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions
my_list = [expression for element in iterable]

[number ** 2 for number in range(1,10)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]

# Empty list
empty = []
empty
[]
list()
[]
list(0,1,2) #argument must be iterable
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    list(0,1,2)
    ~~~~^^^^^^^
TypeError: list expected at most 1 argument, got 3
list((0,1,2,3)) # here passing a tuple
[0, 1, 2, 3]
```
___
## List methods <div id='list-methods'/>
| Functions | Explanation |
|-----------|-------------|
| append() | adds an element to the end of the list `list.append(element)`  
| extend() | adds all elements of a list to another list `list.extend(collection)`
| insert() | inserts an item at the defined index `list.insert(int, element)`
| remove() | removes first occurrence of the item or raises ValueError `list.remove(element)`
| pop() | returns and removes an element at the given index or from thh end `element  = list.pop([int])`
| clear() | removes all items from the list also works on dictionary and set `list.clear()`
| index() | returns the index of the first matched item or raises ValueError `index_nr = list.index(element)`
| count() | returns the count of the number of items passed as an argument `int = list.count(element)`
| sort() | sort items in a list in ascending order `list.sort()`
| sorted()| returns a new sorted list `list = sorted(collection)`
| reverse() | reverse the order of items in the list `list.reversed()`
| copy() | returns a shallow copy of the list `new_list = old_list.copy()`
___
## Basic operation <div id='basic-operation'/>
Python sequence slice addresses can be written as `list[start:end:step]` and any of start, stop or end can be dropped. 
`list[::3]` is every third element of the sequence, `list[-3:]` getting the last three elements.  
Reverting `list[::-1]`.

````python
my_list[start:stop:step]
list = list[slice]    # Or: list[from_inclusive : to_exclusive : ±step]
new_list = old_list[:]   # Another way to copy a list
````
### List comprehensions <div id='list-comprehensions'/>
````python
squares = [x**2 for x in range(1, 11)]
````
````python
sum_of_elements = sum(collection)
minimum_value_in_list = min(list)
maximum_value_in_list = max(list)
list_from_range = list(range(1, 100))
elementwise_sum = [sum(pair) for pair in zip(list_a, list_b)]
list_of_chars = list(str)
````
### Modifying and adding elements <div id='modifying-and-adding-elements'/>
Change single element
````python
l = ["ciastka", "tort"]
l[0] = 'carrots'
l
['carrots', 'tort']
````
Adding values
```python
# append() adds an element to the end of a list:
l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l.append('milk')
print(l)
['foo', 'bar', 'baz', 'blabla', 'cookies', 'milk']

# insert() adds an element to a list at a given position
l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l.insert(1, 'jujitsu')
print(l)
['foo', 'jujitsu', 'bar', 'baz', 'blabla', 'cookies']
```
Modifying Multiple List Values
```python
l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l[0:4] = ['moreCookies', 'BAR', 'something']
l
['moreCookies', 'BAR', 'something', 'cookies']

# For inserting multiple elements in place of a single element use a slice 
# that denotes only one element.
l = [1,2,3]
l[1:2] = [4,5,6]
l
[1, 4, 5, 6, 3]

l = [1,2,3]
l[2] = [88, 100, 12]
l
[1, 2, [88, 100, 12]]

# for inserts without removing anything, just specify a zero-length slice [n:n]
l = [1,2,3]
l[1:1] = ['cookie', 33, 88]
l
[1, 'cookie', 33, 88, 2, 3]
```
___
### Removing values <div id='removing-values'/>
```python
# del removes an item using the index
l = ["ciastka", "tort"]
del l[0]
l
['tort']
# remove() removes an item with using actual value of it:
l.remove("ciastka") # removing item by its value

# pop()  will remove and return the last item of the list.  
# You can also pass the index of the element as an optional parameter
l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l.pop()
print(l)
['foo', 'bar', 'baz', 'blabla']

```
___
### Reverting a list <div id='reverting-a-list'/>
```python
l = [1,2,3]
print(l[::-1])
[3, 2, 1]
````
```python
# reverse() like sort()dosen't create a new list, this is why you call it directly instead of generating a new varibale
spam = ['cat', 'dog', 'turtle']
spam.reverse()
spam
['turtle', 'dog', 'cat']
```
___
### Finding index <div id='finding-index'/>
```python
l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l.index('blabla')
3
```
___
### The in and not in operators <div id='the-in-and-not-in-operators'/>
```python
1 in [1,2,3]
True

'jujitsu' not in ['football', 'hockey', 'jujitsu']
False
```
### Multiple assignment trick <div id ='multiple-assignment-trick'/>
```python
furniture = ['table1', 'chair2', 'rack3', 'shelf4']
table, chair, rack, shelf = furniture

print(table, shelf)
table1 shelf4

# this trick can be used to swap values
a, b = 'python', 'c++'
a, b = b, a
print(a)
c++
print(b)
python
```

### random.choice() and random.shuffle() <div id ='#random.choice()-and-random.shuffle()'/>
```python
import random

pets = ['dog', 'cat', 'turtle']
random.choice(pets)
dog
```
```python
import random

people = ['Alice', 'Celina', 'Elski']
random.shuffle(people)
people
['Celina', 'Elski', 'Alice']
```
___
## List concatenation <div id='list-concatenation'/>
With '+' operator
```python
list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8] 

result = list1 + list2
print(result)
[1, 2, 3, 4, 5, 6, 7, 8] # list2 appended at the end of the other

my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
print(my_list)
[1, 2, 3, 'A', 'B', 'C']
```
With a for loop:
```python
list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8]

for i in list2:
    list1.append(i)

print(list1)
[1, 2, 3, 4, 5, 6, 7, 8]
```
With a list comprehension
```python
list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8]

result = [j for i in [list1, list2] for j in i]
print(result)
[1, 2, 3, 4, 5, 6, 7, 8]
```
With extend() function
```python
list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8]

list1.extend(list2)
print(list1)
[1, 2, 3, 4, 5, 6, 7, 8]
```
With '*' operator
```python
list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8]

result = [*list1, *list2] # * operator unpacks a collection of items
print(result)
[1, 2, 3, 4, 5, 6, 7, 8]
```
With itertools.chain()
```python
import itertools

list1 = [1, 2, 3, 4, 5] 
list2 = [6, 7, 8]
# itertools.chain() accepts different iterables as parameters and gives a sequence as output.  
# Output is a linear sequence. The data type doesn't affect the functioning of the method. 
result = list(itertools.chain(list1, list2))
print(result)
[1, 2, 3, 4, 5, 6, 7, 8]
```
By multiplication
```python
print(['a', 'b', 'c'] * 4)
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```
___
## Sorting <div id='sorting'/>
```python
# sort() dosne't creat a new list this is why you call it directly instead of creating a new varibale.
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers)
[-7, 1, 2, 3.14, 5]

l = ['foo', 'bar', 'baz', 'blabla', 'cookies']
l.sort(reverse=True)
print(l)
['foo', 'cookies', 'blabla', 'baz', 'bar']

# If you need to sort the values in regular alphabetical order, pass str.lower  
# for the key keyword argument in the sort() method call:
letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
print(letters)
['a', 'A', 'z', 'Z']

# You can use the built-in function sorted() to return a new list:
numbers = [2, 5, 3.14, 1, -7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
[-7, 1, 2, 3.14, 5]
```
## Copying
```python
# Aliasing, binding a new name to the same underlying object
# By modifying an alias will result in modifying the original list and vice versa
new_variable = original_variable
countries = ["US", "Canada", "Polad"]
nations = countries
id(countries)
2180282582592
id(nations)
2180282582592
id(countries) == id(nations)
True

countries[0]="Italy"
countries
['Italy', 'Canada', 'Polad']
nations
['Italy', 'Canada', 'Polad']

# Shallow vs Deep Copies

# Shallow copy ia a new list containing references to the objects in the original list.
# To create shallow copies:
# slicing [:]
nations = countries[:]
nations
['Italy', 'Canada', 'Polad']
id(countries) == id(nations)
False
id(nations[0]) == id(countries[0])
True

countries[0] = "Japan"
countries
['Japan', 'Canada', 'Polad']
nations
['Italy', 'Canada', 'Polad']

# The .copy() method

# copy() from the copy module

# A deep copy of a list contains references to copies of the objects in the original list
# To create deepcopy:
# deepcopy() from the copy module

>>> from copy import copy, deepcopy
>>> matrix = [[1,2,3], [4,5,6], [7,5,9]]
>>> shallow = copy(matrix)
>>> deep= deepcopy(matrix)
>>> id(matrix)
2180282522944
>>> id(shallow)
2180282585216
>>> id(deep)
2180282583424
>>> id(matrix[0])
2180282588416
>>> id(shallow[0])
2180282588416
>>> id(deep[0])
2180282517120

>>> matrix[0][0] = 100
>>> matrix[0][1] = 200
>>> matrix[0][2] = 300
>>> matrix
[[100, 200, 300], [4, 5, 6], [7, 5, 9]
>>> shallow
[[100, 200, 300], [4, 5, 6], [7, 5, 9]]
>>> deep
[[1, 2, 3], [4, 5, 6], [7, 5, 9]]
```
## Tips and Tricks <div id='tips-and-tricks'/>
### Enumerate <div id='enumerate'/>
```python
inventory = ['book', 'magic potion', 'arrow']

for index, item in enumerate(inventory):
    print(f"{index}: {item}")

0: book
1: magic potion
2: arrow
```
### Difference between two lists <div id='difference-between-two-lists'/>
```python
list1 = [1, 2, 3, 4, 'C#'] 
list2 = [1, 7, 8, 2, 'Python']

set1 = set(list1)
set2 = set(list2)
# symmetric_difference() method returns a set that contains all items from both  
# set, but not the items that are present in both sets
result = list(set1.symmetric_difference(set2))
print(result)
[3, 4, 7, 8, 'Python', 'C#']
```
### Removing duplicate items from list <div id='removing-duplicate-items-from-list'/>
```python
list1 = [1,1,2,3,4,5,5,6,6,8,8,8,10,'Python','Python']

no_duplicates = list(set(list1))
print(no_duplicates)
[1, 2, 3, 4, 5, 6, 8, 10, 'Python']
```
### Find if all items are identical <div id='find-if-all-items-are-identical'/>
```python
list1 = [1,1,1,1]
list2 = [1,1,1,2]
# counting the occurrence of the first element, if it is the same as the length  
# of a list then all element must be the same
print(all(item == list1[0] for item in list1))
print(all(item == list2[0] for item in list2))
True
False
```
### How to efficiently compare two unordered lists <div id='how-to-check-if-all-elements-in-a-list-are-unique'/>
```python
# collections.Counter class,allows you to count the occurrences of  
# elements in each list
from collections import Counter

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 2, 1]

print(Counter(list1) == Counter(list2))
True
```
### How to check if all elements in a list are unique <div id='convert-two-lists-into-a-dictionary'/>
```python
# You can check if all elements in a list are unique by converting the list to a  
# set and comparing the lengths. If the length of the set is equal to the length  
# of the original list, it means all elements are unique

def are_all_elements_unique(lst):
    return len(lst) == len(set(lst))

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 2, 3, 4]

print(are_all_elements_unique(my_list1))  # Output will be True
print(are_all_elements_unique(my_list2))  # Output will be False
```
### Convert two lists into a dictionary <div id='convert-two-lists-into-a-dictionary'/>
```python
list1 = [1,2,3]
list2 = ['python', 'java', 'c++']

new_dict = dict(zip(list1,list2))
print(new_dict)
{1: 'python', 2: 'java', 3: 'c++'}
```
### Loop multiple list with zip() <div id='loop-multiple-list-with-zip'/>
```python
items = ['apple', 'milk', 'honey']
prices = [1.20, 2, 3]

for item, price in zip(items, prices):
    print(f'The {item} costs {price}')
The apple costs 1.2
The milk costs 2
The honey costs 3
```
### Convert list to dictionary with enumerate <div id='convert-list-to-dictionary-with-enumerate'/>
```python
import pprint
tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

pprint.pprint(dict(list(enumerate(tickers))))

{0: 'AAPL.US',
 1: 'AXP.US',
 2: 'BA.US',
 3: 'CAT.US',
 4: 'CSCO.US',
 5: 'CVX.US',
 6: 'DIS.US',
 7: 'DOW.US',
 8: 'GS.US',
 9: 'HD.US',
 10: 'IBM.US',
 11: 'INTC.US'}

```


