from flask import Blueprint, request
from app.models import User, db
from flask_login import login_user, logout_user, login_required
auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/')
def login():
    
