# Interpretation
| Abbreviation | Effect |
|--------------|--------|
| echo | display a line of text

## Interpretation of arithmetic expressions
| Operator | Description |
|--------------|--------|
| + | addition
| - | subtraction
| * | multiplication
| / | division integers
| % | modulo
| **| exponentiation
````
$((expression))

echo $((2 + 2))
````
___
## Bracket interpretation
````
echo Front-{A, B, C}-Back
Fornt-A-Back, Fornt-B-Back, Fornt-C-Back

echo Liczba_{1..3}
Liczba_1 Liczba_2 Liczba_3
````
____
## Interpretation on command result
````
ls -l $(which cp)
-rwxr-xr-x 1 root root 71564 2007-12-05 80:58 /bin/cp
````
Here the result of `which cp` is redirected to `ls` w obtain a list of the localization of `cp`

````
file $(ls /usrt/bin/* | grep zip)
````
___
## Shutting down the interpretation mechanism
`" "` Double quotation mark will turn off the interpretation of all special characters apart from 
$, \, apostrophes,
`' '` Single quotation mark turn off everything
`\` backslash to tun off interpretation of the following sign like \\ o \$ is also used for some special characters like \t for tab
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019

