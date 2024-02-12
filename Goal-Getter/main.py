# Import the create_app function from the website package
from website import create_app

# Create an instance of the Flask application using the create_app function
app = create_app()

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)

"""This script serves as the entry point to the Flask application. 
It imports the create_app function from the website package, creates an 
instance of the Flask application,and runs it in debug mode when the 
script is executed directly."""