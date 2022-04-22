# import re
___
## MetaCharacters
````
.  --> Any Character Except New Line
\d --> Digit (0-9)
\D --> Not a Digit [^0-9]
\w --> Word Character (a-z, A-Z, 0-9, _)
\W --> Not a word Character
\s --> Whitespace (space, tab, newline)
\b --> Word Boundary
\B --> Not a Word Boundary
\A --> Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.
\Z --> Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.
\n --> Matches a newline character
\t --> Matches tab character
^ --> Beginning of a String
$ --> End of a String
[] --> Matches Characters in brackets -  no need to escape characters inside e.g.: [-.] ---> ! either a dash or a 
dot not both and not two dashes or two dots - w tym miejscu będzie jeden z tych znaków’
[^ ] --> Matches Characters NOT in brackets
- --> Dash between values specify a range [a-zA-Z] only letters
| --> Either Or
( ) --> Group e.g: (r|s|rs) match r OR s OR rs
(?:...) --> Non capturing group
(?#)  --> Comment
(?PAB) --> Matches the expression AB, and it can be accessed with the group name
(?P=name) --> Matches the expression matched by an earlier group named “name”.
(...)\1 -->  The number 1 corresponds to the first group to be matched. If we want to match more instances of the same
expression, simply use its number instead of writing out the whole expression again. We can use from 
1 up to 99 such groups and their corresponding numbers.
````
___
## Assertions
````
A(?=B) -->  Lookahead assertion. This matches the expression A only if it is followed by B
A(?!B)  --> Negative lookahead assertion. This matches the expression A only if it is not followed by B.
(?<=B)A -->  Positive lookbehind assertion. This matches the expression A only if B is immediately to its left. T
his can only matched fixed length expressions.
(?<!B)A --> Negative lookbehind assertion. This matches the expression A only if B is not immediately to its left. 
This can only matched fixed length expressions.
(?()|) --> If else conditional

?>  --> Once-only Subexpression - Not sure if it works in python 
?() --> Condition [if then] - Not sure if it works in python
?()! --> Condition [if then else] - Not sure if it works in python
````
___
## Quantifiers
````
* - 0 or More
+ - 1 or More
? - 0 or One
{3} - Exact Number
{3,4} - Range of Numbers (Minimum, Maximum)
{2,} - 2 or more
{,5} - Up to 5

Regex patterns are by defoult greedy, they are looking for the widest possible range of fit. 
Lazy patterns find the smallest possible number of characters instead of the largest before they give up checks on the 
rest of the Expression. They are defined by adding --> "?"
*?
+?
{n,}?
````
___
## METHODS

| Functions | Explanation |
|-----------|-------------|
| re.Match  | It will search the regular expression pattern and return the first occurrence.
| re.search | It takes a regular expression pattern and a string and searches for that pattern within the string.If the search is successful, search() returns a match object or None otherwise.
|re.fullmatch| It will return a match object if and only if the entire string matches the pattern. Otherwise, it will return None. # TODO
|re.compile | It can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search for a pattern again without rewriting it.
|re.sub     | It is used to replace occurrences of a particular sub-string with another sub-string
|re.escape  | It will return a string with all non-alphanumerics backslashed. this is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it. # TODO
|re.split   | It will split a string by multiple delimiters.
|re.findall | It will return all non-overlapping matches of pattern in the string, as a list of strings.
|re.subn    | It will return the new string along with the no. of replacements.

### re.compile
Compile a regular expression pattern into a regular expression object, which can be used for matching using its 
match(), search() and other methods. 
````python
pattern = re.compile(r'abc')
match = pattern.match("abc mam cos tam abc")
print(match)
Output <re.Match object; span=(0, 3), match='abc'>
````
___
### re.findall()
The re.findall() method returns a list of strings containing all matches.
If the pattern is not found, re.findall() returns an empty list.
````python
Extract numbers from a string
string = 'hello 12 ciao 89. Dziendoberek 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)
Output: ['12', '89', '34']
````
___
### raw strings
When r prefix is used before a regular expression, it means raw string. For example, 
'\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n. 

Backlash \ is used to escape various characters including all metacharacters. However, using r prefix makes \ treat 
as a normal character. 
````python
special_char = '\n and \t are special characters.'
result = re.findall(r'[\n\t]', special_char)
print(result)
Output: ['\n', '\t']
````
___
### re.split()
The re.split method splits the string where there is a match and returns a list of strings where the splits 
have occurred. If the pattern is not found, re.split() returns a list containing the original string.
````python
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)
Output: ['Twelve:', ' Eighty nine:', '.']
````

