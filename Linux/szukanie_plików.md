# Szukanie plików

| Command | Action |
|---------|--------|
| locate | wyszukuje pliki na podstawie nazwy
| find | szuka plików w hierarchii katalogów
| fzf | It's an interactive Unix filter for command-line that can be used with any list; files, command history, processes, hostnames, bookmarks, git commits, etc. https://github.com/junegunn/fzf

## locate
`locate` wykonuje szybkie przeszukiwanie baz danych nazw plików, a następnie wyświetla każdą nazwę, która pasuje  
do podanego fragmentu łańcucha.

````
▶locate bin/zip

# locate przeszukuje swoją bazę danychścieżek iwyświetla każdą, która zawiera łańcych bin/zip.
/mnt/c/Program Files/Git/mingw64/bin/zipcmp.exe
/mnt/c/Program Files/Git/mingw64/bin/zipmerge.exe
/mnt/c/Program Files/Git/mingw64/bin/ziptool.exe
/mnt/c/Program Files/Git/usr/bin/zipgrep
/mnt/c/Program Files/Git/usr/bin/zipinfo.exe
/mnt/c/Program Files/Java/jre1.8.0_281/bin/zip.dll
...
````
Oczywiście `locate` można łączyć z innymi narzędziami:
```
▶locate zip | grep bin

/usr/bin/bunzip2
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/gpg-zip
/usr/bin/gunzip
/usr/bin/gzip
/usr/bin/preunzip
/usr/bin/prezip
/usr/bin/prezip-bin
/usr/bin/zipdetails
/usr/lib/klibc/bin/gunzip
/usr/lib/klibc/bin/gzip
/usr/share/man/man1/prezip-bin.1.gz
....
````
`locate` posiada swoje warianty takie jak `slocate` czy `mlocate`
___
## find
`find` program `locate` wyszukuje pliki tylko na podstawie ich nazwy. Program `find` przeszukuje podany katalog  
i jego podkatalogi w poszukiwaniu plików na podstawie różnych atrybutów.  
W najprostszym przypadku do programu `find` przekazujemy nazwę lub kilka nazw katalogów, które chcemy przeszukać:
```
└─ $ ▶find ~ | wc -l
55989
```
`find` identyfikuje pliki, które spełniają określone kryteria, program wykorzystuje do tego celu `testy`,`akcje` i `opcje`  
### Testy
Przypuśćmy, że chcemy wyświetlić listę albo katalogów, albo tylko plików.
Skorzystamy do tego z testu:
`-type d` ogranicza wyszukiwanie do katalogów
`-type f` ogranicza wyszukiwanie do plików

```
└─ $ ▶find ~ -type d | wc -l
10353

