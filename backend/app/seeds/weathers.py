from app.models import db, User, environment, SCHEMA, Weather
from sqlalchemy.sql import text
from .weather_data import data
from datetime import datetime
def seed_weather():
    records_to_insert = [
        Weather(
            name=entry['name'],
            date=datetime.strptime(entry['date'], '%Y-%m-%d %H:%M:%S'),
            temp=entry['temp'],
            weather=entry['weather'],
            wind=entry['wind'],
            snow=entry['snow'],
            rain=entry['rain'],
        )
        for entry in data
    ]
    # demo_channel = Weather(
    #     admin_id = User.query.filter(User.username == 'DemoAdmin').first().id,
    #     title = 'Demo Channel'
    # )
    # another_demo_channel = Weather(
    #     admin_id = User.query.filter(User.username == 'DemoAdmin').first().id,
    #     title = 'Another Demo Channel'
    # )


    # all_channels = [demo_channel, another_demo_channel]
    # for channel in all_channels:
    #     existing_channel = Channel.query.filter_by(title=channel.title).first()
    #     if not existing_channel:
    #         db.session.add(channel)
    # db.session.commit()

    db.session.add_all(records_to_insert)
    db.session.commit()

def undo_weather():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.weather RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM weather"))

    db.session.commit()
