# Tuple
Tuples are immutable and hashable lists.  
Can hold elements of arbitrary data types.
```python
tuple = ()
tuple = (element,)  # Or: <el>, Need to add a comma if it is just one element
tuple = (el_1, el_2 [...])  # Or: <el_1>, <el_2> [...]
```
Only reassignment works. But, if the element is itself a mutable data type like a list, its nested items can be changed.
```python
t = (1,2,3)
t = (a,b,c)
```
Concatenation + operator to combine two tuples.
In order to repeat the elements in a tuple for a given number of times use * operator.
Both + and * operations result in a new tuple.
````python
# Concatenation
print((1, 2, 3) + (4, 5, 6))
(1, 2, 3, 4, 5, 6)

# Repeat
print(("Repeat",) * 3)
('Repeat', 'Repeat', 'Repeat')
````
Deleting a tuple entirely, is possible using the keyword `del`.
````python
t = (1,2,3)
del t
````
`count` and `index` methods works with tuple.(see list)
___
## Named tuple
Tuple's subclass with the fields that can also be accessed by .fieldname

```python
>>> from collections import namedtuple
>>> Coordinate = namedtuple('Coordinate', 'x y')
>>> c = Coordinate(1, y=2)
Coordinate(x=1, y=2)
>>> c[0]
1
>>> c.x
1
>>> getattr(c, 'y')
2
>>> c._fields  # Or: Coordinate._fields
('x', 'y')
```