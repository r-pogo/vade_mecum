# Archiwizacja i kopie zapasowe

| Command | Action |
|---------|--------|
| gzip | kompresuje i wyodrębnia pliki
| bzip2 | kompresuje pliki poprzez sortowanie blokowe
| tar | narzędzie do archiwizacji taśmowej
| zip | pakuje i kompresuje pliki
| rsync | synchronizuje zdalne pliki i katalogi

## Kompresowanie plików

### gzip/gunzip

`gzip` służy do kompresowania jednego lub wielu plików. Gdy zostanie
uruchomiony, zastępuje oryginalny plik jego skompresowaną wersją.  
`gunzip` służy do przywracania skompresowanych plików do oryginalnej postaci.

```
$ ▶ls -l foo*
-rwxrwxrwx 1 elski elski 29 Mar 26 20:28 foo.txt
$ ▶gzip foo*
$ ▶ls -l foo*
-rwxrwxrwx 1 elski elski 57 Mar 26 20:28 foo.txt.gz
$ ▶gunzip foo.txt.gz # rozszerzenie jest gz jest opcjonalne
$ ▶ls -l foo*
-rwxrwxrwx 1 elski elski 29 Mar 26 20:28 foo.txt
```

`gzip` przyjmuje wiele opcji zobacz `man gzip`

`gzip` można także użyć w ciekawy sposób z wykorzystaniem standardowych
strumieni wejścia i wyjścia:

```
$ ▶ ls -l /etc | gzip > foo.txt.gz
```

To polecenie tworzy skompresowany plik z listą zawartości katalogu.
NB: `gunzip` zakłada, że nazwy plików kończą się z rozszerzeniem .gz, dlatego
nie ma konieczności dodawania tego rozszerzenia, chyba że podana nazwa jest w  
konflikcie z istniejącym z dekompresowanym plikiem.

Jeśli zamierzamy tylko sprawdzić zawartość skompresowanego pliku tekstowego:
`$ ▶ gunzip -c foo.txt | less`

Można też wykorzystać z `zcat` albo `zless` działają jak program `gunzip` z
opcją `-c`.  
`$ ▶ zcat foo.txt.gz | less`

### bzip2/bunzip2

`bzip2` działa podobnie jak `gzip` ale korzysta z innego algorytmu.  
Pozwala osiągnąć wyższy poziom kompresji kosztem szybkości. Rozszerzenie
to `.bz2`

```
$ ▶ls -l /etc > foo.txt
$ ▶ls -l foo.txt
-rwxrwxrwx 1 elski elski 13084 Mar 26 20:45 foo.txt
$ ▶bzip2 foo.txt
$ ▶ls -l foo.txt.bz2
-rwxrwxrwx 1 elski elski 2189 Mar 26 20:45 foo.txt.bz2
$ ▶bunzip2 foo.txt.bz2
```

W skład programu `bzip2` wchodzi również program `bzip2recover`. Który służy do
odzyskiwania uszkodzonych plików `.bz2`
___

## Archiwizacja plików

Archiwizacja polega na zebraniu wielu plików i spakowaniu ich w jeden duży
plik.

### tar

`tar` tape archive, rozszerzenie `.tar` lub `.tgz`.
`tar tryb[opcje] ścieżka...`
Tryb to jeden z trybów operacyjnych, zobacz `man tar`
Tu przykładowe

| Tryb | Opis |
|------|---|
| c | Tworzy archiwum na podstawie listy plików i lub katalogów
| x | Rozpakowuje archiwum
| r | Dodaje określone ścieżki na końcu archiwum
| t | Wypisuje zawartość archiwum

```
$ ▶ mkdir -p linuxNauka/dir-{00{1..9},0{10..99},100}
$ ▶ touch linuxNauka/dir-{00{1..99}, 0{10..99}, 100}/file-{A..Z}
$ ▶ tar cf linuxNauka.tar linuxNauka
```

To polecenie tworzy archiwum `tar` o nazwie `linuxNauka.tar`, zawierające całą
hierarchię katalogu linuxNauka.  
Możemy połączyć tryb z opcją `f`, służącą do określania nazwy `tar` i możemy
pominąć znak kreski na początku.  
Tryb musi być zawsze umieszczony na początku, przed jakąkolwiek opcją.

