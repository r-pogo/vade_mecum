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
````python
dict = dict(collection)   # Creates a dict from coll. of key-value pairs.
dict = dict(zip(keys, values))  # Creates a dict from two collections.
{k for k, v in dict.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in dict.items() if k in keys}  # Returns a dictionary, filtered by keys.
````
