from flask import Flask, redirect, render_template, url_for, request
import sqlite3 as sql


app = Flask(__name__)

# user = (
#     ('Tu', 'phamvantu'),
#     ('Tuan','nguyentrongtuan'),
#     ('Nam', 'giangvannam')
# )
#
# con = sql.connect('database.db')
#
# with con:
#     cur = con.cursor()
#
#     cur.execute("DROP TABLE IF EXISTS User")
#     cur.execute("CREATE TABLE User(userame Varchar(20) PRIMARY KEY , password Varchar(20))")
#     cur.executemany("INSERT INTO User VALUES( ?, ?)", user)

@app.route('/home/')
def home():
    return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    a = []
    con = sql.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM User")
    users = cur.fetchall()
    for row in users:
        a.append(row)

    if request.method == 'POST':
        for (k, v) in users:
            if request.form['username'] == k and request.form['password'] == v:
                return redirect(url_for('home'))
            else:
                error = 'Invalid.Please try again'
    return render_template('login.html', error = error)

if __name__ == '__main__':
    app.run()
