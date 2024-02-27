from flask import Blueprint, request, make_response
from app.models import Weather, db
from flask_login import current_user, login_required
from app.forms import WeatherForm

weather_routes = Blueprint('weathers', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages

@weather_routes.route('/')
def get_weather():
    weather = Weather.query.all()
    return weather.to_dict()
