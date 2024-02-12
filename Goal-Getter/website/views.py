# Import necessary modules from Flask and related packages
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note  # Import the Note model from the models module
from . import db  # Import the SQLAlchemy instance 'db' from the current package
import json  # Import the JSON module for handling JSON data

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)

# Define a route for '/' with support for both GET and POST requests
@views.route('/', methods=['GET', 'POST'])
@login_required  # Require the user to be logged in to access this route
def home():
    if request.method == 'POST':
        # Retrieve note input from the form
        note = request.form.get('note')

        if len(note) < 1:
            # Flash an error message if the note is too short
            flash('Note is too short!', category='error')
        else:
            # Create a new Note object and add it to the database
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            # Flash a success message for adding the note
            flash('Note added.', category='success')

    # Render the home page template and pass the current user to the template
    return render_template("home.html", user=current_user)

# Define a route for '/delete-note' with support for POST requests
@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Load JSON data from the request
    note = json.loads(request.data)
    noteId = note['noteId']
    
    # Query the database to get the Note with the given ID
    note = Note.query.get(noteId)
    
    if note:
        # Check if the current user owns the note
        if note.user_id == current_user.id:
            # Delete the note from the database
            db.session.delete(note)
            db.session.commit()
            
            # Flash a success message for deleting the note
            flash('Note deleted.', category='success')

    # Return an empty JSON response
    return jsonify({})
