import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    if session.get('number') == None:
        session['number'] = random.randrange(0,101)

    # if session.get('num') == random.randrange(0,101):
    #     print "you won"
    # else:
    #    print "you lost"
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def getNum():

    session['user_num'] = int(request.form['user_num'])
    return redirect("/")

    # if session['num'] == session['number']:
    #     print session['number']
    #     print "you won"
    # else:
    #     print session['number']
    #     print "you lost"
    # return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session["number"] = None
    session["user_num"] = None
    return redirect('/')

app.run(debug=True) # run our server
