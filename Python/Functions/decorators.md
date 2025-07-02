# Decorators
Decorator = A function that extends the behaviour of another function without modyfiyng that base function.
Based function is pased as an argument to the decorator
A function that taks another function as an argument and returns another functinon as a return value 
a higher level function - it operates on other functions

````python
from functools import wraps


def create_new_function(function): # the decorator takes a function as an argument
    
    @wraps(function) # to not loos teh doc string from function_1
    def inner(values) # usually decorators have an inner function
        # do stuff
        return # stuff
    return inner

@create_new_function  # this is the same as function_1 = create_new_function(function_1) 
def function_1():
    print("funciton_one")


def function_2():
    print("function_two")
````
```python
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper()

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper()

@add_sprinkles
@add_fudge  
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")
    
get_ice_cream("vanilla")
```
