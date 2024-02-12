# Import necessary modules from Flask and related packages
from flask import Flask
# Import SQLAlchemy: An ORM (Object-Relational Mapping) library that
#  simplifies database interactions within Flask applications
from flask_sqlalchemy import SQLAlchemy
# Import path from the os module: Allows working with file and directory paths.
from os import path
#Part of the Flask-Login extension, facilitating user authentication in Flask applications.
from flask_login import LoginManager

# Create an instance of SQLAlchemy and set the database file name
db = SQLAlchemy()
DB_NAME = "database.db"

# Define a function to create the Flask application
def create_app():
    # Create an instance of the Flask application
    app = Flask(__name__)

    # Configure Flask app settings, including secret key and database URI
    app.config['SECRET_KEY'] = 'allen garcia'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Import blueprints (views and auth) and register them with the app
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import User and Note models from models module
    from .models import User, Note

    # Create all database tables if they do not exist
    with app.app_context():
        db.create_all()

    # Initialize and configure the Flask-Login extension
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Define a function to load a user by ID for Flask-Login
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Return the configured Flask app
    return app

# Function to create the database if it does not exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
