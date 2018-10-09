curl -i http://localhost:5000/api/

curl -i http://localhost:5000/api/Record/

curl -i http://localhost:5000/api/upload

curl -i http://localhost:5000/api/Record/37

curl -H 'Content-Type: application/json' -X POST -d '{"description": "Cesna NEW","datetime": "2016-10-12T12:00:00-05:00","longitude": "43.0583264","latitude": "-81.0149807","elevation": "200"}' http://localhost:5000/api/Record/

curl -i -X PUT -H "Content-Type: multipart/form-data"\
  -F "description=New Description"\
  -F "datetime=2006-10-12T12:00:00-05:00"\
  -F "longitude=3.2583264"\
  -F "latitude=-8.8149807"\
  -F "elevation=200"\
  http://localhost:5000/api/Record/37

curl -X "DELETE" http://localhost:5000/api/Record/37
