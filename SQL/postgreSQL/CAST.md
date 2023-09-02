# CAST
```sql
SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
FROM date_time_types;

SELECT numeric_column,
CAST(numeric_column AS integer),
CAST(numeric_column AS varchar(6)
FROM number_data_types;

/*This will return invalid input syntax for integer, because letters cannot be integers
CAST only works if the target data type can hold the original value, e.g:
Casting an integer to text is possible because character types can include numbers.  
There is no way to cast text containing letters to a number.*/

SELECT CAST(char_column AS integer) FROM char_data_types;
```
CAST can be also done by using `::` symbol
```sql
SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
FROM date_time_types;

-- This will do the same as the query above

SELECT timestamp_column::varchar(10)
FROM date_time_types;
```
```sql
ALTER TABLE customer
ALTER COLUMN sex TYPE sex_type USING sex::sex_type;
```
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018
- D. Banas, https://github.com/derekbanas/postgresql-tutorial/tree/main
