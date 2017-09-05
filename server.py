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
			"3. Find Student": "/student/<student_id>"
		}
		return jsonify({'instructions' : output})

api.add_resource(Home, '/')
api.add_resource(StudentList, '/students')
api.add_resource(Student, '/student/<string:student_id>')

if __name__ == '__main__':
    app.run(debug=True)