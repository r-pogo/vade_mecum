# CREATE and INSERT
## Create a database
```sql
CREATE DATABASE analysis;
```
___
## Create table
Create table X creates a table named `X`. This process requires the definition  
of the data type you plan to store in each column.
```sql
CREATE TABLE customer(
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(60) NOT NULL,
company VARCHAR(60) NULL,
street VARCHAR(50) NOT NULL,
city VARCHAR(40) NOT NULL,
state CHAR(2) NOT NULL DEFAULT 'PA',
zip SMALLINT NOT NULL,
phone VARCHAR(20) NOT NULL,
birth_date DATE NULL,
sex CHAR(1) NOT NULL,
date_entered TIMESTAMP NOT NULL,
id SERIAL PRIMARY KEY
);
```
```sql
CREATE TABLE product(
type_id INTEGER REFERENCES product_type(id), -- secondary key
name VARCHAR(30) NOT NULL,
supplier VARCHAR(30) NOT NULL,
description TEXT NOT NULL,
id SERIAL PRIMARY KEY);
```
```sql
CREATE TABLE sales_person(
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(60) NOT NULL,
street VARCHAR(50) NOT NULL,
city VARCHAR(40) NOT NULL,
state CHAR(2) NOT NULL DEFAULT 'PA',
zip SMALLINT NOT NULL,
phone VARCHAR(20) NOT NULL,
birth_date DATE NULL,
sex sex_type NOT NULL, -- Custom data type
date_hired TIMESTAMP NOT NULL,
id SERIAL PRIMARY KEY
);
```
### Some data types
Character Types 
1. Char(5) : Stores up to a max number of 5 characters
2. Varchar : Store any length of characters
3. Varchar(20) : Store up to 20 characters
4. Text : Store any length of characters
Numeric Types : Used when you need accuracy / precision
Serial : Whole numbers that also auto increment. Always used for column ids.
5. Smallserial : 1 to 32,767
6. Serial : 1 to 2147483647
7. Bigserial : 1 to 9223372036854775807
Integer : Whole numbers only Always used when you don’t need a decimal
8. Smallint : -32,768 to 32, 767
9. Integer : -2,147,583,648 to 2,174,483,647
10. Bigint : -9223372036854775808 to 9223372036854775807
Floats
11. Decimal : 131072 whole digits and 16383 after decimal
12. Numeric : 131072 whole digits and 16383 after decimal
13. Real : 1E-37 to 1E37 (6 places of precision)
14. Double Precision : 1E-307 to 1E308 (15 places of precision) Used when decimal doesn’t have to be very precise
15. Float : Same as double
Boolean
16. True, 1, t, y, yes, on
17. False, 0, f, n, no, off
18. null

Date / Time 
DATE
1. No matter what format you enter you get this : 1974-12-21
TIME
2. TIME WITHOUT TIME ZONE (Default)
3. ‘1:30:30 PM’:: TIME WITHOUT TIME ZONE -> 13:30:30
4. 01:30 AM EST -> 01:30-5:00 (UTC Format)
5. 01:30 PM PST -> 01:30-8:00
6. 01:30 PM UTC -> 01:30+00:00
7. ’01:30:30 PM EST’::TIME WITH TIME ZONE -> 13:30:30-5:00
TIMESTAMP
8. ‘DEC-21-1974 1:30 PM EST’::TIMESTAMP WITH TIME ZONE -> 1974-12-21 13:30-5:00
INTERVAL
9. Represents a duration of time
10. ‘1 day’::INTERVAL -> 01:00
11. ‘1 D 1 H 1 M 1 S’::INTERVAL -> 01:01:01:01
12. You can add and subtract intervals
13. You can add or subtract intervals from dates
14. (‘DEC-21-1974 1:30 PM EST’::TIMESTAMP WITH TIME ZONE) – (‘1 D’::INTERVAL)
Also Currency, Binary, JSON, Range, Geometric, Arrays, XML, UUID
Data Constraints 

NOT NULL = If you mark data as not null that means it must have a value when a new row of data is created
DEFAULT = designates a default value when a row is created without data
___
## Inserting data to table
```sql
INSERT INTO customer(first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered)  
VALUES ('Christopher', 'Jones', 'christopherjones@bp.com', 'BP', '347 Cedar St', 'Lawrenceville', 'GA', '30044', '348-848-8291', '1938-09-11', 'M', current_timestamp);
```
Inserting multiple values
```sql
INSERT INTO product_type (name) VALUES ('Business');
INSERT INTO product_type (name) VALUES ('Casual');
INSERT INTO product_type (name) VALUES ('Athletic');
```
You can insert multiple rows without defining column names if you put the values in the same order as the table data.
```sql
INSERT INTO product VALUES
(1, 'Grandview', 'Allen Edmonds', 'Classic broguing adds texture to a charming longwing derby crafted in America from lustrous leather'),
(1, 'Clarkston', 'Allen Edmonds', 'Sharp broguing touches up a charming, American-made derby fashioned from finely textured leather'),
(1, 'Derby', 'John Varvatos', 'Leather upper, manmade sole'),
(1, 'Ramsey', 'Johnston & Murphy', 'Leather upper, manmade sole'),
(1, 'Hollis', 'Johnston & Murphy', 'Leather upper, manmade sole'),
(2, 'Venetian Loafer', 'Mezlan', 'Suede upper, leather sole'),
```
___
## Creating TYPE
```sql
CREATE TYPE sex_type as enum
('M', 'F');
```
___
## Creating INDEX
```sql
-- Create index based on a single column (Use UNIQUE INDEX for a unique index)
CREATE INDEX transaction_id ON transaction(name)

-- Create an index based on 2 columns
CREATE INDEX transaction_id_2 ON transaction(name, payment_type)
```
___
## Sources
- A. DeBarros, Practical SQL: A Beginner's Guide to Storytelling with Data, No Starch Press 2018
- D. Banas, https://github.com/derekbanas/postgresql-tutorial/tree/main
