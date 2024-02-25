from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

enviornment = os.getenv("FLASK_ENV") #setting environment to production
SCHEMA = os.environ.get("SCHEMA") # for render

db = SQLAlchemy()

def add_prefix_for_prod(attr):
    if enviornment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr
