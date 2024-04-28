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
___
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
___
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
___
## cut
`cut` służy do wyodrębniania sekcji tekstu z wiersza i zwrócenia tej sekcji do standardowego strumienia wyjścia.  
Program ten akceptuje kilka nazw plików w postaci argumentów lub dane ze standardowego strumienia wejścia.
Sekcji wiersza, która ma zostać wyodrębniona jest zdefinowana za pomocą opcji:  

| Opcja | Długa opcja | Opis |
|-------|-------------|------|
| -c lista | --characters=lista | Wyodrębnia fragment wiersza zdefiniowany przez listę. Lista może zawierać zakres liczbowy lub kilka zakresów liczbowych oddzielonych przecinkami
| -f lista | --fields=lista | Wyodrębnia co najmniej jedno pole z wiersza zgodnie z definicją w liście. Lista może zawierać jedno pole lub kilka pól lub zakresów pól oddzielonych przecinkami
| -d znak_sep | --delimiter=znek_sep | Domyślnie pola musszą być oddzielone jednym znakiem tabulacji
| | --complement | Wyodrębnia cały wiersz tekstu z wyjątkiem fragmentów określonych za pomocą opcji -c i/lub -f

````
└─ $ ▶cat -A distros.txt.txt 
SUSE^II10.2^II12/07/2006$^M$
Fedora^II10^II11/25/2008$^M$

# tylko pojedyncze znaki tabulacji

└─ $ ▶cut -f 3 distros.txt.txt 
I12/07/2006$
I11/25/2008$
I11/25/2008$

└─ $ ▶cut -f 3 distros.txt.txt | cut -c 8-11
2006
2008
2008

└─ $ ▶ cut -c 13- # od 13 znaku do końca
````
Podczas pracy z polami możemy zdefiniować inny separator pola zamiast znaku tabulacji:  
```
└─ $ ▶cut -d ':' -f 1 /etc/passwd | head
root
daemon
bin
sys
sync
games
man
lp
mail
news
```
___
## paste
`paste` dodaje kolumnę lub kolumny tekstu do pliku. Odczytuje wiele plików i łączy pola
znalezione w każdym pliku w jeden standardowy strumień wyjścia.  
```
 $ ▶paste numbers.txt distros.txt.txt 
1       SUSE    I10.2   I12/07/2006$
2       Fedora  I10     I11/25/2008$
3       Ubuntu  I10     I11/25/2008$
```
___
## join
`join`trochę jak JOIN z SQL, łączy dane z wielu plików na podstawie wspólnego pola kluczowego.  
___
## comm
`comm` porównuje dwa liki tekstowe, wyświetlając wiersze, które są unikalne w każdym z plików, oraz wiersze wspólne.  

```
└─ $ ▶comm file1.txt file2.txt 
a  # pierwsza kolumna zawiera wiersze unikalne dla pierwszego argumentu
                b
                c    # trzecia kolumna wspólne
                d
        e # pierwsza kolumna zawiera wiersze unikalne dla drugiego argumentu
```
`comm` przyjmuje opcję -n, która może mieć wartości 1,2,3. Opcje te określają, które kolumny należy pominąć w zwracanym wyniku.
___
## diff
```
└─ $ ▶diff file1.txt file2.txt 
1d0
< a
4a4
> e
```
Postać zakres operacja zakres i służy do opisu pozycji i rodzajów zmian wymaganych do przekształcenia pierwszego pliku w drugi plik.
Bardziej popularne formaty to:
Format kontekstowy
```
└─ $ ▶diff -c file1.txt file2.txt 
*** file1.txt   2024-04-18 22:27:10.938611700 +0200
--- file2.txt   2024-04-18 22:27:34.802784400 +0200
***************
*** 1,4 **** # określa wiersze od 1 do 4 w pierwszym pliku
- a
  b
  c
  d
--- 1,4 ---- # określa wiersze od 1 do 4 w drugim pliku
  b
  c
  d
+ e
```
| Wskaźnik | Znaczenie |
|----------|-----------|
| brak | Wiersz wyświetlony dla kontekstu. Nie ma różnicy
| - | Usunięty wiersz. Zostanie wyświetlony w pierwszym pliku a w drugim już nie
| + | Dodany wiersz. Zostanie wyświetlony w drugim pliku
| ! | Zmieniony wiersz. Wyświetlone zostaną dwie wersje wiersza, każda w odpowiedniej sekcji zmienionej grupy

