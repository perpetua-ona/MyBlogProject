from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

# @app.route('/')

# def index():
#    return"<h1>Hi world</>"

@app.route('/')

def index():
    first_name = "John"
    books = ["Story", "Programming Books", "Religious Books", 50]
    return render_template ("index.html", first_name=first_name, books=books)

@app.route('/user/<name>')

def user(name):
   return render_template ("test_user.html", name=name)

# Custom Error Pages

# Invalid Url
@app.errorhandler (404)
def page_not_found(e):
    return render_template("error.html")



