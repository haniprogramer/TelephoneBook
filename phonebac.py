import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,name text,number INTEGER ,gmail text,groph text)')
    conn.commit()
    conn.close()


def insert(name, number, gmail, groph):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES(NULL,?,?,?,?)', (name, number, gmail, groph))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name='', number='', gmail='', groph=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE name=? OR number=? OR gmail=? OR groph=?', (name, number, gmail, groph))
    rows = cur.fetchall()
    conn.close()
    return rows


def delet(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update(id, name, number, gmail, groph):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('UPDATE  book SET name=?, number=?, gmail=?, groph=? WHERE id=?', (name, number, gmail, groph, id))
    conn.commit()
    conn.close()


connect()





