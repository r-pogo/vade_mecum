# Q/A

### Kiedy skończyć testować?  
Generalnie tyle ile się da, ale nie można tego robić w nieskończoność, więc  
potrzebne są dobrze zdefiniowane `kryteria wyjścia`.

1. Osiągnięcie Celów Testowych: Testowanie może być uważane za zakończone, gdy  
osiągnie się cele testów zdefiniowane w test planie. Na przykład, gdy przetestowano 
wszystkie funkcje i scenariusze wymienione w planie.
2. Brak krytycznych błędów
3. Uzyskanie akceptacji od klienta
4. Osiągnięcie określonego poziomu pokrycia
5. Deadline/Termin wydania
6. Decyzja na podstawie ryzyka: jeśli pozostałe błędy lub problemy nie są  
    krytyczne, lub nie wpływają znacząco na użytkowników.
7. Zakończeni fazy testowe np. w wterfall model
8. Skończył się budżet

Żeby uprościć zadaj sobie następujące pytania:

Czy wszystkie przypadki testowe są wykonywane przynajmniej raz?  
Czy współczynnik zaliczenia przypadków testowych jest zgodny z definicją?  
Czy osiągnięto pełne pokrycie testem?  
Czy wszystkie przepływy funkcjonalne/biznesowe są wykonywane przynajmniej raz?  
Czy osiągnięto ustaloną liczbę defektów?  
Czy wszystkie główne defekty o wysokim priorytecie zostały naprawione i zamknięte?  
Czy wszystkie wady zostały ponownie przetestowane i usunięte?  
Czy przeprowadzono regresję dla wszystkich otwartych defektów?  
Czy wyczerpałeś budżet na testy?  
Czy nadszedł czas zakończenia testowania?  
Czy wszystkie produkty testowe są przeglądane i publikowane?  

Jeśli tak to git.

### Na jakiej podstawie można testować?
Przede wszystkim dokumentacja, dokumentacja i jeszcze raz dokumentacja!

Dużo zależy też od typów testów, ale inne podstawy to:
1. Wymagania i specyfikacje
2. Scenariusze użytkownika/user stories: Testowanie może być przeprowadzane na podstawie  
scenariuszy użytkownika, które opisują, jak użytkownicy będą korzystać z oprogramowania. 
3. Założenia projektowe.
4. Kod źródłowy
5. Dane testowe
6. Testy oparte na znanym zbiorze ataków i technik hakerskich-dla testów bezpieczeństwa
7. Kryteria akceptacyjne uzgodnione z klientem-testy akceptacyjne
8. Historia błędów i defektów
9. Doświadczenie

### Jakich testów nie można zaplanować?
Retesty po naprawie buga.

### Czego nie lubisz w testowaniu?
- Brak dokumentacji/informacji 
- Napięte terminy
- 
### + i - testów automatycznych?
Plusy:
- Szybkość i skutecznośc
- Powtarzalność
- Smoke testing i regresji
- Skomplikowane scenariusze: Np. duża ilość danych wejściowych
- Oszczędza czas: mogą runnować w weekend
- Lepsza kontrola nad procesem testowania, umożliwiając raportowanie wyników,  
- zarządzanie testami i automatyczne tworzenie dokumentacj

Minusy:
- Wymaga czasu i wysiłku, żeby je stworzyć
- Błędy w skryptach mogą prowadzić do fałszywych wyników
- Brak kreatywności i subiektywności: Automatyzacja nie jest w stanie  
  zastąpić kreatywności i intuicji ludzi w testowaniu niektórych aspektów, takich jak testy użyteczności
- Wymagane utrzymanie
- Brak ludzkiego kontekstu.

### + i - testów manualnych
Plusy:
- Zrozumienie kontekstu użytkownika
- Testowanie manualne pozwala na kreatywne podejście do testów,  
  co jest szczególnie ważne w przypadku testów użyteczności, eksploracyjnych i nieoczekiwanych przypadków
- Testy ad hocowe
- Testowanie niekompletnych aplikacji
- Zrozumienie subiektywnych ocen jakości: Testowanie manualne jest bardziej  
  odpowiednie do oceny subiektywnych aspektów jakości, takich jak estetyka, użyteczność i przekaz.

Minusy:
- Czasochłonne
- Ręczne testy mogą prowadzić do błędów ludzkich, a wyniki testów mogą być  
  trudne do powtórzenia dokładnie w tym samym sposób.
- Brak skalowalnośći
- Wymaga znacznych zasobów ludzkich i finansowych do przeprowadzenia testów manualnych na dużą skalę
- Brak zautomatyzowanych raportów
- Brak możliwj ciągłej integracji

### Przetestuj formularz logowania
Testy poprawnego logowania:
 - Test poprawnych danych logowania
 - Test poprawnego logowania jako administrator

Testy niepoprawnego logowania:
 - Test niepoprawnego hasła.
 - Test niepoprawnego loginu
 - Test blokady konta po wielokrotnych nieudanych próbach logowania

Testy pola formularza:
 - Test pustego pola hasła
 - Test pustego pola loginu.

Testy bezpieczeństwa:
 - SQL injection

Testy resetowania hasła.

Testy wydajności: sprawić jak formularz będzie się zachowywać podczas obciążenia
Test bezpieczeństwa hasła
Testy lokalizacji i języka
Testy obsługi błędów
Testy integracji z usługami zewnętrznymi: Jeśli formularz logowania korzysta z  
usług zewnętrznych, przetestuj integrację i uwierzytelnianie z tymi usługami.

