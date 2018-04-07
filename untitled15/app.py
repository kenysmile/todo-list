from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import model as dbHandler
app = Flask(__name__)

a = []
b = []
c = []
con = sqlite3.connect("pvt.db")
cur = con.cursor()

cur.execute("SELECT Use, pas FROM User")
items = cur.fetchall()

@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':
        for (k,v) in items:
            if request.form['username'] == k and request.form['password'] == v:
                response = redirect(url_for("index"))
                response.set_cookie('user', k)
                response.set_cookie('pass', v)
                return response
            else:
                error = 'Invalid.Please try again'
    return render_template('login.html', error = error)

@app.route('/index', methods=['GET', 'POST'])
def index():
    user_id = request.cookies.get('user')
    user_pass = request.cookies.get('pass')
    #users = request.cookies.get('users')
    users = dbHandler.retrieveUsers(user_id)
    if request.method == 'POST':
        todo = request.form['work']
        ngay = request.form['date']
        dbHandler.insertUsers(todo, user_id, ngay)
        dbHandler.retrieveUsers(user_id)

        return redirect(url_for('add'))
    else:
        return render_template('index.html', users = users, user_id = user_id)

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    user_id = request.cookies.get('user')

    users = dbHandler.retrieveUsers(user_id)
    if request.method == 'POST':
        todo = request.form['work']
        ngay = request.form['date']
        dbHandler.insertUsers(todo, user_id, ngay)
        dbHandler.retrieveUsers(user_id)
        res = redirect(url_for('index'))
        res.set_cookie('todo', todo)
        return res
    else:
        error = 'Bug'
    return render_template('index.html', users = users, error=error)

@app.route('/remove')
def remove():
    user_id = request.cookies.get('user')
    todo = request.cookies.get('todo')

    dbHandler.editUsers(todo)
    dbHandler.retrieveUsers(user_id)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)


















#
# @app.route('/add', methods=['GET', 'POST'])
# def add():
#
#     if request.method == 'POST':
#         todo = request.form['work']
#         dbHandler.insertUser(k=k, v=v, todo=todo)
#         users1 = dbHandler.retrieveUsers()
#         return url_for('')
#     else:
#         return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)