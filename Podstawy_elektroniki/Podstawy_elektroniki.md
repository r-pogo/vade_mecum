# Podstawy elektroniki

## Prąd
Jeżeli między dwoma punktami istnieje napięcie,  
to po umożliwieniu nośnikom przepływu z jednego punktu do drugiego zacznie płynąć prąd.
Prąd będzie tym większy, im więcej nośników przepłynie przez połączenie w jednostce czasu,  
a zatem prąd jest miarą szybkości ich przepływu.

Jednostką natężenia prądu jest amper, który oznaczamy literą A.

Natężenie prądu (I): Natężenie prądu to ilość ładunków elektrycznych,  
która przepływa przez przewodnik w jednostce czasu. Jednostką natężenia prądu jest amper (A),  
co oznacza, że 1 amper to przepływ 1 kulomba ładunku elektrycznego na sekundę.

## Napięcie
Napięcie elektryczne, oznaczane literą "V" (od Volta) wyrażane w woltach.  
Jest miarą siły napędowej, która przemieszcza ładunki elektryczne w obwodzie.
Przykład: Napięcie można porównać do wody zebranej przed tamą.  
Poziom wody (napięcia) mierzymy między dwoma umownymi punktami. Im więcej wody,  
tym szybciej będzie wypływała przez śluzę w tamie.

Napięcie może przez długi czas po prostu „istnieć”.  
Przykładowo, jeśli nie będziemy pobierać prądu z baterii AA (1,5 V),  
to będzie ona utrzymywała swoje napięcie przez kilka lat. Tak samo jak  
woda nagromadzona przed tamą z zamkniętą śluzą.

Napięcie może być `stałe DC` i `przemienne AC`.
- `stałe DC`:  ma stałą wartość i kierunek, nie zmienia się z czasem
- `przemienne AC`:  zmienia swoją wartość i kierunek w cykliczny sposób

## Opór (rezystancja)
Opór, inaczej zwany rezystancją, to miara oporu materiału lub elementu wobec przepływu prądu elektrycznego.

W przypadku analogii wodnej oporem będzie poziom otwarcia śluzy.  
Im jest szerzej otwarta, tym opór jest mniejszy i wypływa więcej wody.  
Im bardziej jest zamknięta, tym opór jest większy i ze zbiornika za tamą wypływa mniej wody

Jednostką rezystancji jest om – symbol `Ω (wielka litera omega)`;  
niekiedy zamiast niego stosuje się zapis `om` lub `R`

Rodzaje oporu:

`Opór stały`: Opór nie zmienia się zależnie od wartości prądu ani napięcia. Na przykład, większość przewodników metalowych ma praktycznie stały opór w zakresie normalnych warunków.

`Opór zmienne`: W niektórych materiałach, takich jak półprzewodniki, opór może zależeć 

## Moc
Moc w jednostkach SI (Międzynarodowego Układu Jednostek) jest mierzona w watach (W)  
i określa ilość energii przekazywanej lub zużywanej na jednostkę czasu.

## Rezystor
Rezystor to pasywny element elektroniczny, który wprowadza opór do obwodu elektrycznego.  
Jego głównym zadaniem jest kontrolowanie przepływu prądu w obwodzie poprzez dostarczanie  
oporu elektrycznego. Rezystory są szeroko stosowane w elektronice, zarówno do ograniczania prądu,  
jak i do podziału napięcia w obwodach.

## Prawo Ohma

V = I*R
V to napięcie elektryczne `(w woltach, V)`.  
I to natężenie prądu `(w amperach, A)`.  
R to opór `(w ohmach, Ω)`  

````
     /\
    /  \
   /    \
  /  V   \
 /--------\
/  I  | R  \
------------
````
## Pierwsze prawo Kirchhoffa
W dowolnym węźle (punkt rozgałęzienia) w obwodzie suma prądów wpływających do  
tego węzła jest równa sumie prądów wypływających z tego węzła

Pierwsze prawo Kirchhoffa jest szczególnie przydatne w analizie obwodów,  
w których prąd jest rozgałęziony w różnych kierunkach, na przykład w obwodach równoległych

