# Techniki Testowania
Test techniques support the tester in test analysis (what to test) and in test design (how to test). Test 
techniques help to develop a relatively small, but sufficient, set of test cases in a systematic way. Test 
techniques also help the tester to define test conditions, identify coverage items, and identify test data 
during the test analysis and design. Further information on test techniques and their corresponding 
measures can be found in the ISO/IEC/IEEE 29119-4 standard, and in (Beizer 1990, Craig 2002, 
Copeland 2004, Koomen 2006, Jorgensen 2014, Ammann 2016, Forgács 2019). 

## Black-box test techniques (also known as specification-based techniques) 
### Equivalence Partitioning (Podział na klasy równoważności)
#### Charakterystyka
Podstawa: próbuje przezwyciężyć zasadę niemożności testowania gruntowego.  
Możliwych danych wejściowych jest nieskończenie wiele, ale oczekiwanych zachowań programu na te dane  
jest już skończona liczba.
Testowane zachowanie programu da się sprowadzić do skończonej liczby wariantów.

Technika EP polega na podzieleniu zbioru wszystkich możliwych danych wejściowych na klasy równoważności, 
czyli grupy danych, które są traktowane jako równoważne pod względem przewidywanych wyników działania programu.

Technika EP jest uniwersalna, można ją stosować w każdej sytuacji na każdym poziomie testów i w każdym typie.
Do dziedzin wejściowych, wyjściowych oraz wewnętrznych (związanych ze zmiennymi, które nie są bezpośrednio podawane na wejściu ani  
zwracane na wyjściu).
Nie musi być to koniecznie dziedzina liczbowa, może to być dowolny zbiór np. słowa (jednoliterowe czy dwuliterowe), typy OS (windows, Linux, Mac)

Technika KR indentyfikuje problemy wynikłe z błędnego przetwarzania danych.

#### Implementacja
- Każdy element dziedzin należy do dokładnie jednej klasy równoważności.
- Żadna klasa równoważności nie może być pusta

Klasy, które zawierają wartości normalne/poprawne nazywane są ```klasami prawnymi``` a
klasy zawierające wartości, które moduł lub system powinien odrzucić nazywane są ```klasami niepoprawnymi```.  

Klasy mogą podlegać dalszemu podziałowi na podklasy.

#### Maskowanie błędów
W sytuacji, w której testy mają jednocześnie pokrywać KR pochodzące z więcej niż jednego
podziału, dobrą praktyką jest, aby nie tworzyć przypadków testowych, które będą pokrywać dwie lub więcej klas niepoprawnych.
Poprawna strategia to:
1. Najpierw stwórz przypadki testowe złożone wyłącznie z danych z klas poprawnych, które pokryją wszystkie klasy poprawne.
2. Następnie dla każdej niepokrytej klasy niepoprawnej stwórz osobny przypadek testowy, w którym wystąpi dana z tej klasy, a wszystkie pozostałe  
dane pochodzić będą z klas poprawnych.

Przykład:
System wystawia ocenę studentowi na podstawie dwóch danych:
- liczny punktów za ćwiczenia (0-50)
- liczby punktów za egzamin (0-50)
Student zalicza przedmiot, jeśli suma punktów przekracza 50.

Wyróżniliśmy następujące dziedziny:
1. dziedzina zmiennej "A" = punkty za ćwiczenia:
- A1 klasa niepoprawna: n < 0
- A2 klasa poprawna: n = 0-50
- A3 klasa niepoprawna: n > 50
2. dziedzina zmiennej "B" = punkty za egzamin:
- B1 klasa niepoprawna: n < 0
- B2 klasa poprawna: n = 0-50
- B3 klasa niepoprawna: n > 50

Chcemy pokryć wszystkie klasy równoważności obu dziedzin. Każdy przypadek testowy zawiera
jakąś liczbę punktów za egzamin oraz ćwiczenia.
Najpierw pokrywamy klasy poprawne, wystarczy tylko jeden TC (test case) albo PT(przypadek testowy):
PT1: A = 25, B = 30 (pokrywa poprawną klasę A2 i poprawną klasę B2)

