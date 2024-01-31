
# Import the Flask module
from flask import Flask, render_template

# Create a Flask app object
app = Flask(__name__)

# Define the route for the main page
@app.route("/")
def index():
    """
    Renders the index.html page.

    Returns:
        The rendered index.html page.
    """
    return render_template("index.html")

# Define the route for the about page
@app.route("/about")
def about():
    """
    Renders the about.html page.

    Returns:
        The rendered about.html page.
    """
    return render_template("about.html")

# Define the route for the contact page
@app.route("/contact")
def contact():
    """
    Renders the contact.html page.

    Returns:
        The rendered contact.html page.
    """
    return render_template("contact.html")

# Run the Flask app
if __name__ == "__main__":
    app.run()


This code defines a simple Flask application with three routes: "/", "/about", and "/contact". Each route is associated with a corresponding HTML file ("index.html", "about.html", and "contact.html", respectively) that is rendered when the route is accessed. The code uses Flask's `render_template` function to render the HTML files. The application is started by running the `app.run()` method.