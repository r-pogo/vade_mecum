# Podstawy Testowania

## What is testing
Software testing is a set of activities to discover defects and evaluate the quality of software artifacts.
These artifacts, when being tested, are known as `test objects`.
A common misconception about testing is that it only consists of executing tests. 
However, software testing also includes other activities and must be aligned with the 
software development lifecycle.

Another common misconception about testing is that testing focuses entirely on verifying the test object.
Whilst testing involves `verification`, i.e., checking whether the system meets specified requirements, it also
involves `validation`, which means checking whether the system meets users’ and other stakeholders’
needs in its operational environment.

Testing is not only a technical activity. It also needs to be properly planned, managed, estimated,
monitored and controlled.

Testers use tools, but it is important to remember that testing is largely an intellectual
activity, requiring the testers to have specialized knowledge, use analytical skills and apply critical
thinking and systems thinking.

Testowanie to technologiczne badanie pozwalające otrzymać informacje o jakości  
testowanego produktu.

Testowanie jest procesem który składa się z następujących głównych punktów:
1. Planowanie testów
2. Monitorowanie i nadzór testów
3. Analiza testów
4. Projektowanie testów
5. Implementacja testów
6. Wykonywanie testów
7. Ukończenie testów

Testowanie może mieć zarówno formę `dynamiczną` (uruchamiamy testowany moduł/system),  
jak i `statyczną` (bez uruchomiania, dokumentacja itp).

Testowanie skupia się zarówno na:
- Werifikacji (Czy produkt tworzony jest prawidłowo?)
- Walidacji (Czy tworzony jest prawidłowy produkt?)

### Cele testowania K1
The typical test objectives are:
Evaluating work products such as requirements, user stories, designs, and code
• Triggering failures and finding defects
• Ensuring required coverage of a test object
• Reducing the level of risk of inadequate software quality
• Verifying whether specified requirements have been fulfilled
• Verifying that a test object complies with contractual, legal, and regulatory requirements
• Providing information to stakeholders to allow them to make informed decisions
• Building confidence in the quality of the test object
• Validating whether the test object is complete and works as expected by the stakeholders

### Testing and Debugging
Testowanie (ujawnia awarię): triggers failures that are caused by defects in
the software (dynamic testing) or can directly find defects in the test object (static testing). 

Debbugowanie (szuka przyczyny): debugging is concerned with finding causes of
this failure (defects), analyzing these causes, and eliminating them
___
### Why is Testing Necessary?

Testing provides a cost-effective means of detecting defects. These defects can then be removed (by
debugging – a non-testing activity), so testing indirectly contributes to higher quality test objects.
Testing provides a means of directly evaluating the quality of a test object at various stages in the SDLC.
These measures are used as part of a larger project management activity, contributing to decisions to
move to the next stage of the SDLC, such as the release decision.
Testing provides users with indirect representation on the development project. Testers ensure that their
understanding of users’ needs are considered throughout the development lifecycle. The alternative is to
involve a representative set of users as part of the development project, which is not usually possible due
to the high costs and lack of availability of suitable users.
Testing may also be required to meet contractual or legal requirements, or to comply with regulatory
standards

### QM/QA/TQC/testing
`Quality assurance` (zapewnianie jakości) jest często utożsamiane z testowaniem.
Są to dwa oddzielne procesy, które zawierają się w szerszym pojęciu `Quality management` (zarządzanie jakościa).  
`QM` obejmuje wszystkie czynności mające na celu kierowanie organizacji w dziedzinie  
jakości i ich nadzorowanie.

![img.png](img/img.png)

Testing is a form of quality control.

![img_1.png](img/img_1.png)

`QC`: `product-oriented`, corrective approach that focuses on those activities supporting the achievement 
of appropriate levels of quality.

`QA`: `process-oriented`, preventive approach that focuses on the implementation and improvement of 
processes. It works on the basis that if a good process is followed correctly, then it will generate a good 
product.

Test results are used by QA and QC. In QC they are used to fix defects, while in QA they provide 
feedback on how well the development and test processes are performing. 

