import sqlite3

# tu = (
# 	('tu', 'phamvantu'),
# 	('tuan', 'nguyentrongtuan'),
# 	('nam', 'giangvannam')
# )
# con = sqlite3.connect('pvt')
# cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS Login")
# cur.execute("CREATE TABLE Login(Use TEXT PRIMARY KEY , pas TEXT)")
# cur.executemany("INSERT INTO Login(Use, pas) VALUES(?, ?)", tu)

def registryUser(username,password):
    con = sqlite3.connect("pvt.db")
    cur = con.cursor()
    cur.execute("INSERT INTO User (Use,pas) VALUES (?,?)", (username,password))
    con.commit()
    con.close()
def selectUser():
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("select * from User")
	username = cur.fetchall()
	return username
#print(selectUser())
# registryUser('Quyen','dobaquyen')


def insertUsers(todo, use, ngay):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Phamtu (Todo, Use, ngay) VALUES (?, ?, ?)", (todo, use, ngay))
	con.commit()
	con.close()
#print(insertUsers('Work', 'Tuan', '2018-6-6'))

def retrieveUsers(name):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("SELECT Todo FROM Phamtu WHERE Use = '%s' " % name)
	users = cur.fetchall()
	return users
#print(retrieveUsers('Tuan'))


def editUsers(name):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("update Phamtu set Todo = '%s' "% name)
	con.commit()

def removeUsers(todo):
	con = sqlite3('pvt.db')
	cur = con.cursor()
	cur.execute("delete from Phamtu where Todo = '%s'" % todo)




