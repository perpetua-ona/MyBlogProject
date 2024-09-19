from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

# @app.route('/')

# def index():
#    return"<h1>Hi world</>"

@app.route('/')

def index():
    return render_template ("index.html")

@app.route('/user/<name>')

def user(name):
    return"<h1>Hi {}</>".format(name) 




