# Podstawy testowania
## Co to jest testowanie

Testowanie to `technologiczne badanie` pozwalające otrzymać informacje o jakości testowanego produktu.

`technologiczne` = wykorystuje technologiczne podejście, eksperymenty, matematykę, logikę, narzędzia (programy wspomagające)
`badanie` = jest to zorganizowane poszukiwanie informacji

Testowanie składa się z zestawu czynności (procesu testowego) wykonywanych zarówno przed wykonaniem testów (1-5)
jak i po ich wykonaniu (7).

1. Planowanie testów
2. Monitorowanie testów i nadzór nad nimi
3. Analiza testów
4. Projektowanie testów
5. Implementacja testów
6. Wykonanie testów
7. Ukoniczenie testów

`Wykonanie testów` = uruchamianie oprogramowania w celu znalezenia defektów/bugów.
Czynność polegająca na przeprowadzeniu testumodułu lub systemu, by otrzymać rzeczywiste wyniki.

Testowanie obejmuje zarówno `weryfikację` jak i `walidację` systemu.

`Weryfikacja` = to proces sprawdzania, czy oprogramowanie spełnia wymagania.
Ocenia artefakty oprogramowania (takie jak wymagania, projekt, kod itp.), aby upewnić się,  
że spełniają one określone wymagania i standardy. Zapewnia, że oprogramowanie jest budowane  
zgodnie z potrzebami i specyfikacjami projektowymi.
Odpowiada na pytanie: Czy dobrze budujemy produkt?

`Walidacja` = to proces sprawdzania, czy specyfikacja oddaje wymagania klienta.  
Ocenia oprogramowanie pod kątem potrzeb i wymagań użytkownika. Zapewnia, że  
oprogramowanie pasuje do zamierzonego celu i spełnia oczekiwania użytkownika.
Odpowiada na pytanie: Czy budujemy właściwy produkt?

Podstawowe cele:
- dokonywanie oceny produktów pracy np. wymagania, historyjki użytkownika, projekt, kod
- sprawdzanie czy zostały spełnione wszystkie wyspecyfikowane wymagania
- sprawdzanie, czy przedmiot testów jest kompletny i działa zgodnie z oczekiwaniami użytkowników i innych interesariuszy
- budowanie zaufania do poziomu jakości przedmiotu testów
- wykrywanie defektów i awarii
- zapobieganie awariom
- dostarczanie interesariuszom informacji nizbędnych do podejmowania świadomych decyzji dotyczących poziomu jakości przedmiotów testów
- obniżanie poziomu ryzyka związanego z jakością oprogramowania
- przestrzeganie wymagań wynikających z umów, przpisów prawa i norm/standardów
- sprawdzanie czy obiekt testów jest zgodny z tymi wymaganiami lub standardami

!UWAGA! Testowanie (zwłaszcza dynamiczne) ujawnia `awarie` spowodowane `defektami`, natomiast `debugowanie`
jest czynością programistyczną wykonaną w celu zidentifikowania przyczyny defekty, poprawienu kodu i sprawdzeniu czy
defekt został naprawiony. Pospolite szukanie `buga` w kodzie.

3 poziomy powstania nieprawidłowego wyniku:

- `pomyłka/błąd (error/mistake)`: działanie człowieka powodujące powstanie nieprawidłowego  
rezultatu (błąd w pisaniu kodu, wybór złego algorytmu itp.)
- `defekt/pluskwa/usterka (defect/bug/fault)`: niedoskonałość lub wada produktu pracy, polegająca na niespełnieniu wymagań
- `awaria (failure)`: zdarzenie, w którym moduł luvb system nie wykonuje wymaganej funkcji w określonym zakresie.
!UAWAGA! awarie niekoniecznie są wywołane przez błedy ludzkie, np. czynniki środowiska (pole elektromoagnetyczne)

Nie wszystkie nioczekiwane wyniki testów oznaczją awarie:

- `wynik fałszywie pozytywny`: może być skutkiem błędów związanych z wykonywaniem testów, defektów w danych testowych, środowisku testowym itp.
Wyniki fałszywie pozytywne są raportowane jako defekty, których w rzeczywisotści nie ma.
- `wynik fałszywie negatywny`: sytuacji w której testy nie wykrywają defektu, który powinny wykryć.
___

## 7 zasad testowania