Aby pokryć klasy niepoprawne potrzebujemy 4 kolejnych TC, w których klasy będziemy testować indywiduualnie poniważ druga klasa musi być poprawna:
PT2: A = -8, B = 35 (pokrywa niepoprawną klasę A1; dodatkowo poprawną B2)
PT3: A = 48, B = -11 (nie ok B1; ok A2)
PT4: A = 64; B = 4 (nie ok A3; ok B2)
PT5: A = 12, B = 154 (nie ok B3; ok A2)

Dlaczego:
Załóżmy, że system weryfikuje, czy student zliczył przedmiot, poprzez następująca procedurę:
```
DANE WEJSCIOWE: punkty_za_cwiczenia, punkty_za_egzamin
JEZELI (punkty_za_cwiczenia + punkty_za_egzamin > 50) TO
    ZWROC WYNIK "Przedmiot zdany"
W PRZECIWNYM RAZIE
    ZWROC WYNIK "Przedmiot niezdany"
```
Rozważmy teraz następujący TC:
PT6: A = -26; B = 105 (ni ok A1; nie ok B3)
-26 + 105 = 77 Przedmiot zdany ---> Tym jest ```Maskowanie błędów```

#### Pokrycie
Minimalny zbiór TC zapewniających 100% pokrycie to taki, który pokrywa każdą klasę.
W przypadku wielowymiarowym (więcej niż jedna dziedzina) jest to trochę bardziej skomplikowane, 
gdyż liczba przypadków będzie zależeć od liczby kombinacji klas niepoprawnych,  
a także od ewentualnych zależności pomiędzy wartościami różnych podziałów.

Pokrycie mierzy się jako iloraz liczby klas przetestowanych przy użyciu co najmniej jednej wartości  
przez łączną liczbę zidentyfikowanych klas i jest wyrażana w %

Np.: zbiór 3 testów pokrywa 12 klas, zatem osiąga pokrycie (3/12) * 100 = 25%

#### Each Choice Coverage
Many test objects include multiple sets of partitions (e.g., test objects with more than one input 
parameter), which means that a test case will cover partitions from different sets of partitions. The 
simplest coverage criterion in the case of multiple sets of partitions is called Each Choice coverage. 
Each Choice coverage requires test cases to exercise each partition from each set of 
partitions at least once. Each Choice coverage does not take into account combinations of partitions. 

Each Choice coverage jest techniką testowania stosowaną do testowania złożonych systemów, w których  
istnieje wiele możliwych kombinacji danych wejściowych. Głównym celem tej metody jest zapewnienie, że  
każda możliwa opcja dla każdej zmiennej (czyli każdy wybór) zostanie przetestowana przynajmniej raz.  

Przykład: Rozważmy system z trzema zmiennymi wejściowymi:

A: {1, 2}  
B: {X, Y}  
C: {true, false}  

Dla Each Choice coverage stworzymy przypadki testowe tak, aby każda z możliwych wartości A, B i C 
wystąpiła przynajmniej raz, ale nie musimy sprawdzać każdej kombinacji.

Przykładowe przypadki testowe:  

(A=1, B=X, C=true)  
(A=2, B=Y, C=false)  
(A=1, B=Y, C=true)  

Tymi przypadkami testowymi zapewniamy, że każda z wartości A (1, 2), B (X, Y) i C (true, false) wystąpiła w testach.
___
### Boundary Value Analysis (Analiza wartości brzegowych AWB)
#### Charakterystyka
AWB to rozszerzenie KR. W AWB do testów wybierane są wartości leżące na brzegach klas wyróżnionych w KR.
Elementy dziedziny muszą być uszeregowane/uporządkowane od najmniejszego do największego, aby tę technikę zastosować.
Wartości brzegowe to po prostu element największy i najmniejszy dla danej klasy.

- ```Wersaj dwupunktowa```: dla każdej zidentyfikowanej wartości brzegowej wybiera się tę wartość oraz 
najbliższego sąsiada NIENALEŻĄCEGO do tej klasy.
Np. klasa z wartościami 1 do 6:
- 1 wartość brzegowa
- 0 najbliższy sąsiad spoza klasy dla wartości brzegowej 1
- 6 wartości brzegowa
- 7 najbliższy sąsiad spoza klasy dla wartości brzegowej 6

