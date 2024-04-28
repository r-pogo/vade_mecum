# Interpretation
Each time you type a command line and press the enter key, bash performs several 
processes upon the text before it carries out your command.
The process that makes this happen is called expansion. With expansion, you enter 
something and it is expanded into something else before the shell acts upon it.

| Command | Action |
|--------------|--------|
| echo | display a line of text
``` 
echo ~
/home/elski
```

`~` tilde has a special meaning when used at the beginning of a word, it expands into the name of the 
home directory of the named user, or if no user is named, the home directory of the cur
rent user.
___
## Interpretation of arithmetic expressions
| Operator | Description |
|--------------|--------|
| + | addition
| - | subtraction
| * | multiplication
| / | division integers
| % | modulo
| ** | exponentiation

The interpretation of arithmetic expressions requires the use of the following syntax:
`$((expression))`
````
echo $((2 + 2))
4
````
Space characters have no meaning, and the expressions themselves can be nested:
````
echo $(($((5**2)) *     3))
75
Same as above

echo $(((5**2) * 3))
75
````
___
## Bracket interpretation
This technique allows to create strings based on a pattern.
The pattern cannot contain white space not enclosed in quotation marks.
````
echo Front-{A, B, C}-Back
Fornt-A-Back, Fornt-B-Back, Fornt-C-Back

echo Number_{1..3}
Number_1 Number_2 Number_3

echo {01..15}
01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

echo {001..15}
001 002 003 004 005 006 007 008 009 010 011 012 013 014 015

echo {Z..A}
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

Nested pattern:
echo a{A{1,2},B{3,4}}b
aA1b aA2b aB3b aB4b

Useful for directory and files creation:
mkdir Photos
cd Photos
mkdir {2007,,2009}-0{1..12}
ls
2007-01  2007-07  2008-01  2008-07  2009-01  2009-07
2007-02  2007-08  2008-02  2008-08  2009-02  2009-08
2007-03  2007-09  2008-03  2008-09  2009-03  2009-09
2007-04  2007-10  2008-04  2008-10  2009-04  2009-10
2007-05  2007-11  2008-05  2008-11  2009-05  2009-11
2007-06  2007-12  2008-06  2008-12  2009-06  2009-12
````
___
## Parameter interpretation
To view the contents of the USER variable:
```
echo $USER
elski
```
To view a list of available variables:
`printenv | less`
___
## Interpretation on command result
````
ls -l $(which cp)
-rwxr-xr-x 1 root root 71564 2007-12-05 80:58 /bin/cp
````
Here the result of `which cp` is redirected to `ls` w obtain a list of the localization of `cp`
We can also use more complex commands:
`file $(ls /usrt/bin/* | grep zip)`
___
## Shutting down the interpretation mechanism
| Sign | Action |
|------|--------|
|`""` | Double quotation mark will turn off the interpretation of all special characters apart from `$, \, left apostrophes`. Also the interpretation of parameters, arithmetic and command result will be carried on.
`' '` Single quotation mark turn off everything.
`\` backslash to turn off interpretation of the following sign like \\ o \$ is also used for some special characters like \t for tab

```
Double quotation mark dosen't stop the interpretation of parameters, arithmetic calculation and evaluation of commands
echo "$USER $((2+2)) $(cal)"
elski 4    December 2022
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24

echo "writing     a     test"
writing     a     test

!!!
echo $(cal)
December 2022 Su Mo Tu We Th Fr Sa 1 2 3  4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31

echo "$(cal)"
   December 2022
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

Single quotation mark:
echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER

```
___
## Backslash
Backslash represents also some special characters called control characters.

| Control character | Action |
|-------------------|--------|
| \a | alarm
| \b | backspace
| \n | new line
| \r | carriage return
| \t | tab
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019