## Drugie prawo Kirchhoffa
Drugie prawo Kirchhoffa odwołuje się do napięć na poszczególnych elementach układu.  
Mówi ono, że jeżeli wybierzemy w obwodzie dowolną drogę zamkniętą, to suma napięć  
pochodzących od źródeł zasilania jest równa sumie napięć na pozostałych elementach.

Czyli na podzespołach połączonych równolegle zawsze będzie to samo napięcie,  
ponieważ są dołączone do tego samego zasilania. Natomiast przy elementach połączonych  
szeregowo suma napięć (spadków napięć) na poszczególnych elementach jest równa napięciu zasilającemu.

Drugie prawo Kirchhoffa opiera się na zasadzie zachowania energii elektrycznej.  
Oznacza to, że w zamkniętym obwodzie suma energii elektrycznej dostarczanej do  
obwodu musi równać się sumie energii elektrycznej, która zostaje rozproszona lub zużyta w obwodzie.

To prawo jest szczególnie przydatne w analizie obwodów, w których napięcie jest  
rozdzielane między różnymi elementami obwodu, takimi jak rezystory, źródła napięcia i źródła prądu.  
Drugie prawo Kirchhoffa pomaga określić, jak napięcie jest podzielone w obwodzie i pozwala na  
analizę zachowania napięcia w różnych gałęziach obwodu.

## Kondensator
Kondensator to pasywny element elektroniczny używany w obwodach elektrycznych do  
przechowywania ładunku elektrycznego. Jego główną funkcją jest gromadzenie energii  
elektrycznej w polu elektrycznym między dwoma przewodzącymi płytami lub innymi przewodnikami.

biegunowe i bezbiegunowe (można mówić również o spolaryzowanych i niespolaryzowanych).  
Czyli dla niektórych kondensatorów istotny jest kierunek włączenia ich do obwodu, a  
dla pozostałych jest to całkowicie obojętne.

Kondensatory włączamy równolegle do zasilanego urządzenia, dzięki czemu zachowują  
się podobnie do akumulatorów: ładują się podczas normalnej pracy i rozładowują,  
kiedy nasze źródło zasilania jest chwilowo niewystarczające.

## Dioda krzemowa/prostownicze
Ich główną funkcją jest przewodzenie prądu w jednym kierunku (polarizacja przewodzenia) 
i blokowanie prądu w przeciwnym kierunku (polarizacja zaporowa).

## Dioda świecąca/LED
Generują światło w wyniku przepływu prądu elektrycznego przez nie. Dioda świecąca,  
jak sama nazwa wskazuje, jest zdolna do emitowania światła, co ją wyróżnia wśród  
innych diod półprzewodnikowych. Działa na zasadzie zjawiska elektroluminescencji,  
co oznacza, że konwertuje energię elektryczną na światło.

## Tranzystor
Tranzystor to trzywarstwowy półprzewodnikowy element elektroniczny, który jest  
używany do wzmacniania sygnałów elektrycznych, przełączania obwodów elektrycznych oraz  
innych zastosowań w elektronice.

Można spotkać się z tłumaczeniami, że tranzystor steruje przepływem prądu lub wzmacnia go - elektroniczny przełącznik.
Dzięki niemu możemy w bezpieczny sposób (małym prądem) włączyć przepływ większego prądu.

## Stabilizator
Stabilizator napięcia to urządzenie elektryczne lub elektroniczne, które ma za zadanie  
utrzymywać stabilne napięcie elektryczne na wyjściu, niezależnie od zmian w napięciu  
wejściowym lub obciążeniu. Stabilizatory napięcia są szeroko stosowane w elektronice i  
elektryce, aby chronić urządzenia elektryczne przed nagłymi fluktuacjami napięcia oraz zapewnić  
im napięcie zasilania w określonym zakresie.

## Przekaznik
Przekaźnik to elektromechaniczne urządzenie elektryczne, które służy do  
przekazywania sygnału lub sterowania prądem elektrycznym w jednym obwodzie za  
pomocą oddzielnego obwodu elektrycznego
