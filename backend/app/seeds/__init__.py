from flask.cli import AppGroup
# from .users import seed_users, undo_users
from .weathers import seed_weather, undo_weather
from .locations import seed_location, undo_location
# from .messages import seed_messages, undo_messages
# from .members import seed_members, undo_members
# from .replies import seed_replies, undo_replies
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_location()
        undo_weather()
    seed_weather()
    seed_location()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_weather()
    undo_location()

    # Add other undo functions here
