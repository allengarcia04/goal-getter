How it works:

1. main.py:
   -Entry point of the application.
   -Creates an instance of the Flask app using the create_app function from the website package.
   -Runs the app in debug mode if executed directly.

2. **init**.py:
   -Initializes the Flask app, SQLAlchemy for database management, and Flask-Login for user authentication.
   -Registers blueprints (views and auth) to organize routes.
   -Creates necessary database tables.
   -Configures Flask-Login to manage user sessions.

3. views.py:
   -Contains routes and views related to the main functionality of the application.
   -home() displays the home page where users can view, add, and delete notes.
   -delete_note() handles the deletion of notes via a POST request.

4. auth.py:
   -Manages user authentication and related routes.
   -login(), logout(), and sign_up() handle user login, logout, and sign-up, respectively.

5. models.py:
   -Defines the structure of the database using SQLAlchemy.
   -Contains User and Note models with relationships between them.

6. base.html:
   -The base template for other HTML files to extend.
   -Defines the common structure, navigation bar, and includes necessary CSS and JavaScript libraries.
   -Handles displaying flashed messages (alerts) and defines blocks for content and additional JavaScript.

7. login.html:
   -Extends base.html and provides a form for user login.

8. sign_up.html:
   Extends base.html and provides a form for user registration.

9. home.html:
   -Extends base.html and displays user notes along with a form to add new notes.

10. JavaScript (in base.html):
    -Provides a function (deleteNote()) for asynchronous note deletion.

Interaction Flow:
-Users interact with the application through the routes defined in views.py and auth.py.
-Authentication is managed by Flask-Login, and user data is stored in the database.
-Views access the database to retrieve and manipulate user notes.
-Templates, especially base.html, provide a common structure and handle the display of messages and dynamic content.
-The project follows a standard Flask architecture with separate files for routes, templates, models, and static content. The application's core functionality revolves around managing user notes, authentication, and displaying relevant views.
