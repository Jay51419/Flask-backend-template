from app import app
# db
from flask import request,jsonify
import json

@app.route("/register",methods=["POST"])
def register():
	data = request.get_json()
	print(data)
	is_user_already_registered = db.users.find_one({'email':data['email']})
	if is_user_already_registered:
		return jsonify({"message":"User is already registered"})
	else:
		try:
			db.users.insert_one({"email":data["email"],"password":data["password"]})
			return jsonify({"message":"Registeration successful"})
		except Exception as e:
			print(e)
			return jsonify({"message":"Something went wrong while registering"})

