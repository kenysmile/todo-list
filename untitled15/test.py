import sqlite3
a = 'Tuan'
b = 'nguyentrongtuan'
con = sqlite3.connect("pvt.db")
cur = con.cursor()
cur.execute("SELECT Use, pas FROM User")
items = cur.fetchall()
for k , v in items:
    if k == a:
        print('Okie')
