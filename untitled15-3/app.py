from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import model as dbHandler
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():

    con = sqlite3.connect("pvt.db")
    cur = con.cursor()
    cur.execute("SELECT Use, pas FROM User")
    items = cur.fetchall()
    error = None
    # user_id = request.cookies.get('use')
    # user_data = request.cookies.get('data')
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
    users = dbHandler.retrieveUsers(user_id)
    if request.method == 'POST':
        todo = request.form['work']
        ngay = request.form['date']
        dbHandler.insertUsers(todo, user_id, ngay)
        data = dbHandler.retrieveUsers(user_id)

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
        error = None
    return render_template('index.html', users = users, error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    a = []
    con = sqlite3.connect("pvt.db")
    cur = con.cursor()
    cur.execute("SELECT Use, pas FROM User")
    items = cur.fetchall()
    error = None

    if request.method == 'POST':
        name = request.form['user']
        pas = request.form['pass']
        dbHandler.registerUser(name, pas)

        return redirect(url_for('login'))
    else:
       # error = 'False'
        return render_template('register.html', error=error)

@app.route('/remove')
def remove():
    a = []
    user_id = request.cookies.get('user')
    users = dbHandler.retrieveUsers(user_id)

    for user in users:
        a.append(user)
    dbHandler.removeUsers(user)

    return redirect(url_for('index'))

@app.route('/edit')
def edit():
    return 'okie'

if __name__ == '__main__':
    app.run(debug=True)
