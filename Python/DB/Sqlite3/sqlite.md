# SQLite3
Table of content:
- [Create SQL connection](#create-sql-connection)
- [Create cursor](#create-cursor)
- [Create Table, commit and close connection](#create-table-commit-and-close-connection)
- [Inserting values](#inserting-values)
- [Query and fetch all](#query-and-fetch-all)
- [Primary keys](#primary-keys)
- [Where clause](#where-clause)
- [Update records](#update-records)
- [Deleting records](#deleting-records)
- [Order by](#order-by)
- [AND/OR](#andor)
- [Limiting results](#limiting-results)
- [Deleting table](#deleting-table)
## Create SQL connection <div id='create-sql-connection'/>
```python
import sqlite3

con = sqlite3.connect("../database_name.db")

# you can also use a db in memory, which will disappear as soon as the programs ends.
con = sqlite3.connect(':memory:')
```
___
## Create cursor <div id='create-cursor'/>
In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
```python
import sqlite3

import sqlite3
con = sqlite3.connect("database_name.db")

cur = con.cursor()
```
___
## Create Table, commit and close connection <div id='create-table-commit-and-close-connection'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("""CREATE TABLE table_name (
            column_name1 data_type(e.g"text),
            column_name2 text,
            column_name3 text)
""")

# Call con.commit() on the connection object to commit the transaction:
con.commit()
# close connection,
con.close()
```
___
## Inserting values <div id='inserting-values'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("""INSERT INTO table_name VALUES ('Rafal', 'Pogorzelski', 'elski@gmail.com')
""")


many_customers = [
    ('Pan', 'Kowalski', 'pan@kowal'),
    ('Francesca', 'Rossi', 'franca@rossi.com'),
    ('X', 'MrX', 'x@mrX.com')]

cur.executemany("INSERT INTO table_name VALUES (?,?,?)", many_customers) # ? is a placeholder so first_name, last_name, email is (?,?,?)
con.commit()
```
___
## Query and fetch all <div id='query-and-fetch-all'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("SELECT * FROM table_name")
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
## Primary keys <div id='primary-keys'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()
 # primary hey == rowid
row_id = cur.execute("SELECT rowid, * FROM table_name")

for i in row_id:
    print(i)
    
con.commit()

(1, 'Rafal', 'Pogorzelski', 'elski@gmail.com')
(2, 'Pan', 'Kowalski', 'pan@kowal')
(3, 'Francesca', 'Rossi', 'franca@rossi.com')
(4, 'X', 'MrX', 'x@mrX.com')
```
___
## Where clause <div id='where-clause'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("SELECT * FROM table WHERE column = 'value' ")
cur.execute("SELECT * FROM table WHERE column LIKE '%value'")

con.commit()
```
___
## Update records <div id='update-records'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("""UPDATE table SET column1 = 'value1'
                WHERE column2 = 'value2'""")
# tip use the rowid to do updates
cur.execute("""UPDATE table SET column1 = 'value1'
                WHERE rowid = 1 """)
con.commit()
```
___
## Deleting records <div id='deleting-records'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("DELETE from table WHERE rowid = 6")
con.commit()
```
___
## Order by <div id='order-by'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("SELECT rowid, * FROM table ORDER BY value/column ASC/DESC")
con.commit()
```
___
## AND/OR <div id='andor'/>
```python
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("SELECT rowid, * FROM table WHERE value/column LIKE 'string%' AND/OR rowid=3")
con.commit()
```
___
## Limiting results <div id='limiting-results'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("SELECT * FROM table_name LIMIT 2")
con.commit()
```
___
## Deleting table <div id='deleting-table'/>
```python
import sqlite3
con = sqlite3.connect("database_name.db")
cur = con.cursor()

cur.execute("DROP TABLE table_name")
con.commit()
```
___
## Sources
 - Python Documentation, https://docs.python.org/3/library/sqlite3.html 
 - freeCodeCamp.org, https://www.youtube.com/watch?v=byHcYRpMgI4&ab_channel=freeCodeCamp.org
 