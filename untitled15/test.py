import sqlite3
db = []
tu = (
    (1, 'tu', 'phamvantu'),
    (2, 'tuan','nguyentrongtuan'),
)
tu1 = (
    (1, 'cau long', 1),
    (2, 'bong ban', 2),
)
# con = sqlite3.connect('kenysmile.db')
# # cur.execute("DROP TABLE IF EXISTS Todo")
# # # cur.execute("CREATE TABLE User(id int PRIMARY KEY, username text, password text)")
# # # cur.executemany("INSERT INTO User VALUES(?, ?, ?)", tu)
# # cur.execute("create table Todo(id int PRIMARY KEY, work text, userid int)")
# # cur.execute("insert into Todo values(4, 'gym', 4)")
# a = []
# b = []
# c = 'thang'
# with con:
#     cur = con.cursor()
#     items = cur.execute("select id from User where username = 'tu'")
#     for item in items:
#         a.append(item)
#
#     print(item)

   #  rows = cur.execute("insert into Todo(work) values(?)", [c])
   #  rows.fetchone()

	#print(item[0])




#print(items)
	# items.fetchall()
	# print(items)
	# print(tuple(items))
	# for item in items:
	# 	a.append(item)
	# print(a)


a = 'Tu'
con = sqlite3.connect("phamvantu.db")
cur = con.cursor()
user = cur.execute("select * from User")
user.fetchall()
#print(user)
# item = cur.execute("INSERT INTO Congviec (user, work) VALUES (?, ?)",([user], a))
# item.fetchone()
# item.fetchall()

# list[item]
#print(item)


# #
def insertUser(user, work):
	con = sqlite3.connect("phamvantu.db")
	cur = con.cursor()
#
	#cur.execute("select username from User")

	cur.execute("INSERT INTO Congviec (user, work) VALUES (?, ?)",(user,work))
	con.commit()
	con.close()

#print(insertUser('thang', 'backetball'))
# #
def retrieveUsers(a):
	con = sqlite3.connect("phamvantu.db")
	cur = con.cursor()
	cur.execute("select work from Congviec where user = '%s'" %a)
#	cur.execute("SELECT work from Congviec WHERE  user= 'tu'")
	users = cur.fetchall()
	con.close()
	return users
insertUser('Tuan', 'sex')
print(retrieveUsers('Tuan'))
#print(retrieveUsers())
# # data
# tu1 = (
#     ('tu', 'cau long'),
#     ('tuan', 'bong ban'),
#     ('truong', 'boi')
# )
# tu2 = (
#     ('tu', 'phamvantu'),
#     ('tuan', 'nguyentrongtuan'),
#     ('truong', 'phamtuantruong')
# )
# # get connection and cursor objects
# conn = sqlite3.connect('tu1')
# c = conn.cursor()

# # create tables
# c.execute('''create table login (username text , password text)''')
# #c.execute('''create table work (username text, work text)''')
#
# c.executemany('insert into login values (?,?)', tu2)
#
# #c.executemany('INSERT INTO work VALUES (?,?)', WORK)
#
#


















def insertUser(k, v, todo):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Pvt (Ten, Hoten, Todo) VALUES (?, ?, ?)", (k, v, todo))
	con.commit()
	con.close()

#print(insertUser(todo='ball'))

def retrieveUsers(name):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("SELECT Todo FROM Pvt WHERE Ten = '%s' " % name)
	users = cur.fetchall()
	con.close()
	return users
