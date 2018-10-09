from flask import request
from flask_restful import Resource
from model import db, Record, RecordSchema

records_schema = RecordSchema(many=True)
record_schema = RecordSchema()

class RecordResource(Resource):
    ## Get all records about the products or by get record by id
    def get(self, id=None, page=None):
        if not id:
            ## If page is not used
            if not page:
                ## Fetch all records in the database
                records = Record.query.all()
                ## Deserialize the data
                records = records_schema.dump(records).data
                return {'status': 'success', 'data': records}, 200

            ## Fetch with pagination
            pagination = Record.query.paginate(page,3,error_out=False)
            records = records_schema.dump(pagination.items).data
            return {'status': 'success', 'data': records}, 200

        record = Record.query.filter_by(id=id).first()
        if not record:
            return {'message': 'Record does not exist'}, 400
        result = record_schema.dump(record).data
        return {'status': 'success', 'data': result}, 200




    ## Add a new record about a product
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = record_schema.load(json_data)
        if errors:
            return errors, 422

        record = Record(
            description = data['description'],
            longitude = data['longitude'],
            latitude = data['latitude'],
            elevation = data['elevation']
        )

        db.session.add(record)
        db.session.commit()

        result = record_schema.dump(record).data

        return { "status": 'success', 'data': result }, 201


    def put(self, id):

        if not id:
               return {'message': 'No record id provided'}, 400
        # Validate and deserialize input
        data, errors = record_schema.load(id)
        if errors:
            return errors, 422
        record = Record.query.filter_by(id=id).first()
        if not record:
            return {'message': 'Record does not exist'}, 400

        record.description = data['description']
        record.longitude = data['longitude']
        record.latitude = data['latitude']
        record.elevation = data['elevation']

        db.session.commit()

        result = record_schema.dump(record).data

        return { "status": 'success', 'data': result }, 204


    def delete(self, id):
        # json_data = request.get_json(force=True)
        if not id:
               return {'message': 'No record id provided'}, 400
        # Validate and deserialize input
        data, errors = record_schema.load(id)
        if errors:
            return errors, 422
        record = Record.query.filter_by(id=id).delete()
        db.session.commit()

        result = record_schema.dump(record).data

        return { "status": 'success', 'data': result}, 204
