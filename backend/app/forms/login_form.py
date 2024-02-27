from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

def user_exists(field):
    email = field.data
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError('The email and/or password did not match our record. Please try again.')

def password_matches(form, field):
    password = field.data
    email = form.data['email']
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError('The email and/or password did not match our record. Please try again.')
    if not user.check_password(password):
        raise ValidationError('The email and/or password did not match our record. Please try again.')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired(), password_matches])
