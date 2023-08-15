import sqlite3

# Initially created a DB with the following records:
# (1, 'Rafał', 'Pogorzelski', 'raf@pogo.com')
# (2, 'Pan', 'Kowalski', 'pan@kowal')
# (3, 'Francesca', 'Rossi', 'franca@rossi.com')
# (4, 'X', 'MrX', 'x@mrX.com')

def show_people():
    con = sqlite3.connect("people.db")
    cur = con.cursor()

    cur.execute("SELECT rowid, * FROM employees")
    people = cur.fetchall()

    for person in people:
        print(person)

    con.commit()
    con.close()


def add_person(first_name, last_name, email):
    con = sqlite3.connect("people.db")
    cur = con.cursor()

    cur.execute("INSERT INTO employees VALUES (?,?,?)", (first_name, last_name, email))

    con.commit()
    con.close()


def add_persons(list_people):
    con = sqlite3.connect("people.db")
    cur = con.cursor()

    cur.executemany("INSERT INTO employees VALUES (?,?,?)",
                list_people)

    con.commit()
    con.close()


def del_person(primary_key):
    con = sqlite3.connect("people.db")
    cur = con.cursor()
    cur.execute("DELETE from employees WHERE rowid = (?)", primary_key)

    con.commit()
    con.close()


def email_lookup(email):
    con = sqlite3.connect("people.db")
    cur = con.cursor()

    cur.execute("SELECT rowid, * FROM employees WHERE email = (?)", (email,))
    people = cur.fetchall()

    for person in people:
        print(person)

    con.commit()
    con.close()

