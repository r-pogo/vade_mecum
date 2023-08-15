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

    cur.execute("INSET INTO customers (?,?,?)", (first_name, last_name, email))

    con.commit()
    con.close()


def del_person(id):
    con = sqlite3.connect("people.db")
    cur = con.cursor()

    con.commit()
    con.close()
