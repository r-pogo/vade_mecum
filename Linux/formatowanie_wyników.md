# Formatowanie wyników

| Command | Action |
|---------|--------|
| nl | wstawia numery wierszy
| fold | zawija każdy wiersz do podanej długości
| fmt | program do prostego formatowania tekstu
| pr | formatuje tekst do druku
| printf | formatuje i wyświetla dane
| groff | system formatowania dokumentów

___

## nl

`nl` numeruje wiersze.

```
└─ $ ▶nl distros.txt.txt 
     1  SUSE    I10.2   I12/07/2006$
     2  Fedora  I10     I11/25/2008$
     3  Ubuntu  I10     I11/25/2008$
```

`nl` akceptuje kilka nazw plików, przekazanych jako argumenty wiersza poleceń
lub standardowy strumień wejścia.

Podczas numerowania wierszy program `nl` posługuje się koncepcją zwaną stronami
logicznymi. Pozwala to mu na ponowne rozpoczęcie sekwencji liczbowej. Dzięki
tej opcji możemy rozpocząć numerowanie od podanej wartości i do pewnego stopnia
wpłynąć na format. Strona logiczna jest dalej dzielona na nagłówek, część
główną i stopkę. W każdej z tych sekcji można rozpocząć numerowanie i lub
zastosować inny styl. Jeśli przekażemy do programu`nl` kilka plików, będą one
traktowane jako pojedynczy strumień tekstu. Sekcje w strumieniu tekstowym są
wyznaczone na podstawie obecności znaczników umieszczonych w tekście:

| Znacznik | Znaczenie |
|---------|------------|
| \:\:\: | Początek nagłówka strony logicznej
| \:\: | Początek głównej części strony logicznej
| \: | Początek stopki strony logicznej

Każdy z powyższych elementów musi się pojawić samodzielnie w swoim własnym
wierszu. Po przetworzeniu znacznika program `nl` usuwa go ze strumienia
tekstowego.

```
# sed script to produce Linux distributions report
1 i\
\\:\\:\\:\
\
Linux Distributions Report\
\
Name Ver. Released\
---- ---- --------\
\\:\\:
s/\([0-9]\{2\}\)\/\([0-9]\{2\}\)\/\([0-9]\{4\}\)$/\3-\1-\2/
$ a\
\\:\
\
End Of Report

[me@linuxbox ~]$ sort -k 1,1 -k 2n distros.txt | sed -f distros-nl.s
ed | nl

 Linux Distributions Report

 Name Ver. Released
 ---- ---- --------
 1 Fedora 5 2006-03-20
 2 Fedora 6 2006-10-24
 3 Fedora 7 2007-05-31
 4 Fedora 8 2007-11-08
 5 Fedora 9 2008-05-13
 6 Fedora 10 2008-11-25
 7 SUSE 10.1 2006-05-11
 8 SUSE 10.2 2006-12-07
 9 SUSE 10.3 2007-10-04
 10 SUSE 11.0 2008-06-19
 11 Ubuntu 6.06 2006-06-01
 12 Ubuntu 6.10 2006-10-26
 13 Ubuntu 7.04 2007-04-19
 14 Ubuntu 7.10 2007-10-18
 15 Ubuntu 8.04 2008-04-24
 16 Ubuntu 8.10 2008-10-30

 End Of Report
```

| Option | Meaning |
|--------|---------|
| -b | style Set body numbering to style, where style is one of the following: a = number all lines t = number only non-blank lines. This is the default. n = none pregexp = number only lines matching basic regular expression regexp.
| -f | style Set footer numbering to style. Default is n (none).
| -h | style Set header numbering to style. Default is n (none).
| -i | number Set page numbering increment to number. Default is one.
| -n | format Sets numbering format to format, where format is: ln = left justified, without leading zeros. rn = right justified, without leading zeros. This is the default. rz = right justified, with leading zeros.
| -p | Do not reset page numbering at the beginning of each logical page.
| -s | string Add string to the end of each line number to create a separator. Default is a single tab character.
| -v | number Set first line number of each logical page to number. Default is one.
| -w |width Set width of the line number field to width. Default is 6

Więcej w `man nl`
___

## fold

`fold` jest procesem łamania wierszy tekstu na określonej szerokości. Akceptuje
plik lub kilka plików bądź standardowy strumień wejścia.

```
└─ $ ▶echo " Szybki brązowy lis przeskoczył nad leniwym psem." | fold -w 12
 Szybki brą
zowy lis prz
eskoczył na
d leniwym ps
em.
```

`-w` określa szerokość fragmentów wyżej 12 znaków, domyślnie 80.

```
└─ $ ▶echo " Szybki brązowy lis przeskoczył nad leniwym psem." | fold -w 12 -s
 Szybki
brązowy
lis
przeskoczył
 nad
leniwym
psem.
```

`-s` będzie łamać wiersz na miejscu najbliższego dostępnego znaku spacji, przed
osiągnięciem szerokości wiersza.
___

## fmt

Program do prostego formatowania tekstu.

