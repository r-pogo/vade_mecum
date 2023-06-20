# Modele cyklu życia oprogramowania
Zasady dobrego testowania, niezależne od modelu:
- dla każdej czynności związanej z wytwarzaiem oprogramowania istnieje odpowiadająca czynność testowa
- każdy poziom testów ma przypisane cele odpowiednie do tego poziomu (tu wyrycie jak największej liczby  
  defektów, a tam walidacja)
- analizę i projektowanie testów ma potrzeby danego poziomu testów należy rozpocząć  
  podczas wykonywania odpowiadającej mu czynności związanej z wytwarzaniem oprogramowania
  ("shift left" - czynności testowe rozpoczynają sięmożliwie najwcześniej)
- testerzy powinni uczestniczyć w dyskusjach dotyczących definiowania i doprecyzowania  
  wymagań i projektu oraz w przeglądach produktów pracy natychmiast po udostępnieniu  
  wersji roboczych odpowiednich dokumentów
___
## Modele
### Modele sekwencyjne
Zakładają wykonywanie poszczególnych czynności wytwórczych jedna po drugiej - liniowo.  
Zakładają, przynajmiej w teorii, że zanim rozpocznie się kolejna faza, następuje moment  
werifikacji tego, czy wszystkie czynności fazy poprzedzającej zostały wykonane poprawnie.

#### Model kaskadowy (waterfall)
Czynności związane z wytwarzaniem oprogramowania wykonuje się jedna po drugiej.
Czynności testowe następują dopiero, gdy wszystkie inne czynności wytwórcze zostaną ukończone.
Jest to porbelm dla testera z braku możliwości "shift left", jest to dobry model w  
projektach w których występują bardzo dobrze zidentifikowane wymagania i ryzyko ich zmiany jest  
niewielkie.

#### Model V
Zakłada integrację procesu testowania z całym procesem wytwarzania oprogramowania,  
stostując zasade wczenego testowania.
Model V obejmuje poziomy testowaniapowiązane z poszczególnymi odpowiadającymi im fazami  
wytwarzania oprogramowania, co dodatkowo sprzyja wczesnemu testowaniu.