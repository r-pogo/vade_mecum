# Exception Handling
Exception is an event that interrupts the flow of a program, there are many types  
(ZeroDivisionError, TypeError, ValueError).
Has 3 blocks: 1.try, 2.except, 3.finally
```
try:
    # Try some code
except Exception:
    # Handle an Exception
finally:
    # Do clean up
```

```python
try:
    number= int(input("Enter number: "))
    print(1 / number)
except ZeroDivisionError:
    print("No division by 0")
except ValueError:
    print("Enter only numbers please")

```
```python
try:
    number= int(input("Enter number: "))
    print(1 / number)
except Exception: # Exception catches all exception this is a bad practice
    print("Something went wrong! WINDOWS!!!")
```
```python
try:
    number= int(input("Enter number: "))
    print(1 / number)
except ZeroDivisionError:
    print("No division by 0")
except ValueError:
    print("Enter only numbers please")
except Exception: # in this case if there is something else we will try to catch it with general Exception
    print("Something went wrong!")
finally: # this black is always executed regardless if there was an exception or not
    print("Clean up!") # like handling opened files in try
```