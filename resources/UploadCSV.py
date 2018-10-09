from numpy import genfromtxt

from flask import request
from flask_restful import Resource
from model import db, Record, RecordSchema


class UploadCSV(Resource):
    def get(self):

        data = genfromtxt("./input.txt", delimiter=',', skip_header=1, dtype=str)
        data = data.tolist()

        for row in data:
          description = row[1]
          datetime = row[2]
          longitude = row[3]
          latitude = row[4]
          elevation = row[5]

          record = Record( description=description, datetime=datetime, longitude=longitude, latitude=latitude, elevation=elevation)
          db.session.add(record)
          # db.session.flush()
          db.session.commit()

        return {"message": "CSV file uploaded to database!"}
