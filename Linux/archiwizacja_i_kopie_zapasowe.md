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
`gzip` służy do kompresowania jednego lub wielu plików. Gdy zostanie uruchomiony, zastępuje oryginalny plik jego skompresowaną wersją.  
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

`gzip` można także użyć w ciekawy sposób z wykorzystaniem standardowych strumieni wejścia i wyjścia:
```
$ ▶ ls -l /etc | gzip > foo.txt.gz
```
To polecenie tworzy skompresowany plik z listą zawartości katalogu.
NB: `gunzip` zakłada, że nazwy plików kończą się z rozszerzeniem .gz, dlatego nie ma koniecznści dodawania tego rozszerzenia,   
chyna że podana nazwa jest w konflikcie z istniejącym zdekompresowanym plikiem.  

Jeśli zamierzamy tylko sprawdzić zawartość skompresowanego pliku tekstowego:
`$ ▶ gunzip -c foo.txt | less`

Można też wykorzystać z `zcat` albo `zless` działają jak program `gunzip` z opcją `-c`.  
`$ ▶ zcat foo.txt.gz | less`

### bzip2/bunzip2
`bzip2` działa podobnie jak `gzip` ale korzysta z innego algorytmu.  
Pozwala osiągnąć wyższy poziom kompresji kosztem szybkości. Rozszerzenie to `.bz2`
```
$ ▶ls -l /etc > foo.txt
$ ▶ls -l foo.txt
-rwxrwxrwx 1 elski elski 13084 Mar 26 20:45 foo.txt
$ ▶bzip2 foo.txt
$ ▶ls -l foo.txt.bz2
-rwxrwxrwx 1 elski elski 2189 Mar 26 20:45 foo.txt.bz2
$ ▶bunzip2 foo.txt.bz2
```
W skład programu `bzip2` wchodzi również program `bzip2recover`. który służy do odzyskiwania uszkodzonych plików `.bz2`
___
##Archiwizacja plików
Archiwizacja polega na zebraniu wielu plików i spakowaniu ich w jeden duży plik.
### tar
`tar` tape archive, rozszerzenie `.tar` lub `.tgz`.
`tar tryb[opcje] ścieżka...`
Tryb to jeden z trybów operacyjnych, zobacz `man tar`
```
$ ▶ mkdir -p linuxNauka/dir-{00{1..9},0{10..99},100}
$ ▶ touch linuxNauka/dir-{00{1..99}, 0{10..99}, 100}/file-{A..Z}
$ ▶ tar cf linuxNauka.tar linuxNauka
```
To polecenie tworzy archiwum `tar` o nazwie `linuxNauka.tar`, zawierające całą hierarchię katalogu linuxNauka.  
Możemy połączyć tryb z opcją `f`, służącą do określania nazwy `tar` imożemy pominąć znak kreski na  
początku. Tryb musi być zawsze umieszczony na początku, przed jakąkolwiek opcją.  

Aby wypisać zawartość archiwum możemy wykonać polecenie:
`$ ▶  tar tf linuxNauka.tar`  
Po dodaniu opcji `v` uzyskamy bardziej szczegółową listę:  
`$ ▶ tar tvf linuxNauka.tar`