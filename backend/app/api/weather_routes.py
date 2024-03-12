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
    sql_command = """
        SELECT name
        FROM Weather
        GROUP BY name;
    """
    result = db.session.execute(sql_command)
    # weather_all = Weather.query.all()
    # weather_data =[weather.to_dict() for weather in weather_all]
    # df = pd.DataFrame(weather_data)
    # df['date'] = pd.to_datetime(df['date']).dt.date
    # result = df.groupby(['date','name']).agg({'rain': 'sum', 'snow': 'sum'}).reset_index()
    # x = result.to_dict(orient='records')
    result_dict = [dict(row) for row in result]
    return result_dict

@weather_routes.route('/<string:location>')
# def get_location(location):
#     location = Weather.query.filter_by(name=location).all()
#     weather_data =[x.to_dict() for x in location]
#     df = pd.DataFrame(weather_data)
#     df['date'] = pd.to_datetime(df['date']).dt.date
#     result = df.groupby(['date','name']).agg({'rain': 'sum', 'snow': 'sum'}).reset_index()
#     x = result.to_dict(orient='records')
#     print(x)
#     return x

def get_location(location):
    sql_command = """
        SELECT  strftime('%Y', date) AS year, Date(date) AS date, name, SUM(COALESCE(rain,0)) AS rain, SUM(COALESCE(snow,0)) AS snow
        FROM Weather
        WHERE name = :location
        GROUP BY Date(date), name;
    """
    result = db.session.execute(sql_command, {'location': location})

    result_dict = [dict(row) for row in result]
    return result_dict
