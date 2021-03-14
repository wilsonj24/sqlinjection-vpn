# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3
app = Flask(__name__)
app.database = "data.db"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    g.db = connect_db()
    error = None
    if request.method == 'POST':
    #    username = request.form[username]

        cur = g.db.execute("select username from managers where username=\""+request.form['username']+"\""+"and password=\""+request.form['password']+"\"")

        username=cur.fetchone()
        if username is None:
            error = 'Invalid Credentials. Please try again'
            return render_template('log.html', error=error)
        else:
            return redirect(url_for('hello'))
    else:
        return render_template('log.html', error=error)


#cur = g.db.execute('select username from managers where username=‘+’request.form[‘username’]’+’and password=‘+‘ request.form[‘password’]')


@app.route('/hello')
def hello():
    g.db = connect_db()
    cur = g.db.execute('select * from Customers')
    Customers = [dict(id=row[0], firstname=row[1], lastname=row[2], age=row[3], street=row[4], city=row[5], state=row[6], zip=row[7], salary=row[8], eyecolor=row[9], dob=row[10], religion=row[11], politicalaffiliation=row[12], relationshipstatus=row[13], ethnicity=row[14]) for row in cur.fetchall()]
    g.db.close()
    return render_template('hello.html', Customers=Customers)


@app.route('/about')
def about():
    return render_template('about.html')




def connect_db():
    return sqlite3.connect(app.database)

#@app.route('/log', methods=['GET', 'POST'])
#def log():
#    error = None
#    if request.method == 'POST':
#        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#            error = 'Invalid Credentials. Please try again'
#        else:
#            return redirect(url_for('hello'))
#    return render_template('log.html', error=error)



if __name__ == '__main__':
    app.run(debug=True)
