# While loop
Execute some code WHILE some condition remains true

```python
c = 10
while c >= 0: # while this condition is True execute the code under
    print("Hello World!")
    c -=1
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```
```python
num = int(input("Enter a nr between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a nr between 1 - 10: "))

print(f"Your number is {num}")
```