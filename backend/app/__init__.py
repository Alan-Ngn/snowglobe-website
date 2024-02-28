import os;
from flask import Flask, request, redirect, send_file #Imports Flask (the main Flask class for creating the application), request (for accessing incoming request data), session (for session management), and redirect (for redirecting requests).
from flask_cors import CORS #Imports Cross-Origin Resource Sharing (CORS) support for Flask applications, allowing the application to handle cross-origin HTTP requests.
from flask_wtf.csrf import generate_csrf #generating CSRF tokens
from flask_login import LoginManager #provides user session management for Flask applications
from .config import Config #configuration settings for the Flask application.
from .api import auth_routes, weather_routes
from .models import db, User
from .seeds import seed_commands
from flask_migrate import Migrate
app = Flask(__name__, static_folder='../../frontend/public', static_url_path='/') #Creates a Flask application instance, specifying the static folder for serving static files (e.g., CSS, JS) from the React build.

login = LoginManager(app)
print(__name__)
CORS(app) #Enables CORS support for the application. pip install flask-cors

app.cli.add_command(seed_commands)
app.config.from_object(Config)
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(weather_routes, url_prefix='/api/weathers')
db.init_app(app)
Migrate(app, db)


# @app.before_request
# def https_redirect():
#     if os.environ.get('FLASK_ENV') == 'production':
#         if request.headers.get('X-Forwarded-Proto') == 'http':
#             url = request.url.replace('http://', 'https://', 1)
#             code = 301
#             return redirect(url, code=code)


# @app.after_request
# def inject_csrf_token(response):
#     response.set_cookie(
#         'csrf_token',
#         generate_csrf(),
#         secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
#         samesite='Strict' if os.environ.get(
#             'FLASK_ENV') == 'production' else None,
#         httponly=True)
#     return response











@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

    # return {'message': 'Test login route'}
