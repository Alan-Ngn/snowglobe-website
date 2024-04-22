from app.models import db, environment, SCHEMA, Location
from sqlalchemy.sql import text
from .location_data import data
from datetime import datetime
def seed_location():
    records_to_insert = [
        Location(
            name=entry['name'],
            url=entry['url']
        )
        for entry in data
    ]

    db.session.add_all(records_to_insert)
    db.session.commit()

def undo_location():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.location RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM location"))

    db.session.commit()
