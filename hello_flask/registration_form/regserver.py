from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    # query = "SELECT * FROM email"                          # define your query
    # email = mysql.query_db(query)
    return render_template('index.html') # pass data to our template

@app.route('/process', methods=['POST'])
def process():

    if len(request.form['first_name']) < 1:
        flash("first name cannot be blank")
        return redirect('/')
    elif re.match("[0-9]",request.form['first_name']):
        flash("first name cannot contain numbers")
        return redirect('/')
    elif len(request.form['last_name']) < 1:
        flash("last name cannot be blank")
        return redirect('/')
    elif re.match("[0-9]",request.form['last_name']):
        flash("last name cannot contain numbers")
        return redirect('/')
    elif len(request.form['email']) < 1:
        flash("Email cannot be empty")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['password'])<8:
        flash("Password cannot be less than 8 chracters!")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("passwords do not match")
        return redirect('/')
    else:
        session['firstname']= request.form('first_name')
        session['lastname']= request.form('last_name')
        session['email'] = request.form('email')
        session['password']=request.form('password')
        session['confrim'] = request.form('confrim_password')
        return redirect('/')


    return redirect('/')

app.run(debug=True)
