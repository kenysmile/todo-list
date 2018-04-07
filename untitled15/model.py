import sqlite3
db = []
tu = (
    ('Tu', 'phamvantu'),
    ('Tuan','nguyentrongtuan'),
    ('Nam', 'giangvannam')
)
# todo = (
#     ('football', 'Tu', '2018-1-1'),
#     ('tennis', 'Tuan', '2018-2-2'),
#     ('swimming', 'Thanh', '2018-3-3')
# )
con = sqlite3.connect('pvt.db')
a = []
b = []

# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS Pvt")
#     cur.execute("CREATE TABLE Pvt(Ten Varchar(20) PRIMARY KEY , Hoten Varchar(20), work Varchar(20))")
#     cur.executemany("INSERT INTO Pvt VALUES( ?, ?, ?)", tu)

# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS User")
#     cur.execute("CREATE TABLE User(Use Varchar(20) PRIMARY KEY , pas Varchar(20))")
#     cur.executemany("INSERT INTO User VALUES( ?, ?)", tu)
#
#
# a = []
# b = []
# con = sqlite3.connect("pvt.db")
# cur = con.cursor()
# cur.execute("SELECT Ten FROM Pvt")
# dbs = cur.fetchall()

def insertUsers(todo, use, ngay):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Phamtu (Todo, Use, ngay) VALUES (?, ?, ?)", (todo, use, ngay))
	con.commit()
	con.close()
# print(insertUsers('ccccc', 'Tu', '2018-5-5 '))
# def insertUsers(k, v, work):
# 	con = sqlite3.connect("pvt.db")
# 	cur = con.cursor()
# 	cur.execute("INSERT INTO Pvt (Ten, Hoten, work) VALUES (?, ?, ?)", (k, v, work))
# 	con.commit()
# 	con.close()
#print(insertUsers('lsdasdfghg', 'Tuan', '2018-2-2'))
def retrieveUsers(name):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("SELECT Todo FROM Phamtu WHERE Use = '%s' " % name)
	users = cur.fetchall()

	# con.close()
	return users
# print(retrieveUsers('Tu'))


def editUsers(name):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("update Phamtu set Todo = '%s' "% name)
	con.commit()

def removeUsers(todo):
	con = sqlite3('pvt.db')
	cur = con.cursor()
	cur.execute("delete from Phamtu where Todo = '%s'" % todo)

	# con.close()

