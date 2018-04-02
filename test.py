import sqlite3
a = []
b = []

con = sqlite3.connect("pvt.db")
cur = con.cursor()
cur.execute("SELECT Ten, Hoten FROM Pvt")
items = cur.fetchall()
for (k,v) in items:
    a.append(k)
    b.append(v)
def retrieveUsers(dbs):
    con = sqlite3.connect("pvt.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Pvt WHERE 'Ten' = ?", (items))
    users = cur.fetchall()
    con.close()
    return users
print(retrieveUsers(dbs=items))
