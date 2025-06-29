# Filter function
`filter(function, collection)` = return all elements that pass a condition. Filters the iterable, keeping only the items for which the function returns True.
Returns: A new iterable containing only the elements that satisfy the condition.
`filter()` selects elements based on a condition.

```python
def is_passing(grade):
    return grade >=60

grades = [91, 32, 83, 44, 65, 56, 99, 67, 80]
passing_grades = filter(is_passing, grades)
print(passing_grades)
<filter object at 0x000001AB9D58EAA0> # object because python is saving memory
# is iterable
for grade in passing_grades:
    print(grade)

# convert filter to a list 
passing_grades = list(filter(is_passing, grades))
print(passing_grades)
[91, 83, 65, 99, 67, 80]

```
## With lambda
```python
grades = [91, 32, 83, 44, 65, 56, 99, 67, 80]

passing_grades = list(filter(lambda grade: grade >= 60,grades))
```