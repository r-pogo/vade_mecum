# Zaawansowane techniki

## EXSIST/NOT EXSIST in subquery
The `EXISTS` operator is a boolean operator that tests for existence of rows in a subquery
```sql
SELECT 
    column1
FROM 
    table_1
WHERE 
    EXISTS( SELECT 
                1 
            FROM 
                table_2 
            WHERE 
                column_2 = table_1.column_1);
```
```sql
SELECT first_name,
       last_name
FROM customer c
WHERE EXISTS
    (SELECT 1
     FROM payment p
     WHERE p.customer_id = c.customer_id
       AND amount > 11 )
ORDER BY first_name,
         last_name;
```
NOT EXISTS
```sql
SELECT first_name,
       last_name
FROM customer c
WHERE NOT EXISTS
    (SELECT 1
     FROM payment p
     WHERE p.customer_id = c.customer_id
       AND amount > 11 )
ORDER BY first_name,
         last_name;
```
EXISTS and NULL
```sql
SELECT
    first_name,
    last_name
FROM
    customer
WHERE
    EXISTS( SELECT NULL )
ORDER BY
    first_name,
    last_name;
```
___
## CASE
```sql
CASE WHEN condition THEN result
WHEN another_condition THEN result
ELSE result
END
```
```sql
SELECT title,
       length,
       CASE
           WHEN length> 0
                AND length <= 50 THEN 'Short'
           WHEN length > 50
                AND length <= 120 THEN 'Medium'
           WHEN length> 120 THEN 'Long'
       END duration
FROM film
ORDER BY title;
```
```sql
select name,
case when monthlymaintenance > 100 then 'expensive' else 'cheap' end as cost
from cd.facilities
```
___
TODO skończyć
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018
- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-case/