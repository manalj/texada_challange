from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

## Defining the model and its columns as it is in the database
class Record(db.Model):
    __tablename__ = 'records'
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    # datetime    = db.Column(db.TIMESTAMP(timezone=False), server_default=db.func.current_timestamp(), nullable=False)
    datetime    = db.Column(db.TIMESTAMP(timezone=False), nullable=False)
    longitude   = db.Column(db.Float, nullable=False)
    latitude    = db.Column(db.Float, nullable=False)
    elevation   = db.Column(db.Float, nullable=False)


## Validation for each field
class RecordSchema(ma.Schema):
    id          = fields.Integer()
    description = fields.String(required=True)
    datetime    = fields.DateTime()
    longitude   = fields.Float(required=True)
    latitude    = fields.Float(required=True)
    elevation   = fields.Float(required=True)
