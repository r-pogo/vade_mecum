# JOIN
```sql
SELECT * 
FROM table_a JOIN table_b
ON table_a.key_column = table_b.foreign_key_column
```
Można użyć dowolnego wyrażenia, które zwraca wartość logiczną `true` albo `false`
do lączenia table po klauzuli `ON` n.p: `ON table_a.key_column >= table_b.foreign_key_column`
___
## INNER JOIN
```sql
SELECT *
FROM schools_left JOIN schools_right
ON schools_left.id = schools_right.id
```
___
## LEFT/RIGHT JOIN
```sql
SELECT *
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id
```
___
## FULL OUTER JOIN
```sql
SELECT *
FROM schools_left FULL OUTER JOIN schools_right
ON schools_left.id = schools_right.id
```
___
## CROSS JOIN
CROSS JOIN = iloczyn kartezjański każdy wiersz z lewej tabeli złączony z wierszem z prawej.
Przedstawia wszystkie możliwe kombinacje wierszy. Złączenie nie potrzebuje połączeń pomiędzy kluczami,
nie trzeba podawać klauzuli przy użyciu słowa kluczowego `ON`.
```sql
SELECT *
FROM schools_left CROSS JOIN schools_right
```
___
## NULL
`NULL` może być wykorzystane do odkrycia brakujących danych w jednej z tabel.
```sql
SELECT *
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id
WHERE schools_right.id IS NULL -- Aby wyszykać kolumny które zawieraja dane użlibyśmy IS NOT NULL
```
___
## Typy relacji pomiedzy tabelami
| Relacja | Opis |
|---------|------|
| Jeden do jednego | Relacja, w której każdemy wierszowi z tabeli A może odpowiadać tylko jedne wiersz z tabeli B.
| Jeden do wielu | Relacja, w której każdemy wierszowi z tabeli A może występować wiele razy w tabeli B.|
| Wiele do wielu | Raelacja ta istnieje, gdy element lub kilka elementów w tabeli A może mieć relacje z elementem lub kilkoma elementami w tabeli B.
___
## Określanie kolumn w złączeniu
```sql
-- Dodajemy prefiks będący nazwą tabeli przed każdą kolumną

SELECT schools_left.id, schools_left.left_school, schools_right.right_school
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id
```
___
## Aliasowanie
```sql
/* W klauzuli FROM przy użyciu słowa kluczowego AS deklarujemy alias lt reprezentujący schools_left  
i alias rt reprezentujący schools_right. */

SELECT lt.id, lt.left_school, rt.right_school
FROM schools_left AS lt LEFT JOIN schools_right AS rt
ON lt.id =rt.id
```
## Złączanie wielu tabel
```sql
SELECT lt.id, lt.left_school, en.enrollment, gr.grades
FROM schools_left AS lt LEFT JOIN schools_enrollmetn AS en 
ON lt.id = en.id
LEFT JOIN schools_grades AS gr
ON lt.id =gr.id
```
___
## Obliczenia matematyczne na kolumnach łączonych tabel
TODO
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018