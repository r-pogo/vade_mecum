# pyInputPlus
| Function | Description |
|----------|-------------|
| inputNum() | Accepts a numeric value. It takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’ for bounds. Returns an int or float.
| inputStr() | Accepts a string value. It provides features such as ‘blockRegexes’, ‘timeout’, ‘limit’ etc.
| inputInt() | Accepts an integer value. This also takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  for bounds. Returns an int.
| inputFloat() | Accepts a floating-point numeric value. Also takes additional ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  parameters. Returns a float.
| inputBool() | Accepts a boolean value. Input can be any case-insensitive form of ‘true’/’false’ and ‘T’/’F’. Returns a boolean value.
| inputChoice() | Takes a list of strings and accepts one of them as input.
| inputMenu() | Similar to inputChoice(), but the choices are presented as items in a menu. Menu items can be marked with letters or numbers, using the ‘lettered’ and ‘numbered’ parameters.
| inputDate() | Accepts a date in a strftime format. We need to pass this format to the ‘formats’ parameter. Returns a datetime.date object.
| inputTime() | Accepts a time in a strftime format. Returns a datetime.time object.
| inputDatetime() | Accepts a date and time in a strftime format. Returns a datetime.datetime object.
| inputYesNo() | Accepts ‘yes’/’no’ or ‘y’/’n’ in case-insensitive form. Returns ‘yes’ or ‘no’.
| inputEmail() | Check correct email format
| inputFilepath() | Check correct path, optionally checks if file exists
| inputPassword() | Similar to input() but shows `*` instead of what the user actually wrote
___
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- PyInputPlus module in Python, GeeksforGeeks, https://www.geeksforgeeks.org/pyinputplus-module-in-python/