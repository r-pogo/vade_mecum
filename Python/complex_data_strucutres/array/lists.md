# Lists
Lists are a part of the core Python language. Despite their name, Python’s lists are 
implemented as dynamic arrays behind the scenes.

This means a list allows elements to be added or removed, and the list will 
automatically adjust the backing store that holds these elements by allocating or 
releasing memory.

Python lists can hold arbitrary elements—everything is an object in Python, 
including functions. Therefore, you can mix and match different kinds of 
data types and store them all in a single list.

A list stores series of items in a particular order. You access items using an index, or with a loop.
````
bikes = ['trek', 'redline', 'giant']
Get the first item in a list
first_bike = bikes[0]

Get the last item in a list
last_bike = bikes[-1]

Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

Inserting elements at a particular position
users.insert(0, 'joe')
users.insert(3, 'bea')

Making numerical lists
squares = []
for x in range(1, 11):
 squares.append(x**2)
 
Changing an element
users[0] = 'valerie'
users[-2] = 'ronald'

Deleting an element by its position
del users[-1]
Removing an item by its value
users.remove('mia')

If you want to work with an element that you're removing 
from the list, you can "pop" the element. If you think of the 
list as a stack of items, pop() takes an item off the top of the 
stack. By default pop() returns the last element in the list, 
but you can also pop elements from any position in the list.

Pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)
Pop the first item in a list
first_user = users.pop(0)
print(first_user)

Find the length of a list
num_users = len(users)
print("We have " + str(num_users) + " users.")

The sort() method changes the order of a list permanently. 
The sorted() function returns a copy of the list, leaving the 
original list unchanged. You can sort the items in a list in 
alphabetical order, or reverse alphabetical order. You can 
also reverse the original order of the list. Keep in mind that 
lowercase and uppercase letters may affect the sort order.

Sorting a list permanently
users.sort()

Sorting a list permanently in reverse alphabetical 
order
users.sort(reverse=True)

Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))

Reversing the order of a list
users.reverse()

You can use the range() function to work with a set of 
numbers efficiently. The range() function starts at 0 by 
default, and stops one number below the number passed to 
it. You can use the list() function to efficiently generate a 
large list of numbers.

Printing the numbers 0 to 1000
for number in range(1001):
 print(number)
 
Printing the numbers 1 to 1000
for number in range(1, 1001):
 print(number)
 
Making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))

There are a number of simple statistics you can run on a list 
containing numerical data.

Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)

Finding the maximum value
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)

Finding the sum of all values
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)

You can work with any set of elements from a list. A portion 
of a list is called a slice. To slice a list start with the index of 
the first item you want, then add a colon and the index after 
the last item you want. Leave off the first index to start at 
the beginning of the list, and leave off the last index to slice 
through the end of the list.

Getting the first three items
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]

Getting the middle three items
middle_three = finishers[1:4]

Getting the last three items
last_three = finishers[-3:]

Making a copy of a list
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]
````
___
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- D. Bader, Real Python, Common Python Data Structures (Guide), https://realpython.com/python-data-structures/#list-mutable-dynamic-arrays


