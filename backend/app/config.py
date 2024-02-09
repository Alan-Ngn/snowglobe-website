import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://') #Sets the SQLALCHEMY_DATABASE_URI attribute to the value of the 'DATABASE_URL' environment variable. This is the connection URI for the SQLAlchemy database. The line also performs a replacement to ensure compatibility with PostgreSQL databases, as some systems might use 'postgres://' in the URL, while SQLAlchemy expects 'postgresql://'.
    SQLALCHEMY_ECHO = True #Enables SQLAlchemy echo mode. When set to True, this option causes SQLAlchemy to log all the SQL statements it executes. This can be helpful during development and debugging but is typically turned off in production.
