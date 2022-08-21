# Sets
Sets:  
- Unordered.
- Contain unique elements. Duplicates are removed.
- It can be modified, but the elements contained in the set must be of an immutable type
- The elements of a set can be of different types
- Can use `len()` for number of elements in set and `in`, `not in` operators for membership

```new_set = set(<iter>)```
The argument `set()` is an iterable, and it generates a list of elements.
```python
name = 'Raffaello'
set(name)
{'f', 'R', 'o', 'l', 'e', 'a'}
```
```new_set = {<obj>, <obj>, ..., <obj>}```
Objects in curly braces are placed into the set intact, even if they are iterable
```python
new_set = {'foo', 'bar', 'baz', 'foo', 'qux'}
new_set
{'foo', 'bar', 'baz', 'qux'}
#---------------------------
new_set = {'foo'}
new_set
{'foo'}
set('foo')
{'f', 'o'}
```
___
:warning:
```python
new_set = set()
type(new_set)
<class 'set'>

new_set = {}
type(new_set)
<class 'dict'>
```
___
## Operation on set
### Union
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 | x2  # if more sets e.g: x1 | x2 | x3 | x4
{'baz', 'quux', 'qux', 'bar', 'foo'}
# OR
x1.union(x2)  # if more sets e.g: x1.union(x2, x3, x4)
{'baz', 'quux', 'qux', 'bar', 'foo'}
```
When using `|` operator both operand must be sets. (This is valid for the others operators)
When using `.union()` method will take any iterable as an argument and convert it to set. (This is valid for the others methods)
___
### Intersection
The resulting set contains only elements that are present in all of the specified sets.
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.intersection(x2)  # if more sets e.g: x1.intersection(x2, x3, x4)
{'baz'}
# OR
x1 & x2  # if more sets e.g: x1 & x2 & x3 & x4
{'baz'}
```
___
### Difference
Compute the difference between two or more set. Is like a subtraction
set nr 1 - set nr 2 = set that results when any elements in set  nr 2 are  subtracted from set nr 1.
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.difference(x2)  # if more sets e.g: x1.difference(x2, x3, x4)
{'foo', 'bar'}
# OR
x1 - x2  # if more sets e.g: x1 - x2 - x3 - x4
{'foo', 'bar'}
```
When multiple sets are specified, the operation is performed from left to right
___
### Symmetric difference
Return a set of all elements in either set nr 1 or set nr 2 but not in both.
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.symmetric_difference(x2)  # !Warning! .symmetric_difference() 
# doesn't allows multiple sets!!!
{'foo', 'qux', 'quux', 'bar'}
# OR
x1 ^ x2   # if more sets e.g: x1 ^ x2 ^ x3 ^ x4
{'foo', 'qux', 'quux', 'bar'}
```
When multiple sets are specified, the operation is performed from left to right.
___
### Isdisjoint
Determines whether two sets have any elements in common.
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

# returns True if x1 and x2 have no elements in common. Intersection will return an empty set
x1.isdisjoint(x2)
False

x2 - {'baz'}
{'quux', 'qux'}
x1.isdisjoint(x2 - {'baz'})  #  There is no operator that corresponds to the .isdisjoint() method
True
```
___
### Issubset
Determine whether one set is a subset of the other.
In set theory, a set x1 is considered a subset of another set x2 if every element of x1 is in x2.
```python
x1 = {'foo', 'bar', 'baz'}
x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})
True

x2 = {'baz', 'qux', 'quux'}
x1 <= x2
False
```
___
### Proper subset
A proper subset is like a subset but the sets can't be identical.  
 A set x1 is considered a proper subset of another set x2 if every element of x1 is in x2, and x1 and x2 are not equal.
```python
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}
x1 < x2
True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
x1 < x2
False
```
___
### Issuperset
A superset is the reverse of a subset. A set x1 is considered a superset of another set x2 if x1 contains every element of x2.
```python
x1 = {'foo', 'bar', 'baz'}

x1.issuperset({'foo', 'bar'})
True

