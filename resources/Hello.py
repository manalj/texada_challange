from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello Texada! Welcome to my amazing API!"}
