from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3
import model as dbHandler
app = Flask(__name__)

@app.route('/set')
def setcookie():
    resp = make_response('setting cookie!')
    resp.set_cookie('framework', 'flask', 'alo')
    return resp
@app.route('/get')
def setcookir():
    framework = request.cookies.get('framework')
    return 'the framework is ' + framework


if __name__ == '__main__':
    app.run(debug=True)