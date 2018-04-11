import sqlite3
string = 'Tung'
con = sqlite3.connect('pvt.db')
con = sqlite3.connect('pvt.db')
cur = con.cursor()
cur.execute("select * from User")
username = cur.fetchall()
for i,j in username:
    if string == i:
        print('Okie')
    else:
        print('No')