Aby wypisać zawartość archiwum możemy wykonać polecenie:
`$ ▶ tar tf linuxNauka.tar`  
Po dodaniu opcji `v` uzyskamy bardziej szczegółową listę:  
`$ ▶ tar tvf linuxNauka.tar`

Wyodrębnienie archiwum do innego katalogu:

````
$ ▶ mkdir foo
$ ▶ cd foo
$ ▶tar xf ../linuxNauka.tar
````

Uwaga, jeśli nie działamy z uprawnieniami użytkownika uprzywilejowanego, plik i
kategorie wyodrębnione z archiwów będą należeć do  
użytkownika wyodrębniającego archiwum, a nie do oryginalnego właściciela.  
Domyślnie stosowane są ścieżki względne, a nie bezwzględne. `tar` tworzy je
podczas tworzenia archiwum, usuwając po prostu ukośnik, znajdujący się na
początku nazwy ścieżki. Aby to zademonstrować, ponownie utworzymy nasze
archiwum, tym razem podając ścieżkę bezwzględną:

```
$ ▶ cd
$ ▶ tar cf linuxNauka2.tar ~/linuxNauka
# po naciśnieću klawisza Enter katalog ~/linuxNauka zostanie zinterpretowany jako /home/me/linuxNauka
$ ▶ cd foo
$ ▶ tar xf ../linuxNauka2.tar
```

Można wyodrębnić zarówno jeden plik:
`tar xf archiwum.tar ścieżka`

```
$ ▶ cd foo
$ ▶ tar xf ../linuxNauka2.tar --wildcards 'home/me/linuxNauka/dir-*/file-A'
```

Na koniec polecenia dodajemy ścieżkę, by wyodrębnić określony plik. Można też
dodać kilka ścieżek. Musi to być pełna ścieżka względna.  
Przy określaniu ścieżek zwykle nie możemy zastosować wieloznaczników, ale
wersja GNU pozwala na ich stosowanie z wykorzystaniem opcji `--wildcards`.

`tar` jest dobre do tworzenia archiwów w połączeniu z poleceniem `find`:

```
$ ▶ find linuxNauka -name 'file-A' -exec tar rf linuxNauka.tar '{}' '+'
```

Używamy polecenia `find`, aby dopasować wszystkie pliki o nazwie `file-A`
znajdujące się w katalogu linuxNauka.  
Następnie, korzystając z akcji `-exec`, uruchamiamy polecenie `tar` w trybie
dołączania `r`, aby dodać pasujące pliki do archiwum linuxNauka.tar.  
`tar` może też korzystać ze standardowych strumieni wejścia i wyjścia.
`$ ▶ find linuxNauka -name 'file-A' | tar cf - --files-from=- | gzip > linuxNauka.tgz`

W tym przykładzie program `find` tworzy listę pasujących plików i przekazuje je
do polecenia `tar`  
Jeśli nazwa pliku ma postać `-`, oznacza to, że zgodnie z potrzebą zostanie
wykorzystany standardowy strumień wejścia lub wyjścia.  
Opcja `--files-from`, skrócona forma to `-T`, sprawia, że `tar` odczytuję listę
ścieżek z pliku, a nie z wiersza poleceń.  
Wreszcie archiwum wykonane przez `tar` jest przekazywane do programu `gzip` w
celu utworzenia skompresowanego archiwum linuxNauka.tgz
Rozszerzenie `.tgz` jest konwencjonalnym rozszerzeniem nadawanym skompresowanym
plikom `tar`. Czasami `.tar.gz`.  
Program `tar` wspiera zarówno kompresję `gzip` i `bzip2` z wykorzystaniem
odpowiednio opcji `z` i `j`.

Transfer sieciowy plików między systemami, np. mamy dwie maszyny działające pod kontrolą systemu uniksowego  
wyposażonego w programy `tar` i `ssh`. W tym scenariuszu można przenieść katalog z systemu zdalnego (nazwanego w przykładzie remote-sys)  
na system lokalny:  
```
$ ▶ mkdir remote-stuff
$ ▶ cd remote-stuff
$ ▶ ssh remote-sys 'tar cf - Documents' | tar xf - me@remote-sys' s password:

```
W tym przykładzie został skopiowany katalog o nazwie Documents z systemu zdalnego remote-sys do podkatalogu znajdującego się w katalogu remote-stuff
w systemie lokalnym. Najpierw został uruchomiony program `tar` w systemie zdalnym korzystając z `ssh`.  
Możemy wykorzystać program `tar` do utworzenia archiwum (tryb `c`) a następnie przesłać je do standardowego strumienia wyjścia zamiast do pliku (opcja `f` z argumentem w postaci kreski).  
W ten sposób przenosimy archiwum przez zaszyfrowany tunel, utworzony przez `ssh`, do systemu lokalnego. W systemie lokalnym uruchamiamy program `tar` i rozpakowujemy
archiwum (w trybie `x`) przekazane ze standardowego strumienia wejścia (ponownie opcja `f` z argumentem w postaci kreski).  

