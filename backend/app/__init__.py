import os;
from flask import Flask, request, redirect, send_file #Imports Flask (the main Flask class for creating the application), request (for accessing incoming request data), session (for session management), and redirect (for redirecting requests).
from flask_cors import CORS #Imports Cross-Origin Resource Sharing (CORS) support for Flask applications, allowing the application to handle cross-origin HTTP requests.
from flask_wtf.csrf import generate_csrf #generating CSRF tokens
from flask_login import LoginManager #provides user session management for Flask applications
from .config import Config #configuration settings for the Flask application.
from .api import auth_routes
from .models import db, User
from .seeds import seed_commands
from flask_migrate import Migrate
app = Flask(__name__, static_folder='../../frontend/public', static_url_path='/') #Creates a Flask application instance, specifying the static folder for serving static files (e.g., CSS, JS) from the React build.

login = LoginManager(app)

CORS(app) #Enables CORS support for the application. pip install flask-cors

app.cli.add_command(seed_commands)
app.config.from_object(Config)
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)
Migrate(app, db)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

    # return {'message': 'Test login route'}
