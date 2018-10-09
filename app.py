from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Record import RecordResource
from resources.UploadCSV import UploadCSV


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/')
api.add_resource(UploadCSV, '/upload')
api.add_resource(RecordResource, '/Record/', '/Record/<int:id>', '/Record/page=<int:page>')
