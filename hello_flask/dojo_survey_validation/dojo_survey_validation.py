from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms

   if len(request.form['name'])< 1:
       flash("Name connot be empty")
       return redirect('/')

   if len(request.form['comment'])<1:
       flash("comment cannot be empty")
       return redirect('/')

   if len(request.form['comment'])>120:
       flash("comment exceeds 120 character limit")
       return redirect('/')
   else:
       name = request.form['name']
       location = request.form['dojoloc']
       language = request.form['language']
       comment = request.form['comment']

       return render_template("result.html", name=name, dojoloc=location, language=language, comment=comment)
   # redirects back to the '/' route
   # return redirect('/')
app.run(debug=True) # run our server
