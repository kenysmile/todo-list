import sqlite3
a = []
# tu = (
# 	('tu', 'phamvantu'),
# 	('tuan', 'nguyentrongtuan'),
# 	('nam', 'giangvannam')
# )
con = sqlite3.connect('pvt.db')
cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS Login")
# cur.execute("CREATE TABLE Login(Use TEXT PRIMARY KEY , pas TEXT)")
# cur.executemany("INSERT INTO Login(Use, pas) VALUES(?, ?)", tu)
#

def registerUser(username,password):
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
	con.close()

	return username
# registryUser('Quyen','dobaquyen')

def insertUsers(todo, use, ngay):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Phamtu (Todo, Use, ngay) VALUES (?, ?, ?)", (todo, use, ngay))
	con.commit()
	con.close()
#print(insertUsers('Gym', 'Tuan', '2018-8-8'))

def retrieveUsers(name):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("SELECT Todo FROM Phamtu WHERE Use = '%s' " % name)
	users = cur.fetchall()
	con.close()
	return users
# b = retrieveUsers('Tuan')
# c = ', '.join(map(str, b))
# #d = ''.join(c)
# print(c)
# for i in c:
# 	a.append(i)
# print(i)
# for i in b:
# 	a.append(i)
# print(i)


#print(retrieveUsers('Tuan'))
# a = []
# b = []
# users = retrieveUsers('Tuan')
# for i, j in users:
# 	a.append(i)
# 	b.append(j)
# print(a)
# print(b)

#print(list(sum(users, [])))
#users = ''.join(users)
# print(users[-2:-1])

def editUsers(name):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("update Phamtu set Todo = '%s' "% name)
	con.commit()
	con.close()

def removeUsers(todo):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("delete from Phamtu where Todo = '%s'" % todo)
	cur.fetchall()
	con.commit()
	con.close()

#print(removeUsers('football'))
#a = retrieveUsers('Tuan')
#print(a)
#print(removeUsers(a))