Elementami `QM` są:
- `Zapewnianie jakości`: skupia się na przestrzeganiu właściwych procesów w celu uzyskania  
  pewności, że osiągnięte zostaną odpowiednie poziomy jakości. Jeśli proces jest wykonywany prawidłowo  
  powstające produkty pracy mają wyższą jakość.
- `Kontrola jakości`: obejmuje cały szereg czynności, także testowych, które wspierają  
  osiągnięcie odpowiednich poziomów jakości.

### Errors, Defects, Failures, Root Causes
- `Pomyłka/Error (błąd)`: działanie człowieka powodujące powstanie nieprawidłowego rezultatu (programista zle NAPISAŁ funkcje, w której pomylił znak + z *)
- `Defekt/Defect (bug, usterka)`: niedoskonałość, wada produktu pracy, polegająca na niespełnianiu wymagań (bug w kodzie czyli * zamiast +)
- `Awaria/Failure`: zdarzenie, w którym moduł/system nie wykonuje wymaganej funkcji w określonym zakresie. (kiedy użytkownik chce dodać to produk mnoży i bęc jest awaria)
- `Podstawowa przyczyna defektu/Root Cause`: fundamental reason for the occurrence of a problem

Errors and defects are not the only cause of failures. Failures can also be caused by environmental 
conditions, such as when radiation or electromagnetic field cause defects in firmware.

![img_2.png](img/img_2.png)

### Wyniki fałszywie pozytywne/negatywne

- `Fałszywie pozytywny`: raportowany jako defekt którego właściwie nie ma
- `Fałszywie negatywny`: nie wykrywają defektu który powinien zostać wykryty

Dlatego kluczowa jest analiza podstawowej przyczyny defektu.

### 7 testing principles
1. Testing shows the presence, not the absence of defects.
2. Exhaustive testing is impossible.
3. Early testing saves time and money.
4. Defects cluster together.
5. Paradoks pestycydów/Tests wear out.
6. Testing is context dependent. 
7. Przekonanie o braku błędów jest błędem/Absence-of-defects fallacy.

![img_3.png](img/img_3.png)
___
## Proces Testowy
### Planowanie testów
Czynności: 
- Cele testowania (co?)  
- Określenie czynności testowych potrzebnych do zrealizowania celów
- Określenie podejścia/strategii do osiągania celów testowania w granicach wyznaczonych przez kontekst (jak?)
  (np. określenie odpowiednich technik testowania i zadań testowych oraz sformułowanie harmonogramu testów, który umożliwi dotrzymanie wyznaczonego terminu)
- Zdefiniowanie miar
- Kryteria wyjścia

Produkty pracy:
 - Plan/y testów

### Monitorowanie i nadzór - czynności
Monitorowanie testów polega na ciągłym porównywaniu rzeczywistego z zaplanowanym  
postępem testowania przy użyciu miar specjalnie w tym celu zdefiniowanych w planie  
testów. Nadzór nad testami polega na podejmowaniu działań, które są niezbędne do  
osiągnięcia celów wyznaczonych w planie testów (z uwzględnieniem jego ewentualnych  
aktualizacji).

Element wspomagający monitorowanie testów i nadzór nad nimi to ocena kryteriów wyjścia  
z planu testów, która obejmuje:
- sprawdzenie rezultatów testów i dziennika testów pod kątem określonych kryteriów pokrycia;
- oszacowanie poziomu jakości modułu lub systemu na podstawie rezultatów testów i dziennika testów;
- ustalenie, czy są konieczne dalsze testy (np. w przypadku nieosiągnięcia przez  
  dotychczas wykonane testy pierwotnie założonego poziomu pokrycia ryzyka produktowego, co  
  wiąże się z koniecznością napisania i wykonania dodatkowych testów)
- raporty onpostępie testów
- informowanie intersariuszy o postępie w realizacji planu testów

Produkty pracy:
 - Raporty z testów

___
## Sources
- A. Doronins, ISTQB® Foundation: Getting Started, https://app.pluralsight.com/
- A. Roman, L. Stapp, Certifikowany tester ISTQB Poziom Podstawowy, Helion SA 2020
- Certified Tester Foundation Level Syllabus v4.0


