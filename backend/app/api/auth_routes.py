from flask import Blueprint, request
from app.models import User, db
from app.forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required
auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/', methods=['POST'])
def login():
    form = LoginForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        login_user(form.data['username'])
        return {'message': 'User logged in'}

@auth_routes.route('/logout')
def logout():
    logout_user()
    return {'message': 'User logged out'}

@auth_routes.route('/signup', methods=['POST'])
def signup():
    req = request.get_json()
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password'],
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return {'message': 'User signed up and logged in'}
