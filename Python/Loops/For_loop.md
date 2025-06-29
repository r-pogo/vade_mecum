# For loop
Execute a block of code a fixed number of times.  
Can iterate over a range, string, sequence etc.

```python
for i in range(1, 11):
    print(i)
1
2
3
4
5
6
7
8
9
10

# Counting by 2
for i in range(1,11,2):
    print(i)
1
3
5
7
9

# Backwards with range
for i in range(11, -1, -1):
    print(i)
11
10
9
8
7
6
5
4
3
2
1
0

# With the revers function
for i in reversed(range(1, 11)):
    print(i)
10
9
8
7
6
5
4
3
2
1
```
___
## Continue and Break
```python
# Skip 13
for i in range(1, 21):
    if i == 13:
        continue
    else:
        print(i)
1
2
3
4
5
6
7
8
9
10
11
12
14
15
16
17
18
19
20

# Stop at 13
for i in range(1, 21):
    if i == 13:
        break
    else:
        print(i)
1
2
3
4
5
6
7
8
9
10
11
12
```