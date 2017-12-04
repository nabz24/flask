from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', friends=friends) # pass data to our template



@app.route('/process', methods=['POST'])
def create():
    # if len(request.form('firstname')>1):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name': request.form['firstname'],
                'last_name':  request.form['lastname'],
                'occupation': request.form['occupation']
                }
    # Run query, with dictionary values injected into the query.
        print data
        mysql.query_db(query, data)
        return redirect('/')
    # return redirect('/process/' + str(friend_id))

@app.route('/delete/<friend_id>', methods=['POST'])
def delete(friend_id):
    print "there"
    query = "DELETE FROM friends WHERE id = :id "
    print query
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/update/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/edit/<friend_id>')
def edit(friend_id):
    print "variable from url", friend_id;

    return render_template("edit.html", friendID = friend_id)


# @app.route('/process/<friend_id>', methods=['GET'])
# def u(friend_id):
#     query= "SELECT friends.first_name, friends.last_name, friends.occupation FROM friends"
#
#     friends=mysql.query_db(query)
#     return redirect('/')


app.run(debug=True)