Format zuniformizowany:
```
└─ $ ▶diff -u file1.txt file2.txt 
--- file1.txt   2024-04-18 22:27:10.938611700 +0200
+++ file2.txt   2024-04-18 22:27:34.802784400 +0200
@@ -1,4 +1,4 @@ # wiersze z pierwszego i drugiego pliku
-a
 b
 c
 d
+e
```
___
## patch
`patch` służy do aplikowania zmian na plikach tekstowych, przyjmuje wynik z programu `diff`.
Dokumentacja GNU sugeruje następujący sposób użycia programu `diff` na potrzeby programu `patch:  

`diff -Naur stary_plik nowy_plik > plik_różnic`  
opcja `r` rekursywne przetwarzanie katalogów  
Po utworzeniu pliku różnic możemy go dołączyć do starego pliku, tworząc nowy plik:  
`patch < plik_różnic`

```
└─ $ ▶diff -Naur file1.txt file2.txt > patchfile.txt

└─ $ ▶patch < patchfile.txt 
patching file file1.txt

└─ $ ▶cat file1.txt 
b
c
d
e
```
___
## tr
`tr` służy do transliteracji znaków - znajdz i zamień.  
```
└─ $ ▶echo "lowercase letters" | tr a-z A-Z
LOWERCASE LETTERS
```
Akceptuje dwa argumenty: zestaw znaków, które mają być przekształcone, oraz odpowiadający im
zestaw znaków, na które należy je przekształcić. Zestaw znaków można przekazać na kilka sposobów:
- lista wyliczalna np. ABCDEFGHIJKLMNOPQRSTUVWXYZ
- zakres znaków np. a-z
- klasy znaków POSIX np. [:upper:]

Oprócz transliteracji program `tr` pozwala na proste usuwanie znaków ze strumienia wejściowego za pomocą opcji `-d`.

Korzystając z opcji `-s` można usunąć powtarzające się znaki:
```
└─ $ ▶echo "aabbbcccccc" | tr -s ab
abcccccc
```
___
## sed
`sed` stream editor 
Zasadniczo sposób działania programu `sed` polega na przekazaniu pojedynczego polecenia 
edycji (w wierszu poleceń) lub nazwy pliku skryptu zawierającego wiele poleceń, a następnie wykonaniu
każdego z tych poleceń na każdym wierszu tekstu ze strumienia.
```
└─ $ ▶echo "front" | sed 's/front/back/'
back
```
Polecenia programu `sed` rozpoczynają się od liter. W powyższym przykładzie `s` substytucja.  
Po czym następuje łańcuch wyszukiwania i zmiany rozdzielone znakiem lewego ukośnika, służący jako separator. 
Ale to tylko konwencja separatorem może być dowolny znak, może to ułatwić czytelność:  
```
└─ $ ▶echo "front" | sed 's_front_back_'                                                                                                                                                                                                
back
```
Większość poleceń w programie `sed` można poprzedzić adrsem, okerślającym, który wiersz (które wiersze)  
strumienia wejściowego ma być edytowany. Jeśli pominiemy adres polecenie zostanie wykonane na każdym wierszu.
Najprostszą formą adresu jest numer wiersza:
```
└─ $ ▶echo "front front" | sed '1s_front_back_'
back front
```
Adresy można podawać na wiele sposobów:

| Adres | Opis |
|-------|------|
| n | Numer wiersza, n to dodatnia pełna liczba
| $ | Ostatni wiersz
| /regexp/ | Wiersze pasujące do podstawowych wyrażeni POSIX. Opcjonalnie regexa można umieścić między innymi znakami, \cregexpc, gdzie c jest alternatywnym znakiem
| adr1,adr2 | Zestaw wierszy od adresu adr1 do adr2 włącznie. Adresy mogą mieć dowolną postać z opisanych powyżej
| pierwszy~krok | Pasuje do wiersza reprezentowanego przez liczbę pierwszy, a następnie do wszystkich koljenych wierszy w odstępach o wartości krok. Np. 1~2 określa każdy nieparzysty wiersz, a 5~5 co piąty wiersz, począwszy od wiersza 5
| adr1,+n | Pasuje do adr1 oraz kolejnych n wierszy
| adr! | Pasuje do wszystkich wierszy z wyjątkiem adr, który może mieć jedną z powyższych postaci

```
└─ $ ▶sed -n '/SUSE/p' distros.txt.txt 
SUSE    I10.2   I12/07/2006$