1. `Testowanie ujawnia usterki, ale nie może dowieść ich braku`: Testowanie pokazuje obecność, a nie brak usterek,  
testowanie ma charakter negatywny, tzn. pokazuje, że coś nie działa, a nie, że wszystko jest w porządku.
2. `Testowanie gruntowne jest niemożliwe`.
3. `Wczesne testowanie oszczędza czas i pieniądze (shift left)`.
4. `Kumulowanie się defektów`: reguła Pareto, 20% modułów zawiera 80% defektów
5. `Paradoks pestycydów`: jeżeli powtarzamy ciągle te same testy, to - po zmianach, które prowadzą do usunięcia wykrytych  
defektów, nie znajdziemy żadnych nowych usterek - przypadki testowe muszą być regularnie przeglądane i modyfikowane.
6. `Testowanie jest zależne od kontekstu`.
7. `Przekonanie o braku błędów jest błedem`: punkty 1 + 2 oraz fakt, że nawet aplikacja wolna od defektów,
może wciąż nie spełniać wymagań użytkownika.
___
## Proces testowy
`Proces testowy` to zbiór powiązanych ze sobą działań obejmujący planowanie i monitorowanie testów, ich analizę,  
projektowanie, implementację i zkaończenie.

Dobór procesu testowego do konkretnego oprogramowania zależy od wielu czynników.
Dobrą praktyką jest zdefinowanie `mierzalnych kryteriów pokrycia` dotyczących podstawy testów.
Mogą one pełnić funkcję tzw. kluczowych wskazników wydajnośći `KPI Key Performance Indicators`

Proces testowy w typowych sytuacjach składa się z:
1. Planowanie testów
2. Monitorowanie testów i nadzór nad nimi
3. Analiza testów
4. Projektowanie testów
5. Implementacja testów
6. Wykonywanie testów
7. Ukończenie testów

Grupy te są opisane logicznie sekwencyjne, ale w rzeczywistości mogą występować iteracyjnie, zazębiać się,  
występować jednocześnie czy być pomijane. Zalerzy od procesu.

W ramach procesu testowego powstają `produkty pracy`, dobrym punktem odniesienia dla prOduktów pracy
związanych z testowaniem jest standard międzynarodowy `ISO/IEC/IEEE 29119-3`.

### Czynnosci i produkty pracy
#### Planowanie testów
Czynności:
 - zdefiniowanie celów testowania
 - określenie czynności testowych potrzebnych do wypełnienia misji i zrealizowania celów testowania
 - określenie podejścia do osiągnięcia celów testowania w granicach wyznaczonych przez kontekst
 - harmonogram testów, który umożliwi dotrzymanie terminów
 - zdefiniowanie miar

Produkt pracy:
 - plan\plany testów

#### Monitorowanie testów i nadzór
Czynności:
 - sprawdzanie rezultatów i dziennika (loga) testów pod kątem określonych kryteriów pokrycia
 - oszacowanie poziomu jakości modułu lub systemu na podstawie rezultatów i dziennika testów
 - ustalenie, czy są konieczne dalsze testy
 - informowanie interesariuszy o postępie w realizacji planu testów
 - raporty o postępie testów

Produkt pracy:
 - raporty z testów np. raporty o postępie testów (tworzone na bieżąco), sumaryczne raporty końcowe 
   (tworzone w momencie osiągnięcia poszczególnych kamieni milowych)

#### Analiza testów
Analiza testów umożliwia zapoznanię się z podstawą testów i przeanalizowanie jej w celu  
zidentifikowania testowalnych cech i zdefiniowania związanych z nimi warunków testowych i  
oczywiście ustaleniem co należy testować.

Ogólne cele testowania zostaną przekształcone w konkretne warunki testowe i projekty testów.

Czynności:
 - zapoznanie się z podstawą testów, specyfikacją wymagań, wymagania biznesowe, wymagania funkcjonalne  
   wymagania systemowe, historyjki użytkownika, opowieści (epics), przypadki użycia, podobne produkty pracy;  
   określają one pożądane zachowanie gunkcjonalne i niefunkcjonalne modułu lub systemu
 - analiza informacji dotyczacych projektu i implementacji takich jak diagramy lub dokumenty opisujące  
   architekturę systemu lub oprogramowania, specyfikacje projektowe, przepływy wywołań, modele oprogramowania;
   dokumenty określające strukturę modułu lub systemu.
 - analiza implementacji samego modułu lub systemu, kodu, metadanych, zapytań do bazy danych oraz interfejsów
 - analiza raportów z analizy ryzyka
 - dokonanie oceny testowalności podstawy, aby zidentifikować często wytępujące typt defektów
 - zidentifikowanie cech które mają zostać przetestowane
 - zdefiniowanie warunków testowych w odniesieniu do poszczególnych cech oraz określenie ich priorytetów
 - stworzenie możliwości dwukierunkowego śledzenia powiązań między elementami podstawy testów
   a związanymi z nimi warunkami testowymi

Produkt pracy:
 - warunki testowe
 - dwukierunkowe śledzenie powiązań (macierz śledzenia) między tymi warunkami a  
   pokrywanymi przez nie elementami podstawy testów.
 - w testowaniu eksploracyjnym karty opisu testu
 - ewentualnie zgłoszenia o wykryciu defektów w podstawie testów








