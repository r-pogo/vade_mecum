# Drukowanie

| Command | Action |
|---------|--------|
| pr | przekształca pliki tekstowe przeznaczone do druku
| lpr | drukuje pliki
| a2ps | formatuje pliki przeznaczone do druku na drukarce PostScript
| lpstat | wyświetla informacje o stanie drukarki
| lpq | wyświetla status kolejki drukarki
| lprm | anuluje zadania drukowania


Nowoczesne systemy Linux wykorzystują dwa pakiety oprogramowania do zarządzania drukiem. 
Pierwszy to `CUPS (Common Unix Printing System)` zapewnia sterowniki drukowania i mechanizmu zarządzania zadaniami drukowania.
Drugi to `Ghostscript`, interpreter PostScriptu, działa jak procesor RIP.
CUPS zarządza drukarkami, tworząc i zarządzając `kolejkami drukowania`. 
Drukowanie w systemie Unix zostało pierwotnie zaprojektowane jako proces zarządzania scentralizowaną drukarką, współdzieloną przez wielu użytkowników. 
Ponieważ drukarki są z natury powolne w porównaniu do komputerów, które przekazują im treść,
systemy drukowania wymagają sprawnego planowania wielu zadań drukowania i zapewnienia organizacji całego procesu. 
CUPS umożliwia też rozpoznawanie różnych typów danych (w granicach rozsądku) i może przekształcić pliki do drukowalnej postaci.

## pr - przekształcenie pliko tesktowych przeznaczonych do druku
`pr` jest wykorzystywany do dopasowania tekstu do określonego rozmiaru strony, z uwzględnieniem  
opcjonalnych nagłówków i marginesów strony.
Zwykle używany w potokach jako filtr.

Lista zawartości katalogu /usr/bin sformatowana za pomocą programu `pr` w 
stronicowany, trzykolumnowy układ:
```
└─ $ ▶ls /usr/bin | pr -3 -w 65 | head


2024-04-23 21:41                                           Page 1


2to3-2.7              btrfs-convert         c_rehash
GET                   btrfs-find-root       caca-config
HEAD                  btrfs-image           cal
NF                    btrfs-map-logical     calendar
POST                  btrfs-select-super    captoinfo

```

| Option | Meaning |
|--------|---------|
|  +first[:last] | Output a range of pages starting with first and, optionally, ending with last.
| -columns | Organize the content of the page into the number of columns specified by columns.
| -a | By default, multicolumn output is listed vertically. By adding the -a (across) option, content is listed horizontally. 
| -d | Double-space output.
| -D “format” | Format the date displayed in page headers using format. See the man page for the date command for a description of the format string.
| -f | Use form feeds rather than carriage returns to separate pages.
| -h “header” | In the center portion of the page header, use header rather than the name of the file being processed.
| -l length | Set page length to length. Default is 66 (US letter at 6 lines per inch)
| -n | Number lines.
| -o offset | Create a left margin offset characters wide.
| -w width | Set page width to width. Default is 72.
___
## lpr styl Berkeley
`lpr` służy do przesyłania plików do drukarki, można z niego korzystać także w potokach, akceptuje standardowy strumień wejścia.  
`$ ▶ ls /usr/bin | pr -3 | lpr`
Raport zostałby wysłany do domyślnej drukarki. `-P` aby wysłać plik do innej drukarki.  
`lpr -P nazwa_drukarki`  
Aby wyświetlić listę drukarek rozpoznawanych przez system:  
`lpstat -a`  

| Option | Meaning |
|--------|---------|
| -# number | Set number of copies to number.
| -p | Print each page with a shaded header with the date, time, job name, and page number. This so-called “pretty print” option can be used when printing text files.
| -P printer | Specify the name of the printer used for output. If no printer is specified, the system’s default printer is used.
| -r | Delete files after printing. This would be useful for programs that produce temporary printer-output files.
___
## lp styl Systemu V
`lp` akceptuje pliki lub standardowe wejście jako źródło drukowania, różni się od `lpr` tym, 
że wspiera nieco bardziej zaawansowany zestaw opcji.  
`$ ▶ ls /usr/bin | pr -4 -w 90 -l 88 | lp -o page-left=36 -o cpi=12 -o`