### U mnie działa
1. Zebrać informacje
2. Zdiagnozować środowisko: upewnij się, że środowisko testowe jest zgodne z tym, na którym programista pracuje
3. Dobra dokumentacja w raporcie buga
4. Może defekt pojawia się tylko w określonych warunkach
5. Przegląd kodu może pomóc
6. Skontaktować sie bezpośrednio z devem.

### Konflikt dev tester, czy to bug czy feature?
Pogadaj z product owner

### what are test metric
### Jak podejdziesz do testowania dowolnej historii użytkownika w zwinnym projekcie?
1. Rozumienie hisorii i czego dokładnie wymaga użytkownik
2. Jakie cele i wartości dana historyjka ma dostarczyć użytkownikowi
3. Stworzyć Scenariusze testowe
4. Rozwinąć ST w PT

### Brak dokumentacji
1. Czy mamy jakaś dokumentacje powiązaną?
2. Rozmowa z innymi członkami zespołu i deweloperami i analitykami
3. Stwórz dokumentację na podstawi tych rozmów
4. Testowanie eksploracyjne/na doświadczeniu
5. Analiza kodu źródłowego
6. Skoncentruj się na obszarach, które są krytyczne dla funkcjonalności i celów projektu.

### Dlaczego testowanie regresji stanowi wyzwanie w zwinnym programowaniu i jak sobie z nim poradzić
1. Każdy sprint = nowa funkcjonalności + bug fixy czyli wielokrotne dostawy
2. krótki okres iteracji = mało czasu
3. Coraz większe testy regresji
4. Testowanie oparte na ryzyku
5. Najlepiej wszystko zautomatyzować

### Jakie będzie Twoje podejście do tworzenia przypadku testowego
1. Zapoznać się z wymaganiami
2. Wyjaśnić wszelkie wątpliwości
3. Stworzyć scenariusze testowe
4. Wystosować techniki projektowania testów w celu udoskonalenia scenariuszy testowych.
5. Tworzenie przypadków testowych:
   - Identyfikator testu
   - Określenie warunków początkowych
   - Opis kroków testu
   - Dane wejściowe
   - Środowisko
   - Oczekiwane wyniki
   - Faktyczne wyniki
   - Warunki zakończenia testu
   - Dodatkowe info
   - Notatki
6. Przegląd i walidacja/peer reviewed

### W jaki sposób można zapewnić, że wszystkie wymagania zostaną uwzględnione w testach
Kluczową rolę odgrywa `Macierz identyfikowalności wymagań`  
`(ang. Requirements Traceability Matrix, RTM)` to narzędzie służące do śledzenia  
związku między różnymi elementami projektu, takimi jak wymagania, przypadki testowe,  
zmiany w projekcie i inne. Celem RTM jest zapewnienie, że każde wymaganie jest  
przypisane do odpowiednich zadań i jest monitorowane na przestrzeni całego cyklu  
życia projektu.

Ważne jest również:
- Ustalenie priorytetów testów
- Narzędzi do zarządzania testami
- Monitorowanie postępu testów

### Jeśli oprogramowanie jest aktualnie w fazie produkcyjnej i jeden z modułów kodu został zmodyfikowany. Czy przetestujesz ponownie całą aplikację, czy tylko przetestujesz funkcjonalność związaną z tym modułem
Podejście do testowania w tym przypadku może zależeć od kilku czynników,  
takich jak zakres zmiany, złożoność aplikacji, czas i zasoby dostępne dla testowania  
oraz ryzyko związane z modyfikacją.

1. Testowanie tylko zmienionego modułu: Jeśli modyfikacje są ograniczone  
   do jednego konkretnego modułu i zmiany nie wpływają na inne części aplikacji, 
   można skoncentrować się na testowaniu tylko tego modułu.
2. Testowanie zmienionego modułu oraz obszarów wpływających: Jeśli zmiany w  
   module mogą wpłynąć na inne części aplikacji, warto przetestować również te  
   obszary, które mogą być dotknięte zmianami. To pomaga w identyfikacji potencjalnych regresji.
3. Testowanie funkcji kluczowych: Jeśli modyfikacje dotyczą funkcji kluczowych  
   lub krytycznych dla aplikacji, zaleca się przetestowanie tych funkcji oraz obszarów,  
   które mogą wpłynąć na ich działanie
4. Testowanie funkcjonalności end-to-end: Jeśli aplikacja jest złożona  
   i zmiany w module mogą mieć nieoczekiwane skutki w innych częściach aplikacji,  
   rozważ przeprowadzenie testów end-to-end, które obejmują całą ścieżkę  
   użytkownika lub scenariusze użycia
5. Testowanie na podstawie wcześniejsze błędy
6. Automatyczne testy regresji

### Czy zgadzasz się, że tester powinien studiować dokumenty projektowe w celu napisania przypadków testowych?
Tak.
1. Lepsze zrozumienie wymagań
2. Można określić zakres testu, jakie sa funkcje i moduły do przetestowania
3. Identyfikacja krytycznych ścieżek i przypadków użycia
4. Zrozumienie interakcji między modułami
5. Planowanie testów regresji
6. Można zwrócić feedback (testowanie statyczne)
