# Podstawy Testowania

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

Podstawowe cele testowania to:
  - Ocena produktów pracy, takich jak wymagania, khistoryjki użytkownika, projekt, kod;
  - Sprawdzanie, czy zostały spełnione wszystkie wyspecyfikowane wymagania;
  - Sprawdzanie, czy przedmiot testów jest kompletny i działa zgodnie z oczekiwaniami
    użytkowników i innych interesarjuszy
  - Budowanie zaufania do poziomu jakości przedmiotu testów;
  - Wykrywanie defektów i awarii
  - Zapobieganie awariom
  - Dostarczanie interesariuszom informacji niezbędznych do podejmowania świadomych  
    decyzji dosyczących zwłaszcza poziomu jakości przedmiotu testów;
  - Obniżanie poziomu ryzyka związanego z jakością oprogramowania;
  - Przestrzeganie wymagań wynikających z umów, przepisów prawa i norm/standardów;
  - Sprawdzanie, czy obiekt testowy jest zgodny z tymi wymaganiami lub standardami;
___
## QA/QM
`Quality assurance` (zapewnianie jakości) jest często utorzsamiane z testowaniem.
Są to dwa oddzielne procesy, które zawierają się w szerszym pojęciu `Quality management` (zarządzanie jakościa).  
`QM` obejmuje wszystkie czynności mające na celu kierowanie organizacji w dziedzinie  
jakości i ich nadzorowanie

Elementami `QM` są:
- `Zapewnianie jakości`: skupia się na przestrzeganiu właściwych procesów w celu uzyskania  
  pewności, że osiągnięte zostaną odpowiednie poziomy jakości. Jeśli proces jest wykonywany prawidłowo  
  powstające produkty pracy mają wyższą jakość.
- `Kontrola jakości`: obejmuje cały szereg czynności, także testowych, które wspierają  
  osiągnięcie odpowiednich poziomów jakości.
___
## Pomyłka, defekt i awaria
- `Pomyłka (błąd)`: działanie człowieka powodujące powstanie nieprawidłowego rezultatu  (programista zle napisał funkcje wktórej pomylil znak + z *)
- `Defekt (bug, usterka)`: niedoskonałość, wada produktu pracy, polegająca na niespełnianiu wymagań  (bug w kodzie czyli * zamiast +)
- `Awaria`: zdarzenie, w którym moduł/syytem nie wykonuje wymaganej funkcji w okreśłonym zakrasie. (kiedy użytkownik chce dodać to produk mnoży i bęc jest awaria)
___
## Wyniki fałszywie pozytywne/negatywne

- `Fałszywie pozytywny`: raportowany jako defekt którego właściwie nie ma
- `Fałszywie negatywny`: nie wykrywają defektu który powinien zostać wykryty

Dlatego kluczowa jest analiza podstawowej przyczyny defektu.
___
## 7 zasad testowania
1. Testowanie ujawnia usterki, ale nie może dowieść ich braku.
2. Testowanie gruntowne jest niemożliwe.
3. Wczesne testowanie oszczędza czas i pieniądze.
4. Kumulowanie się defektów.
5. Paradoks pestycydów
6. Testowanie jest zależne od kontekstu.
7. Przekonanie o braku błędów jest błędem.
___



