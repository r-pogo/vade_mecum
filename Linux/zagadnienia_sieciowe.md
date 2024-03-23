# Zagadnienia sieciowe

| Command | Action |
|---------|--------|
| ping | wysyła komunikat ICMP ECHO_REQUEST do hostów sieciowych
| traceroute | wypisuje trasy pakietów do hosta sieciowego
| ip | wyświetla informacje o trasowaniu, urządzeniach, trasowaniu zasad oraz o tunelach i umożliwia manipulowanie nimi
| netstat | wypisuje połączenia sieciowe, tablice trasowania statystyki interfejsu, połączenia maskaradowe oraz udziały w połączeniach multitaskowych
| ftp | program do przesyłania plików przez internet
| wget | nieinteraktywny program do pobierania danych z sieci
| ssh | klient SSH protokołu OpenSSH (program do logowania zdalnego
___
## Monitorowanie sieci
### ping
`ping` wysyła do określonego hosta specjalny pakiet sieciowy, zwanym ICMP ECHO_REQUEST.
Większość urządzeń sieciowych otrzymując ten pakiet wyśle odpowiedz, która pozwala na weryfikację połączenia sieciowego.  
```
└─ $ ▶ping linuxcommand.org
PING linuxcommand.org (216.105.38.11) 56(84) bytes of data.
64 bytes from secureprojects.sourceforge.net (216.105.38.11): icmp_seq=1 ttl=41 time=189 ms
64 bytes from secureprojects.sourceforge.net (216.105.38.11): icmp_seq=2 ttl=41 time=185 ms
64 bytes from secureprojects.sourceforge.net (216.105.38.11): icmp_seq=3 ttl=41 time=187 ms
...
```
`ping` wypisuje statystyki wydajności. Poprawnie działająca sieć charakteryzuje się zerową stratą pakietów.  
Pomyślne wyknoanie polecenia oznacza, że elementy sieci (karty sieciowe, okablowanie, trasy i bramy) znajdują się w dobrej kondycji.  

### traceroute
`traceroute` (w niektórych systemach wykorzystuje się tracepath) wyświetla listę wszystkich przeskoków wykonywanych przez ruch sieciowy od lokalnego systemu  
do określonego hosta.  
```
└─ $ ▶traceroute slashdot.org
traceroute to slashdot.org (104.18.36.64), 30 hops max, 60 byte packets
 1  DESKTOP-3T3MNOS.mshome.net (172.17.49.1)  1.069 ms  0.939 ms  0.613 ms
 2  arrisatom (192.168.0.1)  3.600 ms  6.953 ms  6.828 ms
 3  pl-poz02a-rt1.aorta.net (84.116.254.96)  21.757 ms  23.340 ms  23.324 ms
 4  * * *
 5  pl-waw26b-rc1-ae-63-0.aorta.net (84.116.252.41)  29.257 ms  29.192 ms  30.670 ms
 6  pl-waw02a-ri1-ae-0-0.aorta.net (84.116.138.94)  26.929 ms  23.671 ms  25.644 ms
 7  * * *
 8  104.18.36.64 (104.18.36.64)  25.024 ms  33.398 ms  28.268 ms
```
W treści wyniku widać, że połączenie z naszego systemu do adresu slashdot.org wymaga odwiedzenie 8 routerów.  
Jeśli routery udostępniają informacje identyfikacyjne, możemy zobaczyć nazwy hostów, adresy IP i dane wydajnościowe, które obejmują czas podróży w obie strony  
trzech próbek z systemu lokalnego do routera.  
Jeśli rotery nie udostępniają informacji indetyfikacyjnych (z powodu konfiguracji routera, zatoru sieci, zapór sieciowych itp.)  
na końcu wiersza znajdziemy gwiazdkę jak w wierszu reprezentującym 4 i 7 przeskok.  
W przypadku blokady informacji o trasowaniu czasem można sobie poradzić, dodając opcję -T lub -I do poleceniea `traceroute`.  

### ip
`ip` zastępuje `ipconfig`, za pomocą tego polecenia można przeanalizować interfejsy sieciowe i tablicę trasowania w systemie.

Podczas przeprowadzania zwykłej diagnostyki sieci ważne jest sprawdzenie obecności słowa `UP`~na początku czwartego wiersza  
każdego interfejsu, które informuje, że interfejs sieciowy jest włączony, oraz o obecności poprawnego adresu IP w polu `inet addr` w drugim wierszu.  
W przypadku systemów korzystających z protokołu DHCP poprawny adres IP w tym polu oznacza, że DHCP działa.  

### netstat
`netstat` służy do sprawdzenia różnych ustawień sieciowych i statystyk.  
Opcja `-ie` pozwala na sprawdzenie interfejsów sieciowych w naszym systemie
Korzystając z opcji `-r`, możemy wyświetlić tablicę trasowania sieci jądra. Tablica ta informuje o konfiguracji przesyłania pakietów z sieci do sieci.
___
## Przenoszenie plików przez sieć
### ftp
`ftp` nawę otrzymał od wykorzystywanego protokołu - File Transfer Protocol.
FTP nie jest bezpieczny! Wysyła nazwy kont i hasła w postaci otwartego tekstu, nie są zaszyfrowane i każdy nasłuchujący w sieci może je przechwycić.  
Dlatego niemal zawsze korzystanie z protokołu FTP w internecie odbywa się poprzez anonimowe serwery FTP.  
Serwer anonimowy pozwala każdemu na zalogowanie się za pomocą nazwy użytkownika `anonimowy` i dowolnego hasła.  

### lftp
`lftp`  lepsza wersja `ftp`

### wget
`wget` przydatny do pobierania zawartości z sieci WWW i serwerów FTP. Ma liczne opcje na pobieranie rekursywne, pobieranie plików  
w tle
```
└─ $ ▶wget http://linuxcommand.org/index.php
--2024-03-23 13:56:09--  http://linuxcommand.org/index.php
Resolving linuxcommand.org (linuxcommand.org)... 216.105.38.11
Connecting to linuxcommand.org (linuxcommand.org)|216.105.38.11|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3929 (3.8K) [text/html]
Saving to: ‘index.php’

index.php                                                  100%[=======================================================================================================================================>]   3.84K  --.-KB/s    in 0s

2024-03-23 13:56:09 (83.5 MB/s) - ‘index.php’ saved [3929/3929]

```
___
## Bezpieczna komunikacja z hostami zdalnymi
## ssh
`ssh` protokół secure shell rozwiązuje dwa podstawowe problemy bezpiecznej komunikacji z hostem zdalnym:
1. Uwierzytelnienia hosta zdalnego, czyli sprawdza, czy jest tym, za którego się podaje, zapobiegając atakom `man-in -the-middle`  
2. Szyfruje całą komunikację pomiędzy hostami lokalnymi a zdalnymi.  

SSH składa się z dwóch części. Serwer SSH działa na hoscie zdalnym, nasłuchując połączeń, domyślnie przychodzących przez `port 22`  
natomiast klient SSH jest używany w systemie lokalnym do komunikacji z serverem zdalnym.  
Większość dystrybucji zawiera implementację SSH zwaną OpenSSH.  
Aby włączyć w systemie możliwość otrzymywania połączeń zdalnych, musi być na nim zainstalowany, skonfigurowany i uruchomiony pakiet `OpenSSH-server`.  
Ponadto system, jeśli jest uruchomiony lub znajduję się za zaporą sieciową musi umożliwiać przyjmowanie połączeń sieciowych TCP poprzez port 22.  

Aby połączyć się ze zdalnym hostem o nazwie np: `remote-sys`
`$ ▶ ssh reomte-sys`  

Gdy spróbujemy się połączyć po raz pierwszy, pojawi się komunikat informujący, że nie można było stwierdzić autentyczności hosta zdalnego.
Przyczyną jest to, że program klienta nigdy wcześniej nie miał do czynienia z tym hostem zdalnym. 
Aby zaakceptować dane dostępowe hosta zdalnego, należy wpisać `yes`, gdy pojawi się odpowiednie pytanie.  
Po ustanowieniu połączenia użytkownik zostanie poproszony o hasło.
```
▶ssh bandit.labs.overthewire.org
The authenticity of host 'bandit.labs.overthewire.org (51.20.13.48)' can't be established.
ECDSA key fingerprint is SHA256:IJ7FrX0mKSSHTJ63ezxjqtnOE0Hg116Aq+v5mN0+HdE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
Po wpisaniu poprawnego hasła zobaczy, znak zachęty powłoki systemu zdalnego.  
Sesja powłoki zdalnej będzie kontynuować działanie, dopóki użytkownik nie wpisze `exit`, w ten sposób zostanie przywrócona sesja powłoki lokalnej.  
Istnieje również możliwość połączenia się z systemem zdalnym z wykorzystaniem innej nazwy urzytkownika:
``$ ▶ ssh InnaNazwa@reomte-sys
ssh bandit1@bandit.labs.overthewire.org -p 2220
``

SSH sprawdza autentyczność hosta zdalnego. Jeśli uwierzytelnienie hosta zdalnego się nie powiedzie, na ekranie pojawi się komunikat.  
Mól to być atak man in the middle ale raczej coś się stało z systemem zdalnym, na przykład system operacyjny lub serwer SSH został ponownie zainstalowany.  
Po stroni klienta w takim przypadku można usunąć zdezaktualizowany klucz z pliku `~/.ssh.known_hosts`
```
 $ ▶ssh bandit.labs.overthewire.org
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The ECDSA host key for bandit.labs.overthewire.org has changed,
and the key for the corresponding IP address 51.20.13.48
is unknown. This could either mean that
DNS SPOOFING is happening or the IP address for the host
and its host key have changed at the same time.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:IJ7FrX0mKSSHTJ63ezxjqtnOE0Hg116Aq+v5mN0+HdE.
Please contact your system administrator.
Add correct host key in /home/elski/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/elski/.ssh/known_hosts:2
  remove with:
  ssh-keygen -f "/home/elski/.ssh/known_hosts" -R "bandit.labs.overthewire.org"
ECDSA host key for bandit.labs.overthewire.org has changed and you have requested strict checking.
Host key verification failed.
```

Pracując na systemie zdalnym możemy przekierować wyniki do pliku w systemie lokalnym
`$ ▶ ssh remote-sys 'ls *' > dirlist.txt`

### scp i sftp
Pakiet OpenSSH zawiera także dwa programy wykorzystujące zaszyfrowany tunel SSH przeznaczone do kopiowania plików poprzez sieć.  
`scp` - secure copy działa podobnie jak `cp`. Ścieżka pliku źródłowego lub docelowego może być poprzedzona nazwą hosta zdalnego, po której następuje dwukropek.
Jeśli na przykład chcemy skopiować dokument z systemu zdalnego o nazwie `remote-sys` do bieżącego katalogu roboczego w systemie lokalnym:
`scp remote-sys:document.txt .`  
Na początku nawy hosta zdalnego możemy umieścić nazwę użytkownika, jeśli docelowa nazwa knota na hoście zdalnym nie pasuje do nazwy użytkowniak w systemi lokalnym:
`scp KtoSInny@remote-sys:document.txt .`  

`sftp` to bezpieczna wersja `ftp`. Nie wymaga obecności serwera FTP na hoście zdalnym, wymaga tylko serwera SSH.  
Dowolna maszyna zdalna, która może się połączyć z klientem SSH, może również zostać wykorzystana jak serwer FTP.  
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
