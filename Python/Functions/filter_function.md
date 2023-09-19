# Filter function
Filter function - filter(function, iterable). Returns items from iterable that meet   
the established criteria in the function.

```python
l = [1,2,3,4,5,6,7,8]
def my_filter(numb):
    if numb % 2 == 0:
        return numb
        
f = filter(my_filter, l)
print(f)
<filter object at 0x000001AB9D58EAA0> # object because python is saving some memory

# convert filter to a list 
f = list(filter(my_filter, l))
print(f)
[2, 4, 6, 8]
```