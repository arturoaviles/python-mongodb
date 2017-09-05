# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api
from dotenv import load_dotenv, find_dotenv # .env variables
load_dotenv(find_dotenv()) # Load .env file

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = os.environ.get("DB_NAME")
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

app.url_map.strict_slashes = False # Disable redirecting on POST method from /star to /star/

mongo = PyMongo(app)

class Student(Resource):
	def get(self, student_id):
		students = mongo.db.students
		search = students.find_one({'student_id' : student_id})
		if search:
			output = {
				'student_id': search['student_id'], 
				'first_name': search['first_name'],
				'last_name': search['last_name']
			}
		else:
		    output = "No such student"
		return jsonify({'result' : output})

	def post(self):
	        students = mongo.db.students
	        student_id = request.json['student_id']
	        first_name = request.json['first_name']
	        last_name = request.json['last_name']

	        object_id = students.insert({
	         	'student_id': student_id, 
	         	'first_name': first_name,
	         	'last_name': last_name
	        })
	        
	        new_student = students.find_one({'_id': object_id })
	        output = output = {
				'student_id': new_student['student_id'], 
				'first_name': new_student['first_name'],
				'last_name': new_student['last_name']
			}
	        return jsonify({'result' : output})

class StudentList(Resource):
	def get(self):
		students = mongo.db.students
		output = []
		for student in students.find():
		    output.append({
		    	'student_id': student['student_id'], 
		    	'first_name': student['first_name'],
		    	'last_name': student['last_name']
		    })
		return jsonify({'result' : output})

class Home(Resource):
	def get(self):
		output = {
			"1. Home": "/",
			"2. Students": "/students",
			"3. Find Student": "/students/<student_id>"
		}
		return jsonify({'instructions' : output})

api.add_resource(Home, '/')
api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<string:student_id>')

if __name__ == '__main__':
    app.run(debug=True)