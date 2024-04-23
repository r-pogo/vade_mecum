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