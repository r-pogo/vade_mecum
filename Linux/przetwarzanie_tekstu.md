# Przetwarzanie tekstu

| Command | Action |
|---------|--------|
| cat | łączy pliki i wipisuje ich zawartości w standardowym strumieniu wyjścia
| sort | sortuje wiersze plików tekstowych
| uniq | zgłasza lub pomija powtarzające się wiersze
| cut | usuwa fragmenty z każdego wiersza plików
| paste | łączy wiersze plików
| join | łączy wiersze dwóch plików na podstawie wspólnego
| comm | porównuje dwa posortowane pliki wiersz po wierszu
| diff | porównuje pliki wiersz po wierszu
| patch | dołącza do oryginału plik z różnicami
| tr | transliteruje lub usuwa znaki
| sed | edytor strumieniowy służący do filtrowania i przekształcania tekstu
| aspell | interaktywny program do sprawdzania pisowni

## cat
`cat` ma wiele zastosowań i ciekawych opcji np. `-A`, która służy do wyświetlania znaków niedrukowalnych w tekście.  
```
$ ▶cat > foo.txt
Szybki brązowy lis przeskoczył nad leniwym psem.
# Ctrl + D
$ ▶cat -A foo.txt 
^ISzybki brązowy lis przeskoczył nad leniwym psem.$
```
`^I` to Ctrl + I czyli znak tabulacji. `$` na końcu wiersza oznacza brak znaku spacji. 
Opcja `-n` służy do numerowania wierszy, `-s` do usuwania wielokrotnych pustych wierszy, w przykładzie były dwa puste wiersze:  
```
$ ▶cat -ns foo.txt 
     1  Szybki brązowy lis
     2
     3  przeskoczył nad leniwym psem.
```
___
## sort
`sort` sortuje zawartość standardowego strumienia wejścia lub jednego albo kilku plików  
podanych w wierszu poleceń oraz wysyła wyniki do standardowego strumienia wyjścia.
```
$ ▶sort > foo.txt 
c
b
a
# Ctrl + D
$ ▶cat foo.txt 
a
b
c
```
Sortowanie wielu plików:
`$ ▶ sort file1 file2 file3 > final_sorted_list.txt`  

`-n` służy do sortowania numerycznego. Przykład z wykorzystaniem `du`
````
$ ▶du -s /usr/share/* | sort -nr | head
77204   /usr/share/locale
54640   /usr/share/doc
43600   /usr/share/icons
34376   /usr/share/vim
31716   /usr/share/man
22604   /usr/share/fonts
20020   /usr/share/perl
16716   /usr/share/i18n
12668   /usr/share/qt5
12272   /usr/share/poppler
````
`head` do wyświetlania pierwszych 10 wyników. Korzystając z opcji `n` oraz `r`, tworzymy listę odwrotnie posortowaną  
na podstawie wartości liczbowych, w której największa liczba znajduje się na początku wyników.
To sortowanie tu działa, ponieważ na początku każdego wiersza znajdują się wartości liczbowe.
Ale polecenie `sort` może także przetwarzać poszczególne pola, które może być wskazana za pomocą opcji `-k`:  
```
$ ▶ls -l /usr/bin |sort -nr -k 5 | head
-rwxr-xr-x 1 root   root    25045392 May 29  2023 snap
-rwxr-xr-x 1 root   root     5766288 Jun  6  2023 python3.9
-rwxr-xr-x 1 root   root     5494584 May 26  2023 python3.8
-rwxr-xr-x 1 root   root     3662032 Jul  1  2022 python2.7
-rwxr-xr-x 2 root   root     3478464 May 23  2023 perl5.30.0
-rwxr-xr-x 2 root   root     3478464 May 23  2023 perl
-rwxr-xr-x 1 root   root     3121744 Apr 26  2023 git
-rwxr-xr-x 1 root   root     2910952 May 24  2023 vim.basic
-rwxr-xr-x 1 root   root     2643064 Oct 11  2022 fzf
-rwxr-xr-x 1 root   root     2312584 Jun 13  2023 x86_64-linux-gnu-ld.gold
```
Białe znaki są wykorzystywane jako separatory pomiędzy polami i separatory wchodzą w skład pola podczas sortowania.  
Można również sortować na więcej niż jednym polu:
```sort -k1,1 -k 2n foo.txt
#Albo
soet --key=1,1 --key=2n foo.txt
```
`1,1` tu ograniczamy do sortowania do pierwszego pola, oznacza "rozpocznij od pola1 i skończy na polu 1"
`2n` oznacza, że kluczem sortowania jes pole 2 oraz że sortowanie powinno być numeryczne.
Na końcu wartości opcji klucza możemy umieścić literę opcji określającej typ sortowania, jakie chcemy przeprowadzić:
`b` ignoruje białe znaki na początku
`n` sortowanie numeryczne
`r` sortowanie odwrotne
etc.
Opcja `key -k` pozwala określić przesunięcie wewnątrz pól, dzięki czemu możemy zdefiniować klucze wewnątrz pól:
`sort -k 3.7nbr -k 3.1nbr -k 3.4nbr foo.txt`
Opcja `-k 3.7` sprawia, że pole `sort` będzie sortować według klucza, który rozpoczyna się od siódmego znaku w trzecim polu.
Co, jeśli plik nie używa białych znaków do separacji? Ale np. `:`?
W takich sytuacjach używamy `-t` do określenia znak separatora.
`sort -t ':' -k 7 /etc/passwd | head`

## uniq
`uniq` domyślnie usuwa wszystkie powtarzające się wiersze i i wyśle wynik do standardowego strumienia wyjścia. Często używany razem z `sort`
```
$ ▶cat > foo.txt
a
b
c
a
b
c
# Crl + D
$ ▶uniq foo.txt 
a
b
c
a
b
c
```
Duplikaty nie zostały usunięte!!! Aby polecenie `uniq` wykonało swoje zadanie, najpierw należy
posortować plik wejściowy.
```
$ ▶sort  foo.txt | uniq
a
b
c
```
Często wykorzystywane opcje:

| Opcja | Długa opcja | Opis |
|-------|-------------|------|
| -c | --count | Wyświetla listę powielonych wierszy poprzedzonych liczbą określającą, ile razy wystąpił dany wiersz
| -d | --repeated | Wyświetla tylko powielone wiersze
| -f n | --skip-fields=n | Ignoruje n początkowych pól w każdym wierszu. Pola są oddzielone przez białe znaki, nie ma opcji do ustawiania alternatywnego separatora pól
| -i | --ignore-case | Ignoruje wielkość liter
| -s n | --skip-chars=n | Ignoruje n początkowych znaków w każdym wierszu
| -u | --unique | Wyświetla jedynie unikalne wiersze

## cut
