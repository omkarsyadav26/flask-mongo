from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'store'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/store'

mongo = PyMongo(app)

@app.route('/student', methods=['GET'])
def get_all_students():
  student = mongo.db.students
  output = []
  for s in student.find():
    output.append({'name' : s['name'], 'roll_no' : s['roll_no']})
  return jsonify({'result' : output})

@app.route('/student/', methods=['GET'])
def get_one_student(name):
  student = mongo.db.students
  s = student.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'roll_no' : s['roll_no']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/student', methods=['POST'])
def add_student():
  student = mongo.db.students
  print("------------------", request)
  req = request.get_json()
  name = req['name']
  roll_no = req['roll_no']
  student_id = student.insert({'name': name, 'roll_no': roll_no})
  new_student = student.find_one({'_id': student_id })
  output = {'name' : new_student['name'], 'roll_no' : new_student['roll_no']}
  return {"respose" : output}

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
