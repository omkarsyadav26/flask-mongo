# flask-mongo
### connecting flask container with mongo container using docker-compose
To build this project just use bellow command
```
docker-compose -f flask-mongo-compose.yml up --build
```
Once the project is up and running
To post some data inside mongo use bellow command
```
 curl -X POST   http://localhost:5000/student -H 'content-type: application/json' -d '{"name" : "omkar", "roll_no" : 2334}'
```
To get data from mongo use bellow command
```
curl http://localhost:5000/student
```