### zip
`zip` służy zarówno do kompresji, jak i do archiwizacji.
`zip opcje plikzip plik...`

`$ ▶ zip -r naukaLinux.zip naukaLinux`
`-r` to rekursja inaczej zostanie uwzględniony tylko katalog linuxNauka bez jego zawartości.  
`zip` wyświetla komunikaty świadczące o statusie każdego dodanego pliku do archiwum, korzystając z jednej lub dwóch metod   
przechowywania:
`store` bez kompresji
`deflate` z kompresją.
Wartość liczbowa, wyświetlana po metodzie przechowywania, oznacza poziom osiągniętej kompresji.  
Wyodrębnianie zawartości pliku `zip`:
`$ ▶ unzip ../linuxNauka.zip`
Korzystając z programu `zip`, w przeciwieństwie do `tar`, jeśli podamy istniejący plik, zostanie on uaktualniony, a nie zastąpiony  
Istniejące archiwum zostanie zachowane, nowe pliki zostaną dodane, a istniejące zastąpione.
Korzystając z opcji `-l, unzip -l` wypiszemy zawartości i je wyodrębnimy.  
Do programu `zip` możemy przekazać listę nazw plików, korzystając z opcji `-@`:
`$ ▶ find linuxNauka -name "file-A" | zip -@ fila-A.zip`  
Program `unzip` nie akceptuje standardowego strumienia wejścia.  

`$ ▶ls -l /etc/ | zip ls-etc.zip -`  
Tu do programu `zip` został przekazany wynik działania programu `ls`. Podobnie jak `tar`, `zip` interpretuję kreskę na końcu polecenia  
jako "użyj standardowego strumienia wejścia jako pliku wejściowego".  
Program `unzip` pozwala na przesłanie wyniku do standardowego strumienia wyjścia po wpisaniu opcji `-p` oznaczającej potoki:  
`$ ▶ unzip -p ls-etc.zip | less`  
___
## Synchronizacja plików i katalogów
`rsync` jest preferowanym narzędziem do tej pracy.
`rsync opcje żródło cel`
Gdzie źródło i cel to jedna z poniższych możliwości:
- lokalny plik lub katalog
- zdalny plik lub katalog w postaci `[user@]host:path`
- zdalny serwer rsync określony z pomocą URI w postaci `rsync://[user@]host[:port]/path`  
Albo źródło, albo cel musi być plikiem lokalnym, nie jest wspierane kopiowanie "zdalny do zdalnego".  
Przykład:
`$ ▶rsync -av naukaLinux foo`
opcja `-a` włącza rekursję i zachowuje atrybuty plików, opcja `-v` rozszerzone informacje na wyjściu, aby
utworzyć lustro katalogu linuxNauka w katalogu foo.  

Przykład z `/`: mamy dwa katalogi source i destination  
`$ ▶ rsync source / destination`
Jeśli dodamy `/` na końcu nazwy katalogu source, polecenie `rsync` skopiuje tylko zawartość katalogu source,
a nie sam katalog.

`rsync` może być używany do kopiowania plików przez sieć.
Np:
`$ ▶ sudo rsync -av --delete --rsh=sh /etc /home /usr /local remote-sys:/backup`
`--rsh=ssh` `rsync` skorzysta z programu `ssh` jak z powłoki zdalnej.  
`remote-sys` do ścieżki docelowej trzeba dodać przedrostek określający nazwę hosta zdalnego.  

Drugi sposób zastosowania `rsync` do synchronizacji plików poprzez sieć polega na użyciu `serwera rsync`.  
Program `rsync` można skonfigurować tak, aby działał jako demon i nasłuchiwał przychodzących żądań synchronizacji.
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019







