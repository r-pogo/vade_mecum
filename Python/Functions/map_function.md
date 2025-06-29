# Map function
`map(function, collection)` = Applies a given function to all items in collection
Returns: A new iterable (usually used as a list) where each element is the result of applying the function
`map()` transforms each element.
```python
def c_to_f(temp):
    return (temp * 9/5) + 32


celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
fahrenheit_temps = map(c_to_f, celsius_temps)
print(fahrenheit_temps)
<map object at 0x000002250EED3130> # object is iterable

>>> for temp in fahrenheit_temps:
...         print(temp)
... 
32.0
50.0
68.0
86.0
104.0
122.0

# Or cast type
fahrenheit_temps = list(map(c_to_f, celsius_temps))
```
## With lambda
```python
celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
fahrenheit_temps = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)
```