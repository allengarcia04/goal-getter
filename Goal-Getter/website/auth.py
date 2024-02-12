# Import necessary modules from Flask and related packages
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Import the 'User' model from the 'models' module
from .models import User
# Import password hashing and checking functions from 'werkzeug.security'
from werkzeug.security import generate_password_hash, check_password_hash
# Import the database instance 'db' from the main module
from . import db
# Import Flask-Login functions for user authentication
from flask_login import login_user, login_required, logout_user, current_user

# Create a Blueprint named 'auth'
auth = Blueprint('auth', __name__)


#Define a route for '/login': This creates a route for the login page, allowing both GET and POST requests.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the request method is POST
    if request.method == 'POST':
        #Retrieve email and password: Get user input (email and password) from the login form submitted through POST.
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the database to find a user with the provided email
        user = User.query.filter_by(email=email).first()

        # Check if a user with the given email exists
        if user:
            # Check if the provided password matches the stored hash
            if check_password_hash(user.password, password):
                # Display a success message, log in the user, and redirect to the home page
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                # Display an error message for incorrect password
                flash('Incorrect password, try again.', category='error')
        else:
            # Display an error message for non-existent email
            flash('Email does not exist.', category='error')

    # Render the login template with the current user information
    return render_template("login.html", user=current_user)

    
@auth.route('/logout')
@login_required
def logout():
    # Log out the current user
    logout_user()

    # Display a success message for successful logout
    flash('Logged out successfully!', category='success')

    # Redirect to the login page after logout
    return redirect(url_for('auth.login'))


#Define a route for '/sign-up' with support for both GET and POST requests: 
# This route handles both displaying the sign-up form and processing the form data.
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #Check the request method: Determine if the form is being submitted (POST request)
    if request.method == 'POST':
        # Retrieve user input from the sign-up form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check for existing email: Query the database to check if the email already exists.
        user = User.query.filter_by(email=email).first()
        #Perform validation checks
        #Check various conditions such as email length, first name length, password matching, and password length.
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new user: If all checks pass, create a new user with a hashed password.
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            # Log in the new user
            login_user(new_user, remember=True)

            # Flash a success message for account creation
            flash('Account created!', category='success')

            # Redirect to the home page after successful sign-up
            return redirect(url_for('views.home'))

    # Render the sign-up page template
    return render_template("sign_up.html", user=current_user)