-```Wersja trójpunktowa```: dla każdej zidentyfikowanej wartości brzegowej wybiera się tę wartość oraz obu jej sąsiadów,
niezależnie do jakich klas należą.
Np. klasa z wartościami 1 do 6:
- 1 wartość brzegowa
- 0 lewy sąsiad dla wartości brzegowej 1
- 2 prawy sąsiad dla wartości brzegowej 1
- 6 wartości brzegowa
- 5 lewy sąsiad dla wartości brzegowej 6
- 7 prawy sąsiad dla wartości brzegowej 6


Przykład oby wersji:
![img.png](img/img_16.png)

#### Implementacja
1. Zidentyfikuj dziedzinę, którą chcesz poddać analizie.
2. Przeprowadź podział tej dziedziny na KR.
3. Dla każdej KR wyznacz wartości brzegowe.
4. Dla każdej wartości brzegowej wyznacz elementy do przetestowania.

Przykład: System oblicza zniżkę na bilet osobom poniżej 18 oraz powyżej 65.
1. Identyfikacja dziedziny: Analizowaną zmienną jest wiek pasażera, a więc nieujemna liczba całkowita.
Dziedzina ma więc postać 1,2,3,4....
2. Identyfikacja KR:
Mamy następujące klasy:
- K1: wiek uprawniający dla zniżki 0-17
- K2: bilet normalny 18-65
- K3: wiek uprawniający dla zniżki 66+
3. Identyfikacja wartości brzegowych:
- K1: 0 i 17
- K2: 18 i 65
- K3: 66 nie ma wartości największej
4. Identyfikacja wartości do przetestowania:
- Metoda dwupunktowa: 0,17,18,65,66
W tym przypadku mamy pewnego rodzaju symetrię między każdymi dwiema sąsiadującymi ze sobą wartościami 
brzegowymi dwóch klas. Nie ma wartości mniejszych niż 0.
- Metoda trójpunktowa: 0,1,16,17,18,19,64,65,66,67

#### Uważne wyznaczanie brzegów
W praktyce wartości globalne największe/najmniejsze istnieją, np. zakresy akceptowane przez pola danego typu.  
Warto sprawdzać nie tylko granice klasy wyznaczonych specyfikacją, ale również granice wyznaczone "architekturą"
testowanego rozwiązania.
Poza tym należy uważać na to, jak zdefiniowane są granice klas, np, w specyfikacji mamy sformułowanie, że
poruszamy się w dziedzinie liczb naturalnych, wtedy stwierdzenia "do klasy nalezą elementy nie mniejsze niż 7"
oznacza, iż 7 jest najmniejszą liczbą tej klasy. Z kolei sformułowanie "do klasy należą wartością większe od 7"
oznacza, że najmniejszą liczbą jest 8.
An alogicznie "co najwyżej 65" oznacza liczby do 65 włącznie a warunek "x < 65" oznacza, że największą wartością spełniającą tę nierówność jest 64.

#### Pokrycie
```Metoda dwupunktowa```: iloraz liczby przetestowanych wartości brzegowych oraz łącznej liczby zidentyfikowanych wartości brzegowych.
In 2-value BVA (Craig 2002, Myers 2011), for each boundary value there are two coverage items: this 
boundary value and its closest neighbor belonging to the adjacent partition. To achieve 100% coverage 
with 2-value BVA, test cases must exercise all coverage items, i.e., all identified boundary values. 
Coverage is measured as the number of boundary values that were exercised, divided by the total 
number of identified boundary values, and is expressed as a percentage. 

```Metoda trójpunktowa```: wartościami brzegowymi są wszystkie wartości do testów.
In 3-value BVA (Koomen 2006, O’Regan 2019), for each boundary value there are three coverage items: 
this boundary value and both its neighbors. Therefore, in 3-value BVA some of the coverage items may 
not be boundary values. To achieve 100% coverage with 3-value BVA, test cases must exercise all 
coverage items, i.e., identified boundary values and their neighbors. Coverage is measured as the 
number of boundary values and their neighbors exercised, divided by the total number of identified 
boundary values and their neighbors, and is expressed as a percentage. 