| Option | Meaning |
|--------|---------|
| -c | Operate in crown margin mode. This preserves the indentation of the first two lines of a paragraph. Subsequent lines are aligned with the indentation of the second line.
| -p | string Only format those lines beginning with the prefix string. After formatting, the contents of string are prefixed to each reformatted line. This option can be used to format text in source code comments. For example, any programming language or configuration file that uses a “#” character to delineate a comment could be formatted by specifying -p '# ' so that only the comments will be formatted.
| -s | Split-only mode. In this mode, lines will only be split to fit the specified column width. Short lines will not be joined to fill lines. This mode is useful when formatting text such as code where joining is not desired.
| -u | Perform uniform spacing. This will apply traditional “typewriter style” formatting to the text. This means a single space between words and two spaces between sentences. This mode is useful for removing “justification,” that is, text that has been padded with spaces to force alignment on both the left and right margins.
|-w  |width Format text to fit within a column width characters wide. The default is 75 characters. Note: fmt actually formats lines slightly shorter than the specified width to allow for line balancing.

___

## pr

`pr` służy do dzielenia tekstu na strony. Podczas drukowania tekstu zwykle
wskazany jest podział stron za pomocą kilku pustych wierszy, aby na każdej
stronie powstał górny i dolny margines. Ponadto w pustych wierszach można
umieścić nagłówek i stopkę.

```
[me@linuxbox ~]$ pr -l 15 -w 65 distros.txt
2008-12-11 18:27            distros.txt             Page 1
SUSE    10.2    12/07/2006
Fedora  10      11/25/2008
SUSE    11.0    06/19/2008
Ubuntu  8.04    04/24/2008
Fedora  8       11/08/2007


2008-12-11 18:27            distros.txt             Page 2
SUSE    10.3    10/04/2007
Ubuntu  6.10    10/26/2006
Fedora  7       05/31/2007
Ubuntu  7.10    10/18/2007
Ubuntu  7.04    04/19/2007
```

`-l` długość strony, `-w` szerokość strony, wyżej szerokość 65 i długość 15.
Program `pr` dzieli treść pliku na strony, oddzielając każdą stronę kilkoma
pustymi wierszami, oraz tworzy domyślny nagłówek zawierający czas modyfikacji,
nazwę pliku oraz numer strony.
___

## printf

`printf` - print formatted nie jest używane w potokach nie akceptuje
standardowego strumienia wejścia. Jest wykorzystywane głównie w skryptach.
`printf "format" argumenty`

```
└─ $ ▶printf "Sformatowałem łańcuch: %s\n" foo
Sformatowałem łańcuch: foo
```
łańcuch formatowania  może zawierać zwykły tekst (np. „Sformatowałem ciąg:”), 
sekwencje specjalne (takie jak \n, czy znak nowego wiersza) i sekwencje rozpoczynające się od znaku %,
zwane specyfikacjami formatowania. W powyższym przykładzie specyfikator
%s służy do sformatowania ciągu „foo” i umieszczenia go w tekście zwracany przez 
polecenie.

```
└─ $ ▶printf "Sformatowałem '%s' jako łańcuch.\n" foo
Sformatowałem 'foo' jako łańcuch.
```
W zwaracanym łańcuchu specyfikator formatowania % został zastąpiony łańcuchem foo.
Formatowanie `s` słuzy do sformatowania danych testowych typu ciąg znaku.

| Specyfikator | Opis |
|--------------|------|
| d | Format a number as a signed decimal integer.
| f | Format and output a floating point number.
| o | Format an integer as an octal number.
| s | Format a string.
| x | Format an integer as a hexadecimal number using lowercase a-f where needed.
| X | Same as x but use uppercase letters.
| % | Print a literal % symbol (i.e., specify “%%”)

```
└─ $ ▶printf "%d, %f, %o, %s, %x, %X\n" 380 380 380 380 380 380
380, 380.000000, 574, 380, 17c, 17C
```
Do specyfikatora formatowania możemy dodać kilka opcjonalnych komponentów, które pozwolą dostosować wyniki.
Kompletny specyfikator formatowania może wyglądać następująco:
`%[flags][width][.precision]conversion_specification`
Jeżeli używamy kilku komponentów opcjonalnych, musimy je umieścić w koljeności przedstawionej powyżej, 
w przeciwnym razie nie zostaną odpowiednio zinterpretowane.

| Komponent | Opis |
|--------------|------|
| flags | There are five different flags: # – Use the “alternate format” for output. This varies by data type. For o (octal number) conversion, the output is prefixed with 0. For x and X (hexadecimal number) conversions, the output is prefixed with 0x or 0X respectively. 0–(zero) Pad the output with zeros. This means that the field will be filled with leading zeros, as in “000380”. - – (dash) Left-align the output. By default, printf right-aligns output. ‘ ’ – (space) Produce a leading space for positive numbers. + – (plus sign) Sign positive numbers. By default, printf only + signs negative numbers. 
| width | A number specifying the minimum field width.
| .precision | For floating point numbers, specify the number of digits of precision to be output after the decimal point. For string conversion, precision specifies the number of characters to output.
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
