# Nested loops
nested loop = A loop within another loop (outer, inner)
```python
while x > 0:
    while y > 0:
        print("do something")
        
for x in range(3):
    for y in range(9):
        print("do something")
```
```python
# outer loop specifies how many times the inner will be repeated
for i in range(3):
    # here inner loop is executed 3 times
    for j in range(1, 5):
        print(j, end="-")
1-2-3-4-1-2-3-4-1-2-3-4-

# If you want to have them on separated lines add an empty print() which will add a \n after each  
# iteration of the inner loop

for i in range(3):
    for j in range(1, 5):
        print(j, end="-")
    print()
1-2-3-4-
1-2-3-4-
1-2-3-4-
```
```python
# printing simple figures like rectangle
rows = int(input("Nr rows: "))
columns = int(input("Nr columns "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
```