# So, in the context of your command sed -n '/SUSE/p' distros.txt.txt, 
#the combination of -n suppresses automatic printing, and /SUSE/p prints 
# only the lines containing the string 

└─ $ ▶sed -n '/SUSE/!p' distros.txt.txt
Fedora  I10     I11/25/2008$
Ubuntu  I10     I11/25/2008$

# ! to negacja
```

Podstawowe polecenia:

| Polecenie | Opis |
|-----------|------|
| = | Zwraca bieżący numer wiersza
| a | Dodaje tekst po bieżącym wierszu
| d | Usuwa bieżący wiersz
| i | Wstawia wiersz na początku bieżącego wiersza
| p | Wypisuje bieżący wiersz. Domyślnie sed wypisuje każdy wiersz i edytuje tylko wiersze pasujące do określonego adresu w pliku. Domyślne zachowanie można przesłonić, korzystając z opcji -n
| q | Zamyka program sed bez przetwarzania żadnego kolejnego wiersza. Jeśli nie wpiszemy opcji -n, wyświetli bieżący wiersz
| Q | Zamyka program sed bez przetwarzania żadnego kolejnego wiersza
| s/regexp/zastąpienie/ | Zastępuje każdy fragment pasujący do wzorca regexp łańcuchem zastąpienie. Zastąpienie może zawierać znak specjalny &, który reprezentuje tekst pasujący do wzorca. Ponadto zastąpienie może zawierać sekwencje od \1 do \9, które odpowiadają kolejnym podwzorcom wzorca regexp.
| y/zestaw1/zestaw2/ | Przeprowadza transliterację, przekształcając znaki z zestawu zestaw1 na odpowiadające im znaki z zestawu zestaw2. W przeciwieństwie do programu tr, sed wymaga tej samej długości obydwu zestawów

```
([0-9]{2})/([0-9]{2})/([0-9]{4})$
  miesiąc/dzień miesiąca/rok

zastąpienie odwołania wsteczne: \3-\1-\2

sed 's/\([0-9]\{2\}\)\/\([0-9]\{2\}\)/\([0-9]\{4\}\)$/\3-\1-\2/' file.txt
```

Flaga `-g` instruuje `sed`, aby wyszukiwanie i zastępowanie odbywało się w całym wierszu, a nie tylko na pierwszym wystąpieniu, co jest zachowaniem domyślnym.
```
└─ $ ▶echo "aaabbbccc" | sed 's/b/B/'
aaaBbbccc

└─ $ ▶echo "aaabbbccc" | sed 's/b/B/g'
aaaBBBccc
```

Można też utworzyć bardziej złożone polecenia, umieścić je w pliku skryptu i wykonać program z opcją `-f`
`sed -f skrypt.sed plik.txt`  
___
## aspell
`aspell` interaktywny program do sprawdzania pisowni.
`aspell check plik_tekstowy`
```
└─ $ ▶cat > foo2.txt
Szybki brazowy lis przeskoczył nad leniwum psem.

└─ $ ▶aspell -l pl check foo2.txt 
```
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
