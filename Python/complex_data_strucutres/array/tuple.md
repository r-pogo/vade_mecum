# Tuple

Similar to lists, but are immutable. This means elements can’t be added or removed dynamically, all elements in a 
tuple must be defined at creation time.

Can hold elements of arbitrary data types.
___
## Working with tuples
Only reassignment works. But, if the element is itself a mutable data type like a list, its nested items can be changed.
````
t = (1,2,3)
t = (a,b,c)
````
Concatenation + operator to combine two tuples.
In order to repeat the elements in a tuple for a given number of times use * operator.
Both + and * operations result in a new tuple.
````
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))
(1, 2, 3, 4, 5, 6)

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
('Repeat', 'Repeat', 'Repeat')
````
Deleting a tuple entirely, is possible using the keyword `del`.
````
t = (1,2,3)
del t
````
`count` and `index` methods works with tuple.(see list)
___
## Sources used for the creation of this cheat sheet
- Python documentation, https://docs.python.org/3/library/stdtypes.html#tuple