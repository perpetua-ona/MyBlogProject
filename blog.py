from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

@app.route('/')

def index():
    return"<h1>Hi world</>"