└─ $ ▶find ~ -type f | wc -l
45622
```
Popularne testy typów plików wspierane przez `find`

| Typ plików | Opis |
|---------|--------|
| b | Blokowy plik specjalny urządzenia
| c | Znakowy plik specjalny urządzenia
| d | Katalog
| f | Zwykły plik
| l | Dowiązanie symboliczne

Możemy też wyszukiwać na podstawie rozmiaru pliku `-size` oraz jego nazwy `-name`.
```
└─ $ ▶find ~ -type f -name "*.JPG" -size +1M | wc -l
0
# Plus na początku +1M oznacza że szukamy pliów większych niż podana liczba.
# Minus to mniejsza a brak to oznacza dokładnie pasuje do wartości
```

| Znak | Jednostka |
|---------|--------|
| b | Bloki 512-bajtowe (wartość domyślna, jeśli nie podano wartości)
| c | Bajty
| w | Słowa 2-bajtowe
| k | Kilobajty (jednostki 1024-bajtowe)
| M | Megabajty (jednostki 1048576-bajtowe)
| G | Gigabajty (jednostki 1073741824-bajtowe)

`find` wspiera ogromną liczbę różnych testów, pełna lista w podręczniku `man`

### Operatory
Operatory służą do opisu logicznych relacji między testami.

Przykład: Czy wszystkie pliki i podkatalogi w katalogu posiadają bezpieczne uprawnienia?
Trzeba wyszukać wszystkie pliki o uprawnieniach innych niż 0600 oraz katalogi o uprawnieniach innych niż 0700.  
`▶find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)`

| Operator | Opis |
|---------|--------|
| -and | Sprawdza czy testy po obu stronach operatora są prawdą. Może być zapisany jako `-a`. To domyślny operator.
| -or | Sprawdza czy testy po jednej ze stron operatora są prawdą. Może być zapisany jako `-o`
| -not | Sprawdza czy test za operatorem jest fałszem. Może być zapisany jako `!`
| () | Grupuje testy i operatory w celu utworzenia większych wyrażeń. Służy do kontrolowania pierwszeństwa wyznaczania operacji logicznych.  Znaki nawiasów mają specjalne znaczenie dla powłoki, dlatego powinniśmy je zacytować np. za pomocą odwróconego ukośnika \

`wyrażenie1 -operator wyrażenie2`
We wszystkich przypadkach `wyrażenie1` zostanie wykonane, natomiast to czy `wyrażenie2` zostanie wykonane, determinuje operator:  

| Wynik wyrażenia1 | Operator | wyrażenia2 jest... |
|-----------------|----------|-------------------- |
| Prawda | -and | Zawsze jest wykonywane |
| Fałsz | -and | Nigdy nie jest wykonywane |
| Prawda | -or | Nigdy nie jest wykonywane |
| Fałsz | -or | Zawsze jest wykonywane |

### Akcje
`find` pozwala na wykonywanie akcji na wynikach wyszukiwania.  
Do dyspozycji mamy zestaw predefiniowanych akcji oraz kilka sposobów na stosowanie akcji zdefiniowanych przez użytkownika.  

Predefiniowane akcje programu `find`

| Akcja | Opis |
|---------|--------|
| -delete | Usuwa pliki pasujący do bieżących kryteriów wyszukiwania
| -ls | Wykonuje odpowiednik polecenia `ls -dils` na pliku pasujący do bieżących kryteriów wyszukiwania. Wynik jest wysyłany do standardowego strumienia wyjścia
| -print | Wyświetla pełną ścieżkę psującego pliku do standardowego wyjścia strumienia. Domyślna akcja
| -quit | Wyjście po wykonaniu dopasowania

Więcej akcji w podręczniku `man`
Przykład:
`find ~ -type f -name '*.bak -delete`  
Uwaga na `-delete` warto przetestować tę akcję używając `-print`  
`find ~ -type f -name '*.bak -print`  
Pamiętajmy, że domyślnie pomiędzy każdym testem i akcją istnieje relacja `-and` więc kolejność ma znaczenie!!!

Oprócz predefinowanych akcji możemy też wywołać dowolne polecenia. Tradycyjny sposób polega na wykorzystywaniu akcji `-exec` `-excec polecenie {} ;`  
gdzie `polecenie` jest nazwą polecania a `{}` jest symboliczną reprezentacją nazwy bieżącego obiektu, na którym polecenie pracuje trochę jak taki for loop gdzie {} przedstawia każdy item, który się pojawia w pętli a `;` wymaganym separatorem, sygnalizującym koniec polecenia.  

Przykład użycia `-exec` do wykonania zadania opisanej wcześniej akcji `-delete`: 
`-exec rm '{}' ';'`  
Również tym razem, ponieważ nawiasy i średniki mają specjalne znaczenie dla powłoki, należy je umieścić w cudzysłowach lub poprzedzić lewym ukośnikiem.  
Możemy też akcję, zdefiniowaną przez użytkownika, wykonać w sposób interaktywny. Gdy użyjemy akcji `-ok` zamiast `-exec`,  
użytkownik zostanie poproszony o potwierdzenie przed wykonaniem każdego polecenia.

```
└─ $ ▶find . -type f -name 'a*' -ok ls -l '{}' ';'
< ls ... ./.git/hooks/applypatch-msg.sample > ? y
-rwxrwxrwx 1 elski elski 478 Oct  5  2022 ./.git/hooks/applypatch-msg.sample
< ls ... ./.git/objects/16/a60e35179416c13b7fd98924c84d2201fb7d92 > ? y
-r-xr-xr-x 1 elski elski 119 Sep 19  2023 ./.git/objects/16/a60e35179416c13b7fd98924c84d2201fb7d92
< ls ... ./.git/objects/19/ac9ad80d24d9860db9b314685c9e92b5d78b14 > ? y
-r-xr-xr-x 1 elski elski 151 Aug 12  2023 ./.git/objects/19/ac9ad80d24d9860db9b314685c9e92b5d78b14
< ls ... ./.git/objects/1f/ac983d3052c47dc6d0a605332c702d7e871282 > ? n
< ls ... ./.git/objects/27/a52fcae092d6d14fd1a3d5f02bbd17a75171f3 > ? n
< ls ... ./.git/objects/35/a38b7755b1866e08aa141baa0da1f137a4d799 > ? y
-r-xr-xr-x 1 elski elski 1682 Sep 19  2023 ./.git/objects/35/a38b7755b1866e08aa141baa0da1f137a4d799
...
```

