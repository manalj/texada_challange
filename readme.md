## Description
This project implements a simple RESTful API in Flask framework.


## Requirements
This project runs on python 3.5.2, and requires multiple libraries found in requirements.txt. To install all the requirements, run the following command:

```
$ pip install -r requirements.txt
```
The database used for this project runs on PostgreSQL.


## Details about the implementation

This project implements a simple RESTful API based on python's Flask framework. The features offered are the CRUD operations on a table "Records" in the PostgreSQL database, as well as pagination of the records.

The starting point is the run.py file which imports the packages and starts the server.

config.py includes the configuration to connect to the database. The configuration should be changed depending on the hosting machine.

model.py includes the model of our table Records, which is implemented using SQLAlchemy to avoid the use of SQL queries in the code. The file also includes the validation schema for the table, which is automatically executed when adding or updating a record.

app.py includes the routes that can be used to interact with the API. See How to run section for a list of all possible routes. The routes use Resources which in a larger application would represent a module that encapsulates all the interactions with a table.

Under resources, we have all the resources used in this API. The resource Record.py deals with all CRUD operations for the table Record. The resource Hello.py simply returns a message at the start of the server. UploadCSV.py contains the code for uploading the records in input.txt to the table Record in the database.


## Installation

To run this project, first all required libraries in requirements.txt must be installed. Then a database must be created on PostgreSQL, with a table Record:

```
CREATE DATABASE texada;

\c texada

CREATE TABLE records (
    id              integer CONSTRAINT firstkey PRIMARY KEY,
    description     varchar(250) NOT NULL,
    datetime        TIMESTAMP,
    longitude       numeric,
    latitude        numeric,
    elevation       numeric
);
```


Start the server by running the following command:
```
$ python run.py
```


## How to run

Once the server is started, the API can be accessed on a browser using the URL:

```
http://localhost:5000/api/
```

To list all records in the table:
```
http://localhost:5000/api/Record/
```

To list all records with pagination:
```
http://localhost:5000/api/Record/page=2
```

To show a record using its id:
```
http://localhost:5000/api/Record/<id>
```

The same URL can be used to update or delete a record. The request can be of type GET, PUT or DELETE.


To upload the input.txt file into the database:
```
http://localhost:5000/api/upload
```

To add a new record, use a POST request to the url:
```
http://localhost:5000/api/Record
```

All requests were tested using curl. See test.sh file for all curl commands used.


## Author
Manal Jazouli,
Email: <manaljaz@gmail.com>
