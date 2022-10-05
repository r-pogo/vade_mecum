# Lists
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
- Lists can contain any arbitrary objects.
- List elements can be accessed by index.
- Lists can be nested to arbitrary depth.
- Lists are mutable.
- Lists are dynamic.
___
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
Python sequence slice addresses can be written as `list[start:end:step]` and any of start, stop or end can be dropped. 
`list[::3]` is every third element of the sequence, `list[-3:]` getting the last three elements.

````python
list = list[slice]    # Or: list[from_inclusive : to_exclusive : ±step]
new_list = old_list[:]   # Another way to copy a list
````
````python
# List comprehensions
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
````python
# Change single element
l = ["ciastka", "tort"]
l[0] = 'carrots'
l
['carrots', 'tort']
# Deleting single element
l = ["ciastka", "tort"]
del l[0]
l
['tort']
l.remove("ciastka") # removing item by its value
# Modifying Multiple List Values
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
````
# TODO list concatenation https://www.digitalocean.com/community/tutorials/concatenate-lists-python





