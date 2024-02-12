# Import the 'db' instance from the current package
from . import db
# Import UserMixin from Flask-Login for additional User class functionality
from flask_login import UserMixin
# Import 'func' for using database functions like 'func.now()' in the model
from sqlalchemy.sql import func

# Define a model class 'Note' representing notes in the database
class Note(db.Model):
    # Define a primary key column 'id' of type Integer
    id = db.Column(db.Integer, primary_key=True)
    # Define a data column 'data' of type String with a maximum length of 10000 characters
    data = db.Column(db.String(10000))
    # Define a date column 'date' of type DateTime with timezone support, defaulting to the current timestamp
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Define a foreign key column 'user_id' referencing the 'id' column of the 'User' model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Define a model class 'User' representing users in the database
class User(db.Model, UserMixin):
    # Define a primary key column 'id' of type Integer
    id = db.Column(db.Integer, primary_key=True)
    # Define an email column 'email' of type String with a maximum length of 150 characters, unique for each user
    email = db.Column(db.String(150), unique=True)
    # Define a password column 'password' of type String with a maximum length of 150 characters
    password = db.Column(db.String(150))
    # Define a first name column 'first_name' of type String with a maximum length of 150 characters
    first_name = db.Column(db.String(150))
    # Define a relationship to the 'Note' model, establishing a one-to-many relationship (one user, many notes)
    notes = db.relationship('Note')
