from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, DateTimeField
from wtforms.validators import DataRequired, ValidationError

class WeatherForm(FlaskForm):
    date = DateTimeField('date', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    weather = StringField('weather', validators=[DataRequired()])
    snow = FloatField()
    wind = FloatField()
    rain = FloatField()
