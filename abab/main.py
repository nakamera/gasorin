import os
from abab import app #インポートしている
from flask import render_template, request,redirect,url_for #インポートしている
from flask import send_from_directory
import sqlite3
DATABASE='database.db'
@app.route('/') #webアプリのトップのurlにリクエストがきたらindexの関数が動く
def index():  #renderを使ってindex.htmlを呼びたい
    con=sqlite3.connect(DATABASE)
    db_books=con.execute('SELECT*FROM books').fetchall()
    con.close()
    
    books=[ ]
    for row in db_books:
        books.append({'title':row[0],'price':row[1],'arrival_day':row[2]})
        
    return render_template(
        'index.html',
        books=books
        
    )
    
@app.route('/form')
def form():
        return render_template(
            'form.html'
        )
        
@app.route('/register',methods=['post'])
def register():
    title=request.form['title']
    price=request.form['price']
    arrival_day=request.form['arrival_day']
    con=sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?,?)',
                [title,price,arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))
    
                