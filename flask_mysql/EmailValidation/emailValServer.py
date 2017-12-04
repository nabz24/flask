from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'email')

@app.route('/')
def index():
    # query = "SELECT * FROM email"                          # define your query
    # email = mysql.query_db(query)
    return render_template('index.html') # pass data to our template



@app.route('/success', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!") # just pass a string to the flash function
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
   # just pass a string to the flash function
    else:
        flash("Success! Your name is {}".format(request.form['email']))
        query = "INSERT INTO email (email_address, entered_at) VALUES (:email_address, NOW())"
        data = {
                'email_address': request.form['email']
              }

        print data
        user_id=mysql.query_db(query, data)

        return redirect('/success/' + str(user_id)) # either way the application should return to the index and display the message

    # query = "INSERT INTO email (email_address, entered_at) VALUES (:email_address, NOW())"
    # data = {
    #          'email_address': request.form['email']
    #        }
    # mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success/<user_id>', methods=['GET'])
def u(user_id):
    query= "SELECT email.email_address, email.entered_at FROM email"

    emails=mysql.query_db(query)
    return render_template('/success.html', emails=emails) # either way the application should return to the index and display the message

app.run(debug=True)
