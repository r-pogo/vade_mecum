# lambda
```python
def add(x, y):
    return x + y

print(add(2, 2))
4

# lambda define inputs: define operation
lambda x,y: x + y # lambda can have only single line expressions, it returns automatically  
                  # no need for return keyword

# Lambda functions are anonymous function, they don't have a name, but it can be assigned to a variable
add = lambda x,y: x + y
print(add(2,3))
5

# can also enclose it in parenthesis and add inputs in parenthesis and print it
print((lambda x,y: x + y)(2,3))
5
```
The purpose of a lambda is to be passed into a higher-order function - a function that can  
tak in another function as an input or return a function as an output, or both.

```python
def map(my_func, my_iter):
    result = []
    for i in my_iter:
        new_i = my_func(i)
        result.append(new_i)
    return result

numbers = [3,4,5,6,8]

cubed = map(lambda x: x**3, numbers)
print(cubed)
[27, 64, 125, 216, 512]
```