x2 = {'baz', 'qux', 'quux'}
x1 >= x2
False
```
___
### Proper superset
A proper superset is the same as a superset, except that the sets can’t be identical.   
A set x1 is considered a proper superset of another set x2 if x1 contains every 
element of x2, and x1 and x2 are not equal.
```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
x1 > x2
True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
x1 > x2
False
```
___
## Modifying a set
### Update
```python
# x1.update(x2) and x1 |= x2 add to x1 any elements in x2 that x1 does not 
# already have
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2
x1
{'qux', 'foo', 'bar', 'baz'}

x1.update(['corge', 'garply'])
x1
{'qux', 'corge', 'garply', 'foo', 'bar', 'baz'}
```
___
### Add
```python
# x.add(<elem>) adds <elem>, which must be a single immutable object, to x
x = {'foo', 'bar', 'baz'}

x.add('qux')
x
{'bar', 'baz', 'foo', 'qux'}
```
___
### Remove
```python
# x.remove(<elem>) removes <elem> from x. Python raises an exception if <elem> 
# is not in x
x = {'foo', 'bar', 'baz'}

x.remove('baz')
x
{'bar', 'foo'}

x.remove('qux')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x.remove('qux')
KeyError: 'qux'
```
___
### Discard
```python
# x.discard(<elem>) also removes <elem> from x. However, if <elem> is not in x, 
# this method quietly does nothing instead of raising an exception
x = {'foo', 'bar', 'baz'}

x.discard('baz')
x
{'bar', 'foo'}

x.discard('qux')
x
{'bar', 'foo'}
```
___
### Pop
```python
# x.pop() removes and returns an arbitrarily chosen element from x. If x is 
# empty, x.pop() raises an exception
x = {'foo', 'bar', 'baz'}

x.pop()
'bar'
x
{'baz', 'foo'}

x.pop()
'baz'
x
{'foo'}

x.pop()
'foo'
x
set()

x.pop()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x.pop()
KeyError: 'pop from an empty set'
```
### Clear
```python
# x.clear() removes all elements from x
x = {'foo', 'bar', 'baz'}
x
{'foo', 'bar', 'baz'}

x.clear()
x
set()
```
___
### Intersection
```python
# x1.intersection_update(x2) and x1 &= x2 update x1, retaining only elements 
# found in both x1 and x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
x1
{'foo', 'baz'}

x1.intersection_update(['baz', 'qux'])
x1
{'baz'}
```
___
### Difference
```python
# x1.difference_update(x2) and x1 -= x2 update x1, removing elements found in x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
x1
{'bar'}

x1.difference_update(['foo', 'bar', 'qux'])
x1
set()
```
___
### Symmetric difference
```python
# x1.symmetric_difference_update(x2) and x1 ^= x2 update x1, retaining elements 
# found in either x1 or x2, but not both
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 ^= x2
x1
{'bar', 'qux'}

x1.symmetric_difference_update(['qux', 'corge'])
x1
{'bar', 'corge'}
```
___
## Frozen set
Frozensets are exactly like sets, but they are immutable. Only non modifiying 
operations can be performed on a frozenset.
Cool if you need to have sets as dictionary keys. Normal sets are mutable and 
dictionary keys must be immutable like a forzenset. 
```python
x = frozenset(['foo', 'bar', 'baz'])
x
frozenset({'foo', 'baz', 'bar'})

len(x)
3

x & {'baz', 'qux', 'quux'}
frozenset({'baz'})
```
:warning:
```python
f = frozenset(['foo', 'bar', 'baz'])
s = {'baz', 'qux', 'quux'}

f &= s
f
frozenset({'baz'})
```
Python does not perform augmented assignments on frozensets in place. 
The statement x &= s is effectively equivalent to x = x & s.   
It isn’t modifying the original x. 
It is reassigning x to a new object, and the object x originally referenced is gone.
___
## Sources used for the creation of this cheat sheet
- J. Sturtz, Real Python, Sets in Python, https://realpython.com/python-sets/