You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur
The default value of maxsplit is 0; meaning all possible splits.
````python
string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'
maxsplit = 1
split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)
Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
````
___
### re.sub()
The syntax of re.sub() is: re.sub(pattern, replace, string)
The method returns a string where matched occurrences are replaced with the content of replace variable.
If the pattern is not found, re.sub() returns the original string.
````python
Program to remove all whitespaces
multiline string
string = 'abc 12\
de 23 \n f45 6'

matches all whitespace characters
pattern = '\s+'

empty string
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)
Output: abc12de23f456
````
You can pass count as a fourth parameter to the re.sub() method. If omitted, it results to 0. This will replace all 
occurrences
````python
multiline string
string = 'abc 12\
de 23 \n f45 6'

matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, count=1)
print(new_string)

Output:
abc12de 23
f45 6
````
Another way for replacing
````python
agentNamesRegex = re.compiler(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Karolina that Agent Eve knew about the double role of Agent Beatrix')
Output:
A**** told K*** that E**** knew about the double role of B****
````
___
### re.subn()
The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number 
of substitutions made.
````python

# Program to remove all whitespaces

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)
Output: ('abc12de23f456', 4)
````
___
### re.search()
The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where 
the RegEx pattern produces a match with the string. 
If the search is successful, re.search() returns a match object; if not, it returns None. 
match = re.search(pattern, str)
````python
# Example
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")

Output: pattern found inside the string
Here, match contains a match object
````
___
## Match object
You can get methods and attributes of a match object using dir() function.
Some of the commonly used methods and attributes of match objects are:

### Group method - match.group()
The group() method returns the part of the string where there is a match.
````python
string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")

Output: 801 35
Here, match variable contains a match object.
````
Our pattern (\d{3}) (\d{2}) has two subgroups (\d{3}) and (\d{2}). You can get the part of the string of these
parenthesized subgroups. Here's how:
````python
>>> match.group(1)
'801'

>>> match.group(2)
'35'
>>> match.group(1, 2)
('801', '35')

>>> match.groups()
('801', '35')
````
___
### match.start(), match.end() and match.span()
The start() function returns the index of the start of the matched substring. Similarly, end() returns the end 
index of the matched substring. 
````python
>>> match.start()
2
>>> match.end()
8
The span() function returns a tuple containing start and end index of the matched part.
>>> match.span()
(2, 8)
````
___
### match.re and match.string
The re attribute of a matched object returns a regular expression object. Similarly, string attribute returns the 
passed string.
````python
>>> match.re
re.compile('(\\d{3}) (\\d{2})')

>>> match.string
'39801 356, 2102 1111'
````
___
## FLAGS
___
### VERBOSE
````
phoneRegex = re.compiler(r'''(
(\d{3}|(\d{3}\))?           # Area code
(\s|-|\.)?                  # Separator
\d{3}                       # First three numbers
(\s|-|\.)                   # Separator
\d(4)                       # Last four numbers
(\s*(ext|x|ext.)\s\*\d{2,5})? # external number
)''', re.VERBOSE
````
___
### Other flags
How to "pipe" flags:
````
regex = re.compile(foo, re.IGNORCASE | re.DOTALL | re.VERBOSE)
````
DOTALL falg: all characters including a new line character
````
re.DOTALL
````
___
## Sources used for the creation of this cheat sheet
- B. Forta, Learning Regular Expressions, Addison-Wesley 2018
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
- Programiz, Python RegEx, https://www.programiz.com/python-programming/regex


