from flask import Blueprint, request, make_response
from app.models import Weather, db
from flask_login import current_user, login_required
from app.forms import WeatherForm
import pandas as pd
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
    weather_all = Weather.query.all()
    weather_data =[weather.to_dict() for weather in weather_all]
    df = pd.DataFrame(weather_data)
    df['date'] = pd.to_datetime(df['date']).dt.date
    result = df.groupby(['date','name']).agg({'rain': 'sum', 'snow': 'sum'}).reset_index()
    x = result.to_dict(orient='records')
    return x

@weather_routes.route('/<string:location>')
def get_location(location):
    location = Weather.query.filter_by(name=location).all()
    weather_data =[x.to_dict() for x in location]
    df = pd.DataFrame(weather_data)
    df['date'] = pd.to_datetime(df['date']).dt.date
    result = df.groupby(['date','name']).agg({'rain': 'sum', 'snow': 'sum'}).reset_index()
    x = result.to_dict(orient='records')
    return x