| Option | Meaning |
|--------|---------|
| -d printer | Set the destination (printer) to printer. If no d option is specified, the system default printer is used.
| -n number | Set the number of copies to number.
| -o landscape | Set output to landscape orientation.
| -o fitplot | Scale the file to fit the page. This is useful when printing images, such as JPEG files.
| -o scaling=number | Scale file to number. The value of 100 fills the page. Values less than 100 are reduced, while values greater than 100 cause the file to be printed across multiple pages.
| -o cpi=number | Set the output characters per inch to number. Default is 10.
|-o lpi=number | Set the output lines per inch to number. Default is 6
| -o page-bottom=points -o page-left=points -o page-right=points -o page-top=points | Set the page margins. Values are expressed in points, a unit of typographic measurement. There are 72 points to an inch.
| -P pages | Specify the list of pages. pages may be expressed as a comma-separated list and/or a range. For example “1,3,5,7-10
___
## a2ps
`a2ps` służy konwersji formatu, ale nie tylko. Kiedyś ASCII to PostScript teraz 
to Anything to PostScript. Chociaż nazwa sugeruje, że jest to program do konwersji formatu, w rzeczywistości
służy do drukowania. Zamiast standardowego strumienia wyjścia przesyła do domyślnej drukarki systemu swoje
domyślne wyjście.
```
$ ▶ ls /usr/bin | pr -3 -t | a2ps -o ~/Desktop/ls.ps -L 
66 
[stdin (plain): 11 pages on 6 sheets] 
[Total: 11 pages on 6 sheets] saved into the file `/home/me/Desktop/
 ls.ps
```
W powyższym przykładzie filtrujemy strumień za pomocą programu `pr` z opcją `-t` (pomija nagłówki i stopki)
Następnie, korzystając z programu `a2ps`, określamy plik wynikowy (opcja -o) oraz 66 wierszy na stronę (opcja -L)
co pasuje do stron uzyskanych w programie `pr`.
___
## lpstat
`lpstat` przydatny do ustalenia nazwy i dostępności drukarek w systemie.
Jeśli w systemie znajduje się zarówno drukarka fizyczna (o nazwie printer), jak i wirtualna
drukarka PDF, ich status można sprawdzić w następujący sposób:
```
$ ▶ lpstat -a 
PDF accepting requests since Mon 08 Dec 2008 03:05:59 PM EST 
printer accepting requests since Tue 24 Feb 2009 08:43:22 AM EST
```
Bardziej szczegółowy opis konfiguracji systemu:
```
$ ▶ lpstat -s 
system default destination: printer 
device for PDF: cups-pdf:/ 
device for printer: ipp://print-server:631/printers/printer
```
| Option | Meaning |
|--------|---------|
| -a [printer...] | Display the state of the printer queue for printer. Note that this is the status of the printer queue’s ability to accept jobs, not the status of the physical printers. If no printers are specified, all print queues are shown.
| -d | Display the name of the system’s default printer.
| -p [printer...] | Display the status of the specified printer. If no printers are specified, all printers are shown.
| -r | Display the status of the print server.
| -s | Display a status summary.
| -t | Display a complete status report.
___
## lpq
`lpq` pozwala na wyświetlenie statusu kolejki i zadań drukowania w kolejce.
```
$ ▶ lpq 
printer is ready 
no entries
```
Jeśli nie przekażemy nazwy drukarki (za pomocą opcji -P), wyświetlona zostanie kolejka domyślnej drukarki systemu.
Jeśli prześlemy zadania do drukarki, a następnie sprawdzimy kolejkę, zobaczymy, że zadanie znajduję się na liście:
```
$ ▶ ls *.txt | pr -3 | lp 
request id is printer-603 (1 file(s))
 [me@linuxbox ~]$ lpq 
printer is ready and printing 
Rank    Owner   Job     File(s)                         Total Size 
active  me      603     (stdin)                         1024 bytes
```
___
## lprm i cancel
CUPS zawiera dwa programy służące do kończenia zadań drukowania i usuwania ich z kolejki drukowania.
`lprm` w stylu Berkeley i `cancel` w stylu Systemu V.
Jak zatrzymać i usunąć zadanie drukowania:
```
$ ▶ cancel 603
$ ▶ lpq 
printer is ready 
no entries
```
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019