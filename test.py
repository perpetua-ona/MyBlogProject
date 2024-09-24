from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a flask instance   
app = Flask(__name__)

# Database configuration (Corrected)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Secret Key
app.config['SECRET_KEY'] = "my_secret_key"

# Initialize the database
db = SQLAlchemy(app)

# Create a model
class Users(db.Model):  # db.Model should be capitalized
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Name {self.name}>'

# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Enter Your Full Name", validators=[DataRequired()])
    email = StringField("Enter Your Full Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a Form Class
class NamerForm(FlaskForm,):
    name = StringField("Enter Your Full Name", validators=[DataRequired()])
    submit = SubmitField("Submit") 

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    our_user = Users.query.order_by(Users.date_added).all()  # Initialize our_user for both GET and POST

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()  # Get the first result, if any
        if user is None:
            # Create a new user if no existing user is found
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash("User Added")
        else:
            flash("User already exists.")

        # Reset the form fields
        name = form.name.data
        form.name.data = ''
        form.email.data = ''

        # Re-fetch the list of users after adding a new user
        our_user = Users.query.order_by(Users.date_added).all()

    return render_template("add.html", form=form, name=name, our_user=our_user)

    
@app.route('/')
def index():
    first_name = "John"
    books = ["Story", "Programming Books", "Religious Books", 50]
    return render_template("index.html", first_name=first_name, books=books)

@app.route('/user/<name>')
def user(name):
   return render_template("test_user.html", name=name)

# Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Submit Success")
        
    return render_template("name.html", name=name, form=form)

if __name__ == '__main__':
    app.run(debug=True)
