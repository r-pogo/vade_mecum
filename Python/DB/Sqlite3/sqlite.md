# SQLite3

## Create SQL connection
```python
import sqlite3

con = sqlite3.connect("../database_name.db")

# you can also use a db in memory, which will disappear as soon as the programs ends.
con = sqlite3.connect(':memory:')
```
___
## Create cursor
In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
```python
import sqlite3

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()
```
___
## Create Table, commit and close connection
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text)
""")

# Call con.commit() on the connection object to commit the transaction:
con.commit()
# close connection,
con.close()
```
___
## Inserting values
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""INSERT INTO customers VALUES ('Rafal', 'Pogorzelski', 'elski@gmail.com')
""")


many_customers = [
    ('Pan', 'Kowalski', 'pan@kowal'),
    ('Francesca', 'Rossi', 'franca@rossi.com'),
    ('X', 'MrX', 'x@mrX.com')]

cur.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) # ? is a placeholder so first_name, last_name, email is (?,?,?)
con.commit()
```
___
## Query and fetch all
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT * FROM customers")
cur.fetchone()[2]
cur.fetchmany(4)[]
print(cur.fetchall()[])
[('Rafal', 'Pogorzelski', 'elski@gmail.com'), ('Pan', 'Kowalski', 'pan@kowal'), ('Francesca', 'Rossi', 'franca@rossi.com'), ('X', 'MrX', 'x@mrX.com')]

items = cur.fetchall()

for i in items:
    print(i)
    print(i[0])

con.commit()
````
___
## Primary keys 
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
 # primary hey == rowid
row_id = cur.execute("SELECT rowid, * FROM table")

for i in row_id:
    print(i)
    
con.commit()

(1, 'Rafal', 'Pogorzelski', 'elski@gmail.com')
(2, 'Pan', 'Kowalski', 'pan@kowal')
(3, 'Francesca', 'Rossi', 'franca@rossi.com')
(4, 'X', 'MrX', 'x@mrX.com')
```
___
## Where clause
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT * FROM table WHERE column = 'value' ")
cur.execute("SELECT * FROM table WHERE column LIKE '%value'")

con.commit()
```
___
## Update records
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""UPDATE table SET column1 = 'value1'
                WHERE column2 = 'value2'""")
# tip use the rowid to do updates
cur.execute("""UPDATE table SET column1 = 'value1'
                WHERE rowid = 1 """)
con.commit()
```
___
## Deleting records
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("DELETE from table WHERE rowid = 6")
con.commit()
```
___
## Order by
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT rowid, * FROM table ORDER BY value/column ASC/DESC")
con.commit()
```
___
## AND/OR
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT rowid, * FROM table WHERE value/column LIKE 'string%' AND/OR rowid=3")
con.commit()
```
___
## Limiting results
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT * FROM table_name LIMIT 2")
con.commit()
```
___
## Deleting table
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("DROP TABLE table_name")
con.commit()
```
___





https://www.youtube.com/watch?v=byHcYRpMgI4&ab_channel=freeCodeCamp.org

https://docs.python.org/3/library/sqlite3.html