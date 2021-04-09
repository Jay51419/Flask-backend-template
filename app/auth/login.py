from app import app,db
from flask import request,jsonify


@app.route("/login",methods=['POST'])
def login():
	data = request.get_json()

	return "Welcome to login page"