Gdy korzystamy z akcji `-exec`, za każdym razem, kiedy zostanie znaleziony pasujący plik, uruchamiana jest nowa instancja  
określonego polecenia. Czasem lepiej jest połączyć wszystkie wyszukiwane elementy i uruchomić jedną instancję polecenia.  

Tak, aby polecenia zostało uruchomione tylko raz, a nie kilkakrotnie. Efekt ten może zostać osiągnięty na dwa sposoby: tradycyjny, z wykorzystaniem  
zewnętrznego polecenia `xargs`, oraz alternatywnym, z wykorzystaniem nowej funkcji samego programu `find`.  

Alternatywny:  
Zmieniając końcowy znak średnika na plus, aktywujemy funkcję polecenia `find`, łącząc wyniki wyszukiwania w listę argumentów, którą przekazujemy do pojedynczego wywołania naszego polecenia.
Tu uzyskamy te same wyniki, lecz system musi wykonać `ls` tylko raz
```
└─ $ ▶find . -type f -name 'a*' -exec ls -l '{}' +
-rwxrwxrwx 1 elski elski  478 Oct  5  2022 ./.git/hooks/applypatch-msg.sample
-r-xr-xr-x 1 elski elski  119 Sep 19  2023 ./.git/objects/16/a60e35179416c13b7fd98924c84d2201fb7d92
...
```
Taki sam wynik możemy uzyskać za pomocą polecenia `xargs` które akceptuje dane ze standardowego strumienia wyjścia  
i zamienia je na listę argumentów dla określonego polecenia. W przypadku naszego polecenia wyglądało to by tak:
`find . -type -name 'a*' -print | xargs ls -l`
Wynik polecenia `find` jest przekazywany potokiem do polecenia `xargs`, które z kolei tworzy listę argumentów dla polecenia `ls`  
a następnie je wykonuje.
Uwaga jest limit, jeśli chodzi o liczbę argumentów. Aby sprawdzić maksymalny rozmiar polecenia, należy wykonać  
polecenie `xargs` z opcją `--show-limits`.  

W przypadku dziwnych nazw plików np. mają znaki spacji i/lub nowego wiersza. Aby to obejść, polecenie `find` i `xargs`   
pozwalają na opcjonalne użycie znaku `null` jako separatora argumentów. Znak `null` jest reprezentowany w kodzie ASCII  
przez liczbę `0`. Polecenie `find` przyjmuje opcje `-print0`, która tworzy wynik z separatorami w postaci znaków `null`.  
Natomiast polecenia `xargs` przyjmuje opcję `-null`, która akceptuje dane wejściowe rozdzielone znakami `null`.  
`find ~ -iname '*.jpg' -print0 | xargs --null ls -l`  
Dzięki wykorzystaniu tej techniki mamy pewność, że wszystkie pliki, nawet te o nazwach zawierających znaki spacji, zostaną poprawnie prztworzone.  

### Opcje
Opcje służą do sterowania zakresem wyszukiwania przez polecenie `find`. Można ichużywać razem z innymi testami i akcjami przy tworzeniu wyrażeń `find`.  
Przykłady często używanych

| Opcja | Opis |
|---------|--------|
| -depth | Sprawia że `find` najpierw procesuje pliki znajdujące się w katalogu a potem sam katalog. Stosowana automatycznie z `-delete`
| -maxdepth poziomy | Określa maksymalną liczbę poziomów zgłebnienia, na których `find` będzie przeszukiwało drzewo katalogów podczas wykonywania testów i akcji
| -mindepth poziomy | Ustawia minimalną liczbę poziomów, na których `find` będzie przeszukiwał drzewo katalogów przed wykonaniem testów i akcji
| -mount | Sprawia, że polecenie `find` będzie ignorować katalogi zamontowane w innych systemach plików
| -noleaf | Sprawia, że polecenie `find` będzie optymalizować wyszukiwania na podstwie przypuszczenia, że przeszykiwany jest uniksowy system plików. Opcja ta jest niezbędna podczas skanowania systemów plików DOS (Windows) i płyt CD-ROM.
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019