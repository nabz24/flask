from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    if session.get('count') == None:
        print "Thid"
        session['count'] = 0
    else:
        session['count'] += 1
        print session['count']
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
 # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!





app.run(debug=True) # run our server
