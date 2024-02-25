from .db import db, enviornment, SCHEMA, add_prefix_for_prod, func

class Weather(db.Model):
    __tablename__='weather' #does this need to be plural?

    if enviornment == "production":
        __table_args__= {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    weather = db.Column(db.String(255), nullable=False)
    snow = db.Column(db.Float, nullable=True)
    wind = db.Column(db.Float, nullable=True)
    rain = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
