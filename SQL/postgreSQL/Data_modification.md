# Data modification
## ALTER
```sql
ALTER TABLE table ADD COLUMN colmn data_type;

ALTER TABLE table DROP COLUMN column;

ALTER TABLE table ALTER COLUMN column SET DATA TYPE data_type;

--Dodanie ograniczenia NOT NULL
ALTER TABLE table ALTER COLUMN column SET NOT NULL;

-- Usunięcie ograniczenie NOT NULL
ALTER TABLE table ALTER COLUMN cllumn DROP NOT NULL;

-- Deleting/Dropping
ALTER TABLE table_name DROP COLUMN column_name;

DROP TABLE table_name;
```
___
## UPDATE
Instrukcja `UPDATE` modyfikuje dane w kolumnie we wszystkich wierszach lub podzbiorze wierszy spełniający warunek.
```sql
UPDATE table
SET column = value;

UPDATE table
SET column1 = value,
SET column2 = value;

UPDATE table
SET column = value
WHERE criteria;
```
Można również zaktualizować jedną tabelę za pomocą wartości z innej tabeli.
```sql
UPDATE table
/* W klauzuli SET znajduje się podzapytanie, które stanowi instrukcja SELECT
ijęta w nawias, generująca wartości dla aktulaizacji */
SET column = (SELECT column FROM table_b
              WHERE table.column = table_b.column)
/* Klauzula WHERE EXSISTS używa instrukcji SELECT do generowania wartości, które służą jako 
filtr aktualizacji. Jeśli nie użyjemy tej kaluzuli, możemy nie umyślnie ustawić niektóre wartości NULL
WHERE EXISTS = (SELECT column FROM table_b
               WHERE table.column = table_b.column)
               
 -- Postgresql obsługuję też prostszą składnie
 UPDATE table
 SET column = table_b.column
 FROM table_b
 WHERE table.column = table_b.column
```
___
## Tworzenie kopii zapasowej tabel
```sql
CREATE TABLE copy_table
AS SELECT * FROM original_table
```
___
## DELETING
```sql
DELETE FROM table_name;

DELETE FROM table_name WHERE expression;
```
___
TODO skończyć!!!
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018