# Data exploration with SELECT
```
SELECT column_names FROM table_name
WHERE criteria
ORDER BY column_names;
```
## SELECT
```
SELECT * FROM my_table;
```
```
SELECT column1, column2, column3 FROM table_name;
```
___
## DISTINCT
`DISTINCT` eliminates duplicates
```
SELECT DISTINCT column1 FROM table_name;
```
___
## ORDER BY
```
SELECT column1, column2, column3 
FROM table_name
ORDER BY column3 DESC; -- defoult is ASC
```
```
SELECT last_name, school, hire_date
FROM teachers
ORDER BY school ASC, hire_date DESC;
```
___
## WHERE
```
SELECT last_name, school, hire_date
FROM teachers
WHERE school = 'Cool School'
```
### Comparison Operators
| Operator | Function | Example |
|----------|----------|---------|
| = | Equal | WHERE column_name = 'Searched value'
| < | Less than | WHERE column_name < 10
| > | Greater than | WHERE column_name > 10
| <= | Less than or Equal | WHERE column_name <= 10
| >= | Greater than or Equal | WHERE column_name >= 10
| <> or != | Not Equal | WHERE column_name != 'Searched value'
| BETWEEN | in between| WHERE column_name BETWEEN 2000 and 4000
| IN | matches one of the values | WHERE column_name IN ('value1`, 'value2)
| LIKE | matches the pattern (case sensitive) | WHERE column_name LIKE 'Sam%'
| ILIKE | matches the pattern (case insensitive) | WHERE column_name ILIKE 'sam%'
| NOT | negation | WHERE column_name NOT LIKE 'Sam%`
___
## AND/OR operators
```
SELECT * FROM table_name
WHERE column1 = 'value'
AND column2 < value;
```
```
SELECT * FROM table_name
WHERE column1 = 'value'
OR column2 < value;
```
```
SELECT * FROM teachers
WHERE school = 'F.D Roosvelt HS'
AND (salary < 38000 OR slaary > 40000);
```
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018