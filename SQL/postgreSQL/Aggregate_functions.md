# Aggregate Functions

## COUNT
```sql
SELECT COUNT (column_name) FROM table_name

SELECT COUNT (DISTINCT column_name) FROM table_name
```
## MAX
```sql
SELECT MAX(column_name) FROM table_name
```
## MIN
```sql
SELECT MIN(column_name) FROM table_name
```
## GROUP BY
Klauzula `GROUP BY` umożliwia grupować wyniki według wartości w jednej lub w większej liczbie kolumn.  
```sql
SELECT column1 FROM table_name
GROUP BY column1
ORDER BY column1 DESC

SELECT column1, COUNT(*) FROM table_name
GROUP BY column1
ORDER BY COUNT(*) DESC

-- GROUP BY na wielu kolumnach

SELECT column1, column2 COUNT(*) FROM table_name
GROUP BY column1, column2
ORDER BY column1 ASC,COUNT(*) DESC
```
___
## SUM
`SUM` działa tylko na liczbach
```sql
SELECT sum(col1)
FROM table_name
WHERE col1 > 0
```
___
## AVG
`AVG` działa tylko na liczbach

```sql
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```
___
## HAVING
`HAVING` umożliwia filtrowanie funkcji agregujących. Funkcje agregujace takie jak `sum()`  
nie mogą być używane w klauzuli `WHERE`, ponieważ działa na poziomie wiersza, a   
funkcje agregujące na zbiorze wierszy.
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;

SELECT sum(col1)
FROM table_name
HAVING sun(col1) > 50000
```
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018