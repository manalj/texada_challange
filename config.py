import os

# Setting up the configuration for the database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://manaljazouli@localhost/texada"
# SQLALCHEMY_DATABASE_URI = "postgresql://manaljazouli@localhost:5432/texada"
