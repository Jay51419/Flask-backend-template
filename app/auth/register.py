from app import app, db, get_hashed_password
from flask import request,jsonify
import json

@app.route("/register",methods=["POST"])
def register():
	data = request.get_json()
	print(data)
	is_user_already_registered = db["users"].find_one({"email":data["email"]}) 
	if is_user_already_registered:
		return jsonify({"message":"User is already registered"})
	else:
		try:
			hashed_password = get_hashed_password(data["password"].encode('utf-8'))
			db.users.insert_one({"email":data["email"],"password":hashed_password,'college':""})
			return jsonify({"message":"Registeration successful"})
		except Exception as e:
			print(e)
			return jsonify({"message":"Something went wrong while registering"})

